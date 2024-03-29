from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api.views import (
    PostViewSet, GroupViewSet, FollowListCreateViewSet, CommentViewSet
)

router_v1 = DefaultRouter()

router_v1.register('posts', PostViewSet, basename='post')
router_v1.register('groups', GroupViewSet, basename='group')
router_v1.register('follow', FollowListCreateViewSet, basename='follow')
router_v1.register(
    r'posts/(?P<id>\d+)/comments', CommentViewSet, basename='comment'
)


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
