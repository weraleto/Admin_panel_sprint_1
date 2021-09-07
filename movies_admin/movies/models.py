from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid


class TimeStampedMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Genre(TimeStampedMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('genre')
        verbose_name_plural = _('genres')
        db_table = "genre"


class FilmworkType(models.TextChoices):
    MOVIE = 'movie', _('movie')
    TV_SHOW = 'tv_show', _('TV Show')


class Filmwork(TimeStampedMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True)
    creation_date = models.DateField(_('creation date'), blank=True)
    certificate = models.TextField(_('certificate'), blank=True)
    file_path = models.FileField(_('file'), upload_to='film_works/', blank=True)
    rating = models.FloatField(_('rating'), validators=[MinValueValidator(0), MaxValueValidator(10)], blank=True)
    type = models.CharField(_('type'), max_length=10, choices=FilmworkType.choices)

    class Meta:
        verbose_name = _('filmwork')
        verbose_name_plural = _('filmworks')
        db_table = "film_work"


class PersonRoles(models.TextChoices):
    ACTOR = 'actor', _('actor')
    WRITER = 'writer', _('writer')
    DIRECTOR = 'director', _('director')


class Person(TimeStampedMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(_('full name'), max_length=255)
    birth_date = models.DateField(_('birth date'), blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('person')
        verbose_name_plural = _('persons')
        db_table = "person"


class FilmworkGenre(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    film_work = models.ForeignKey('Filmwork', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "genre_film_work"
        unique_together = (('film_work_id', 'genre_id'),)


class PersonFilmwork(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    film_work = models.ForeignKey('Filmwork', on_delete=models.CASCADE)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    role = models.CharField(_('role'), max_length=10, choices=PersonRoles.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "person_film_work"
        unique_together = (('film_work_id', 'person_id', 'role'),)
