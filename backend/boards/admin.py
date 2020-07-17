from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "caption", "photo", ]
    list_display_links = ["title", "caption"]

    def photo_tag(self, post):
        return mark_safe(f"<img src={post.photo.url} style='width:100px;'/>")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
