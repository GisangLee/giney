from django.conf import settings
from django.db import models
from django.urls import reverse


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Post(TimeStampModel):
    class Meta:
        ordering = ["-id"]

    objects = models.Manager()

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="my_post_set", on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    photo = models.ImageField(
        upload_to="boards/post/%Y/%m/%d", blank=True, null=True)
    caption = models.TextField()
    like_user_set = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name="like_user_set")

    def __str__(self):
        return f'{self.title} + {self.caption}'


class Comment(TimeStampModel):
    class Meta:
        ordering = ["-id"]

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()
