from rest_framework import serializers

from apps.accounts.serializers import UserSerializer
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('title', 'slug', 'text', 'author', 'created_at', 'updated_at')
