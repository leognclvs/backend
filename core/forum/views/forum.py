from rest_framework import permissions
from rest_framework.filters import OrderingFilter, SearchFilter

from core.common.permissions import IsOwnerOrReadOnly
from core.common.views import BaseModelViewSet
from core.forum.models import ForumCategory, ForumThread, ForumPost
from core.forum.serializers import (
    ForumCategorySerializer,
    ForumThreadReadSerializer,
    ForumThreadWriteSerializer,
    ForumPostSerializer,
)


class ForumCategoryViewSet(BaseModelViewSet):
    queryset = ForumCategory.objects.filter(is_active=True)
    read_serializer_class = ForumCategorySerializer
    write_serializer_class = ForumCategorySerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ["get", "head", "options"]


class ForumThreadViewSet(BaseModelViewSet):
    queryset = ForumThread.objects.select_related("category", "owner").prefetch_related(
        "posts",
        "posts__owner",
        "posts__replies",
        "posts__replies__owner",
    ).filter(is_public=True)
    read_serializer_class = ForumThreadReadSerializer
    write_serializer_class = ForumThreadWriteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    lookup_field = "slug"
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title", "content", "category__name"]
    ordering_fields = ["created_at", "updated_at", "last_activity_at", "title"]
    ordering = ["-is_pinned", "-last_activity_at", "-updated_at"]


class ForumPostViewSet(BaseModelViewSet):
    queryset = ForumPost.objects.select_related("thread", "owner", "parent").prefetch_related("replies").all()
    read_serializer_class = ForumPostSerializer
    write_serializer_class = ForumPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [OrderingFilter]
    ordering_fields = ["created_at", "updated_at"]
    ordering = ["created_at"]

    def get_queryset(self):
        queryset = super().get_queryset().filter(thread__is_public=True)
        thread_id = self.request.query_params.get("thread")
        if thread_id:
            queryset = queryset.filter(thread_id=thread_id)
        return queryset

