from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.dispatch import receiver

# Create your models here.


class SocialUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, default="No bio has been added yet...")
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    join_date = models.DateTimeField(auto_now=True)
    following = models.ManyToManyField(
        User, blank=True, related_name="following")
    friends = models.ManyToManyField(
        User, blank=True, related_name="friends")
    followers = models.ManyToManyField(
        User, blank=True, related_name="followers")

    def __str__(self):
        return f"{self.user.username}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        SocialUser.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.socialuser.save()


class Tag(models.Model):
    caption = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.caption}"


class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=False, unique=True)
    content = models.TextField()
    tags = models.ManyToManyField(
        Tag, blank=True, related_name="posts")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, related_name="posts")
    likes = models.ManyToManyField(User, related_name="likes", blank=True)


    class Meta: 
        ordering = ['-created']

    def __str__(self):
        return f"{self.created} - {self.title}"

    def number_of_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    text = models.TextField(max_length=400)
    comment_author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, related_name="comment_author")
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, blank=True, related_name="comments")
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'Comment by {self.comment_author.username}'
