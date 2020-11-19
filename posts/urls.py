"""View functions of the Posts app."""
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views


from .views import PostViewSet, CommentViewSet


router = DefaultRouter()

router.register('api/v1/posts', PostViewSet)
router.register(r'api/v1/posts/(?P<post_id>.+)/comments', CommentViewSet,
                basename='comments')

urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]
