from django.db import models


class AnimeWatchingEnum(models.TextChoices):
    WATCHING = "watching", "Watching"
    COMPLETED = "completed", "Completed"
    ON_HOLD = "on_hold", "On Hold"
    DROPPED = "dropped", "Dropped"
    PLANNED = "planned", "Planned"


class AnimeStatusEnum(models.TextChoices):
    CURRENT = "current", "Currently Airing"
    FINISHED = "finished", "Finished"
    TBA = "tba", "To Be Announced"


class AnimeShowTypeEnum(models.TextChoices):
    TV = "tv", "TV Show"
    MOVIE = "movie", "Movie"
    OVA = "ova", "OVA"


class AnimeAgeRatingEnum(models.TextChoices):
    G = "G", "General Audience"
    PG = "PG", "Parental Guidance"
    R = "R", "Restricted"
