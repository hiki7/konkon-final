from django.contrib import admin
from .models import Anime, Category, Genre, UserAnime


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "synopsis",
        "status",
        "start_date",
        "end_date",
        "episode_count",
        "show_type",
        "age_rating",
    )
    search_fields = ("title", "status", "show_type", "age_rating")
    list_filter = ("status", "episode_count", "show_type", "age_rating")
    ordering = ("title", "episode_count")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    search_fields = ("title",)
    list_filter = ("title",)
    ordering = ("title",)
