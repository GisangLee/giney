from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "id", "username", "avatar", "is_staff",
            "is_active", "is_superuser"
        ]


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ["id", "author", "photo", "title", "caption"]
