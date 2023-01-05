from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    post_number = models.IntegerField(default=0)
    join_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Tag(models.Model):
    caption = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.caption}"


class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images")
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=False, unique=True)
    content = models.TextField()
    tags = models.ManyToManyField(
        Tag, blank=True, null=True, related_name="posts")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, related_name="posts")

    def __str__(self):
        return f"{self.date} - {self.title}"


class Comment(models.Model):
    text = models.TextField(max_length=400)
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name="comment_author")
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, null=True, related_name="comments")
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.name}'
