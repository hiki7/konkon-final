from rest_framework import serializers
from .models import Anime, Category, Genre, UserAnime


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["title", "description"]
