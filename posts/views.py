"""View classes of the 'posts' app."""
from django.shortcuts import get_object_or_404
from rest_framework import viewsets


from .models import Post
from .serializers import PostSerializer, CommentSerializer
from .permissions import ResourcePermission, IsAuthenticated


class PostViewSet(viewsets.ModelViewSet):
    """
    Viewset for 'models.Post' model.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (ResourcePermission, IsAuthenticated)

    def perform_create(self, serializer):
        """
        Override perform_create function.

        Save 'author' field.
        """
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    Viewset for 'models.Comment' model.
    """

    serializer_class = CommentSerializer
    permission_classes = (ResourcePermission, IsAuthenticated)

    def get_post(self):
        """
        Return 'models.Post' specified in URL by id.
        """
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def perform_create(self, serializer):
        """
        Override perform_create function.

        Save 'author' and 'post' fields.
        """
        serializer.save(author=self.request.user,
                        post=self.get_post())

    def get_queryset(self):
        """
        Override get_queryset.

        Return 'models.Comment' queryset for post_id in URL.
        """
        return self.get_post().comments.all()
