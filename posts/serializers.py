"""Serializers of the 'posts' app."""
from rest_framework import serializers


from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    """
    'ModelSerializer' for 'models.Post' objects.
    """

    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        """Adds meta-information."""

        fields = ('id', 'text', 'author', 'image', 'pub_date')
        model = Post



class CommentSerializer(serializers.ModelSerializer):
    """
    'ModelSerializer' for 'models.Comment' objects.
    """

    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        """Adds meta-information."""

        fields = ('id', 'text', 'author', 'post', 'created')
        read_only_fields = ('author', 'post')
        model = Comment
