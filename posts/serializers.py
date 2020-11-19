from rest_framework import serializers


from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        fields = ('id', 'text', 'author', 'image', 'pub_date')
        model = Post



class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        fields = ('id', 'text', 'author', 'post', 'created')
        read_only_fields = ('author', 'post')
        model = Comment
