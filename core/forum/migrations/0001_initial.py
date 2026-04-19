import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


def seed_forum_categories(apps, schema_editor):
    ForumCategory = apps.get_model("forum", "ForumCategory")
    categories = [
        {
            "name": "Discussao Geral",
            "slug": "discussao-geral",
            "description": "Conversas gerais sobre o ecossistema e criacao de idiomas.",
            "color": "#3b82f6",
            "sort_order": 1,
        },
        {
            "name": "Fonologia e Escrita",
            "slug": "fonologia-e-escrita",
            "description": "Inventarios sonoros, IPA e sistemas de escrita.",
            "color": "#10b981",
            "sort_order": 2,
        },
        {
            "name": "Lexico e Gramatica",
            "slug": "lexico-e-gramatica",
            "description": "Lexemas, morfologia, sintaxe e organizacao gramatical.",
            "color": "#f59e0b",
            "sort_order": 3,
        },
    ]

    for category in categories:
        ForumCategory.objects.update_or_create(slug=category["slug"], defaults=category)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ForumCategory",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=120, unique=True)),
                ("slug", models.SlugField(max_length=140, unique=True)),
                ("description", models.TextField(blank=True)),
                ("color", models.CharField(blank=True, max_length=20)),
                ("sort_order", models.IntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={"ordering": ["sort_order", "name"]},
        ),
        migrations.CreateModel(
            name="ForumThread",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=180)),
                ("slug", models.SlugField(max_length=220, unique=True)),
                ("content", models.TextField()),
                ("is_pinned", models.BooleanField(default=False)),
                ("is_locked", models.BooleanField(default=False)),
                ("is_public", models.BooleanField(default=True)),
                ("last_activity_at", models.DateTimeField(blank=True, null=True)),
                ("category", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="threads", to="forum.forumcategory")),
                ("owner", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="forum_threads", to=settings.AUTH_USER_MODEL)),
            ],
            options={"ordering": ["-is_pinned", "-last_activity_at", "-updated_at"]},
        ),
        migrations.CreateModel(
            name="ForumPost",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("content", models.TextField()),
                ("is_solution", models.BooleanField(default=False)),
                ("owner", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="forum_posts", to=settings.AUTH_USER_MODEL)),
                ("parent", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name="replies", to="forum.forumpost")),
                ("thread", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="posts", to="forum.forumthread")),
            ],
            options={"ordering": ["created_at"]},
        ),
        migrations.RunPython(seed_forum_categories, migrations.RunPython.noop),
    ]
