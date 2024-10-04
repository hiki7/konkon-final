from django.db import models
from django.db.models import CASCADE
from django.conf import settings

from .abstract import TimestampModel
from django.utils.translation import gettext_lazy as _

from .dict import Category
from ..enums import (
    AnimeStatusEnum,
    AnimeWatchingEnum,
    AnimeAgeRatingEnum,
    AnimeShowTypeEnum,
)


class Anime(TimestampModel):
    """Аниме"""

    id: int
    title: str = models.CharField(
        verbose_name="Название аниме",
        max_length=255,
        null=False,
        blank=False,
        unique=True,
    )
    synopsis: str = models.TextField(
        verbose_name="Описание аниме", null=True, blank=True
    )
    poster_image_url: str = models.URLField(verbose_name="Ссылка на постер")
    start_date: str = models.DateField(
        verbose_name="Дата начала показа аниме", null=True, blank=True
    )
    end_date: str = models.DateField(
        verbose_name="Дата окончания аниме", null=True, blank=True
    )
    status: str = models.CharField(
        verbose_name="Статус аниме",
        max_length=50,
        choices=AnimeStatusEnum.choices,
        null=True,
        blank=True,
    )
    episode_count: int = models.IntegerField(
        verbose_name="Количество эпизодов", null=True, blank=True
    )
    show_type: str = models.CharField(
        verbose_name="Тип аниме",
        max_length=50,
        choices=AnimeShowTypeEnum.choices,
        null=True,
        blank=True,
    )
    age_rating: str = models.CharField(
        verbose_name="Возрастной рейтинг",
        max_length=50,
        choices=AnimeAgeRatingEnum.choices,
        null=True,
        blank=True,
    )

    categories: Category = models.ManyToManyField(
        Category, verbose_name="Категория аниме", blank=True, related_name="animes"
    )
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, verbose_name="Пользователи", through="UserAnime"
    )

    class Meta:
        verbose_name_plural = _("Аниме")
        verbose_name = _("Аниме")

    def __str__(self):
        return self.title


class UserAnime(TimestampModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="Пользователь", on_delete=models.CASCADE
    )
    anime: Anime = models.ForeignKey(
        Anime, verbose_name="Аниме", on_delete=models.CASCADE
    )
    watch_status = models.CharField(
        verbose_name="Статус просмотра",
        max_length=50,
        choices=AnimeWatchingEnum.choices,
        null=True,
        blank=True,
    )

    class Meta:
        unique_together = ("user", "anime")

    def __str__(self):
        return f"{self.user} - {self.anime} - {self.watch_status}"
