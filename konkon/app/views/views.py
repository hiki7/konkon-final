from rest_framework import permissions, viewsets
from ..models import Anime, UserAnime
from ..serializers import AnimeSerializer, UserAnimeSerializer
from django_filters.rest_framework import DjangoFilterBackend
