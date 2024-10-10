from rest_framework import routers
from django.urls import include, path

from .views import GenreViewSet, CategoryViewSet

router = routers.DefaultRouter()

router.register(r"genres", GenreViewSet)
router.register(r"categories", CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
