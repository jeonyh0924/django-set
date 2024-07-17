from django.urls import path, include
from rest_framework import routers
from rest_framework_nested import routers as nested_routers


from posts.views import PostViewSet, UserViewSet

app_name = "posts"


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet)

# post에 대한 중첩된 라우터 생성
posts_router = nested_routers.NestedSimpleRouter(router, r'users', lookup='user')
posts_router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(posts_router.urls)),
]
