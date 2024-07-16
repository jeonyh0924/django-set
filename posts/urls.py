from django.urls import path

from posts.views import PostViewSet

app_name = "posts"

urlpatterns = [
    path('users/<str:user_uuid>/posts', PostViewSet.as_view({'get': 'list', 'post': 'create'})),
]
