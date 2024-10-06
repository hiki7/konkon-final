from rest_framework import serializers
from .models import Anime, Category, Genre


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["title", "description"]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["name"]
