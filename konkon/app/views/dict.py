from rest_framework import permissions, viewsets
from ..models import Genre, Category
from ..serializers import GenreSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend


class GenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows genres to be viewed or edited.
    """

    queryset = Genre.objects.all().order_by("-created_at")
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name"]
