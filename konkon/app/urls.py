from rest_framework import routers
from django.urls import include, path

from .views import GenreViewSet

router = routers.DefaultRouter()

router.register(r"genres", GenreViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
