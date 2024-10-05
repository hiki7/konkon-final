from django.db import models
from .abstract import TimestampModel
from django.utils.translation import gettext_lazy as _


class Category(TimestampModel):
    """Категория аниме/манги"""

    id: int
    title: str = models.CharField(
        verbose_name="Название категории",
        max_length=255,
        null=False,
        blank=False,
        unique=True,
    )
    description: str = models.TextField(
        verbose_name="Описание категории", null=True, blank=True
    )

    class Meta:
        verbose_name_plural = _("Категории")
        verbose_name = _("Категория")

    def __str__(self):
        return self.title


class Genre(TimestampModel):
    """Жанр аниме/манги"""

    id: int
    name: str = models.CharField(
        verbose_name="Название жанра",
        max_length=255,
        null=False,
        blank=False,
        unique=True,
    )

    class Meta:
        verbose_name_plural = _("Жанры")
        verbose_name = _("Жанр")

    def __str__(self):
        return self.name
