from django.urls import path

from rest_framework_nested.routers import NestedDefaultRouter
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'posts', PostViewSet)

posts_router = NestedDefaultRouter(router, r'posts', lookup='post')
posts_router.register(r'comments', CommentViewSet, basename='post-comments')
posts_router.register(r'images', PostImageViewSet, basename='post-images-comments')

urlpatterns = router.urls + posts_router.urls
