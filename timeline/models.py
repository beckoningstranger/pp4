from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.dispatch import receiver
from django.urls import reverse


class SocialUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(
        max_length=500, default="No bio has been added yet...")
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    join_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        SocialUser.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.socialuser.save()


class Post(models.Model):
    author = models.ForeignKey(
        SocialUser, on_delete=models.CASCADE, null=False, related_name="post_author")
    title = models.CharField(max_length=50, null=False)
    excerpt = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=False, unique=True)
    content = models.TextField(null=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.created} - {self.title}"

    def get_absolute_url(self):
        # Needed for posting something
        return reverse("post-details", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        # Auto-generate a slug for the post
        if not self.slug:
            self.slug = slugify(self.title)
        # Auto-generate an excerpt for the post
        if not self.excerpt:
            if len(self.content) < 30:
                self.excerpt == self.content
            else:
                self.excerpt = self.content[0:30] + "..."
        super(Post, self).save(*args, **kwargs)
