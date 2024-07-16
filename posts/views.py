from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import mixins, viewsets

from posts.models import Post, User
from posts.serializer import PostSerializer, UserSerializer


@extend_schema_view(
    create=extend_schema(summary='Post 생성', tags=['Post']),
    list=extend_schema(summary='Post 목록 조회', tags=['Post']),
    retrieve=extend_schema(summary='Post 상세 조회', tags=['Post']),
    update=extend_schema(summary='Post 수정', tags=['Post']),
)
class PostViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'uuid'


class UserViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
