from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.postgres.fields import ArrayField
from django.utils.text import slugify
from django.dispatch import receiver
from django.urls import reverse, reverse_lazy
from django.core.validators import MaxValueValidator, MinValueValidator


# This sets the default user that every newly created user will follow after signing up
def set_default_following():
    default_user = ['admin']
    return list(default_user)


class SocialUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(
        max_length=200, default="No bio has been added yet...")
    location = models.CharField(max_length=30, blank=True)
    age = models.IntegerField(blank=True, validators=[
                              MaxValueValidator(120), MinValueValidator(1)], null=True)
    join_date = models.DateTimeField(auto_now=True)
    following = ArrayField(models.CharField(
        max_length=100), blank=True, null=True, default=set_default_following)
    profile_image = models.CharField(max_length=100, default="placeholder")

    class Meta:
        ordering = ('-join_date',)

    def __str__(self):
        return f"{self.user.username}"

    def get_absolute_url(self):
        # Needed for posting something
        return reverse("profile", kwargs={"viewed_user_id": self.pk})
        # Alternative:
        # return reverse('timeline')

    def readable_datetime(self, *args, **kwargs):
        return self.join_date.strftime("%B %d, %Y at %H:%M")

    def number_of_posts(self):
        return self.user.post_author.all().count()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        SocialUser.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.socialuser.save()


class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, related_name="post_author")
    title = models.CharField(max_length=50, null=False)
    excerpt = models.CharField(max_length=500)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=False, unique=True)
    content = models.TextField(null=False)
    likes = models.ManyToManyField(
        User, related_name="post_likes", blank=True
    )
    images = ArrayField(models.CharField(
        max_length=1000), blank=True, null=True)
    featured_image = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f"{self.created} - {self.title}"

    def get_absolute_url(self):
        # Needed for posting something
        return reverse("post-details", kwargs={"slug": self.slug})
        # Alternative:
        # return redirect('timeline')

    def save(self, *args, **kwargs):
        # If no slug exists, auto-generate a slug for the post and make sure that the slug does not exist already. If it does, tack on a number
        if not self.slug:
            self.slug = slugify(self.title)
            number = 1
            # Pull all posts from the database:
            all_posts = Post.objects.all()
            # Compile a list of all existing slugs
            all_slugs = []
            for post in all_posts:
                all_slugs.append(post.slug)
            # If the generated slug exists, create a new one by adding a number to the existing one
            while self.slug in all_slugs:
                self.slug = slugify(self.title)
                self.slug += f"-{str(number)}"
                number += 1

        # Auto-generate an excerpt for the post
        if not self.excerpt:
            if len(self.content) < 50:
                self.excerpt == self.content
            else:
                self.excerpt = ""
                list_of_words = self.content.split()
                for i in range(30):
                    self.excerpt += list_of_words[i]
                    self.excerpt += " "
                self.excerpt += "..."

        # Auto-generate a featured image
        try:
            self.featured_image = self.images[0]
        except IndexError:
            self.featured_image = "placeholder"
        super(Post, self).save(*args, **kwargs)

    def number_of_likes(self, *args, **kwargs):
        return self.likes.count()

    def number_of_comments(self, *args, **kwargs):
        return Comment.objects.filter(post=self.id).count()

    def number_of_images(self, *args, **kwargs):
        return len(self.images)

    def readable_datetime(self, *args, **kwargs):
        return self.created.strftime("%B %d, %Y at %H:%M")


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, related_name="comment_author")
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author_social = models.ForeignKey(
        SocialUser, on_delete=models.CASCADE, null=False, related_name="comment_author_social"
    )

    def __str__(self):
        return f"{self.body}"

    def get_absolute_url(self):
        return reverse("post-details", kwargs={"slug": self.post.slug})

    # def save(self, *args, **kwargs):
    #     x = self.author
    #     self.author_social = SocialUser.objects.get(user=x)
