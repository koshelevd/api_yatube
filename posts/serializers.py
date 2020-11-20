"""Serializers of the 'posts' app."""
from rest_framework import serializers


from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    """
    'ModelSerializer' for 'models.Post' objects.
    """

    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)

    class Meta:
        """Adds meta-information."""

        fields = '__all__'
        model = Post



class CommentSerializer(serializers.ModelSerializer):
    """
    'ModelSerializer' for 'models.Comment' objects.
    """

    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)

    class Meta:
        """Adds meta-information."""

        fields = '__all__'
        read_only_fields = ('author', 'post')
        model = Comment
