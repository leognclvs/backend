from django.utils import timezone
from django.utils.text import slugify
from rest_framework import serializers

from core.forum.models import ForumCategory, ForumThread, ForumPost


def serialize_user(user):
    return {
        "id": str(user.id),
        "username": user.username,
        "display_name": user.display_name or user.username,
        "avatar_url": getattr(getattr(user, "profile", None), "avatar", ""),
    }


class ForumCategorySerializer(serializers.ModelSerializer):
    threads_count = serializers.SerializerMethodField()

    class Meta:
        model = ForumCategory
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "color",
            "sort_order",
            "threads_count",
        ]
        read_only_fields = fields

    def get_threads_count(self, obj):
        return obj.threads.filter(is_public=True).count()


class ForumPostSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    replies = serializers.SerializerMethodField()
    parent_id = serializers.UUIDField(required=False, allow_null=True, write_only=True)

    class Meta:
        model = ForumPost
        fields = [
            "id",
            "thread",
            "parent",
            "parent_id",
            "content",
            "is_solution",
            "user",
            "created_at",
            "updated_at",
            "replies",
        ]
        read_only_fields = ["id", "parent", "is_solution", "user", "created_at", "updated_at", "replies"]

    def get_user(self, obj):
        return serialize_user(obj.owner)

    def get_replies(self, obj):
        if obj.parent_id is not None:
            return []
        reply_queryset = obj.replies.select_related("owner").order_by("created_at")
        return ForumPostSerializer(reply_queryset, many=True, context=self.context).data

    def validate(self, attrs):
        thread = attrs["thread"]
        parent_id = attrs.pop("parent_id", None)

        if thread.is_locked:
            raise serializers.ValidationError("Este topico esta bloqueado para novas respostas.")

        if parent_id:
            try:
                parent = thread.posts.get(pk=parent_id)
            except ForumPost.DoesNotExist as exc:
                raise serializers.ValidationError("Resposta pai invalida para este topico.") from exc

            if parent.parent_id is not None:
                raise serializers.ValidationError("Respostas em segundo nivel nao sao permitidas.")

            attrs["parent"] = parent

        return attrs

    def create(self, validated_data):
        request = self.context["request"]
        post = ForumPost.objects.create(owner=request.user, **validated_data)
        thread = post.thread
        thread.last_activity_at = timezone.now()
        thread.save(update_fields=["last_activity_at", "updated_at"])
        return post


class ForumThreadReadSerializer(serializers.ModelSerializer):
    category = ForumCategorySerializer(read_only=True)
    user = serializers.SerializerMethodField()
    posts_count = serializers.SerializerMethodField()
    replies_count = serializers.SerializerMethodField()
    last_reply_at = serializers.SerializerMethodField()
    posts = serializers.SerializerMethodField()

    class Meta:
        model = ForumThread
        fields = [
            "id",
            "category",
            "user",
            "title",
            "slug",
            "content",
            "is_pinned",
            "is_locked",
            "is_public",
            "posts_count",
            "replies_count",
            "last_reply_at",
            "last_activity_at",
            "created_at",
            "updated_at",
            "posts",
        ]
        read_only_fields = fields

    def get_user(self, obj):
        return serialize_user(obj.owner)

    def get_posts_count(self, obj):
        return obj.posts.filter(parent__isnull=True).count()

    def get_replies_count(self, obj):
        return obj.posts.filter(parent__isnull=False).count()

    def get_last_reply_at(self, obj):
        latest_post = obj.posts.order_by("-created_at").first()
        return latest_post.created_at if latest_post else None

    def get_posts(self, obj):
        request = self.context.get("request")
        include_posts = bool(request and request.parser_context and request.parser_context.get("kwargs", {}).get("slug"))
        if not include_posts:
            return []

        queryset = obj.posts.filter(parent__isnull=True).select_related("owner").prefetch_related("replies__owner")
        return ForumPostSerializer(queryset, many=True, context=self.context).data


class ForumThreadWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumThread
        fields = [
            "id",
            "category",
            "title",
            "content",
        ]
        read_only_fields = ["id"]

    def create(self, validated_data):
        request = self.context["request"]
        title = validated_data["title"].strip()
        base_slug = slugify(title)[:180] or "topico"
        candidate = base_slug
        counter = 2
        while ForumThread.objects.filter(slug=candidate).exists():
            candidate = f"{base_slug}-{counter}"
            counter += 1

        thread = ForumThread.objects.create(
            owner=request.user,
            title=title,
            content=validated_data["content"].strip(),
            category=validated_data["category"],
            slug=candidate,
            last_activity_at=timezone.now(),
        )
        return thread
