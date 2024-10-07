# Generated by Django 5.1.1 on 2024-10-07 17:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "changed_at",
                    models.DateTimeField(auto_now=True, verbose_name="Changed at"),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="Название категории"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Описание категории"
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "changed_at",
                    models.DateTimeField(auto_now=True, verbose_name="Changed at"),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="Название жанра"
                    ),
                ),
            ],
            options={
                "verbose_name": "Жанр",
                "verbose_name_plural": "Жанры",
            },
        ),
        migrations.CreateModel(
            name="Anime",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "changed_at",
                    models.DateTimeField(auto_now=True, verbose_name="Changed at"),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="Название аниме"
                    ),
                ),
                (
                    "synopsis",
                    models.TextField(
                        blank=True, null=True, verbose_name="Описание аниме"
                    ),
                ),
                ("poster_image_url", models.URLField(verbose_name="Ссылка на постер")),
                (
                    "start_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Дата начала показа аниме"
                    ),
                ),
                (
                    "end_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Дата окончания аниме"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("current", "Currently Airing"),
                            ("finished", "Finished"),
                            ("tba", "To Be Announced"),
                        ],
                        max_length=50,
                        null=True,
                        verbose_name="Статус аниме",
                    ),
                ),
                (
                    "episode_count",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Количество эпизодов"
                    ),
                ),
                (
                    "show_type",
                    models.CharField(
                        blank=True,
                        choices=[("tv", "TV Show"), ("movie", "Movie"), ("ova", "OVA")],
                        max_length=50,
                        null=True,
                        verbose_name="Тип аниме",
                    ),
                ),
                (
                    "age_rating",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("G", "General Audience"),
                            ("PG", "Parental Guidance"),
                            ("R", "Restricted"),
                        ],
                        max_length=50,
                        null=True,
                        verbose_name="Возрастной рейтинг",
                    ),
                ),
                (
                    "categories",
                    models.ManyToManyField(
                        blank=True,
                        related_name="animes",
                        to="app.category",
                        verbose_name="Категория аниме",
                    ),
                ),
            ],
            options={
                "verbose_name": "Аниме",
                "verbose_name_plural": "Аниме",
            },
        ),
        migrations.CreateModel(
            name="UserAnime",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "changed_at",
                    models.DateTimeField(auto_now=True, verbose_name="Changed at"),
                ),
                (
                    "watch_status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("watching", "Watching"),
                            ("completed", "Completed"),
                            ("on_hold", "On Hold"),
                            ("dropped", "Dropped"),
                            ("planned", "Planned"),
                        ],
                        max_length=50,
                        null=True,
                        verbose_name="Статус просмотра",
                    ),
                ),
                (
                    "anime",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.anime",
                        verbose_name="Аниме",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "unique_together": {("user", "anime")},
            },
        ),
        migrations.AddField(
            model_name="anime",
            name="users",
            field=models.ManyToManyField(
                through="app.UserAnime",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователи",
            ),
        ),
    ]
