from rest_framework import serializers
from .models import Anime, Category, Genre, UserAnime


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["title", "description"]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["name"]


class AnimeSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    genre = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Anime
        fields = [
            "title",
            "synopsis",
            "poster_image_url",
            "start_date",
            "end_date",
            "status",
            "episode_count",
            "show_type",
            "age_rating",
            "categories",
            "genre",
        ]


class UserAnimeSerializer(serializers.ModelSerializer):
    anime = AnimeSerializer(read_only=True)

    class Meta:
        model = UserAnime
        fields = ["anime", "watch_status"]
