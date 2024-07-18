# posts.urls.py
from django.urls import path, include
from rest_framework import routers
from rest_framework_nested import routers as nested_routers

from posts.views import ChildViewSet, ParentViewSet, IndependentChildViewSet

app_name = "posts"

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'parents', ParentViewSet)  # parent - User View Set
router.register(r'children', IndependentChildViewSet)  # child - Post View Set

# post에 대한 중첩된 라우터 생성
parent_router = nested_routers.NestedSimpleRouter(router, r'parents', lookup='parent')
parent_router.register(r'children', ChildViewSet)  # Post View Set

urlpatterns = [
    path('', include(router.urls)),
    path('', include(parent_router.urls)),
]
