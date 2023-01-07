from django.contrib import admin
from .models import Post, SocialUser, Comment, Tag

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("title",)
    }
    list_filter = ("tags", "likes", "comments", "created", "updated",)
    list_display = ("comments", "created", "updated",)
    search_fields = ["content", "author",]


admin.site.register(Post, PostAdmin)
admin.site.register(SocialUser)
admin.site.register(Comment)
admin.site.register(Tag)