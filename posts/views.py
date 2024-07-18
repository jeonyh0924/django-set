from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import mixins, viewsets

from posts.models import Post, User
from posts.serializer import PostSerializer, UserSerializer


@extend_schema_view(
    list=extend_schema(summary='Child 목록 조회', tags=['Child']),
    retrieve=extend_schema(summary='Child 상세 조회', tags=['Child']),
    update=extend_schema(summary='Child 수정', tags=['Child']),
    partial_update=extend_schema(summary='Child 부분 수정', tags=['Child'])
)
class IndependentChildViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@extend_schema_view(
    create=extend_schema(summary='#NestedURL Child 생성', tags=['Child']),
)
class ChildViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'uuid'


@extend_schema_view(
    create=extend_schema(summary='Parent 생성', tags=['Parent']),
    list=extend_schema(summary='Parent 목록 조회', tags=['Parent']),
    retrieve=extend_schema(summary='Parent 상세 조회', tags=['Parent']),
    update=extend_schema(summary='Parent 수정', tags=['Parent']),
    partial_update=extend_schema(summary='Parent 부분 수정', tags=['Parent'])
)
# parent
class ParentViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
