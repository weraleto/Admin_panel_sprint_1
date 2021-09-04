from django.contrib import admin
from .models import *


class FilmworkGenreAdmin(admin.TabularInline):
    model = FilmworkGenre


class PersonFilmworkAdmin(admin.TabularInline):
    model = PersonFilmwork


@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'creation_date', 'rating')
    inlines = [
        FilmworkGenreAdmin, PersonFilmworkAdmin
    ]
    fields = (
        'title', 'type', 'description', 'creation_date', 'certificate',
        'file_path', 'rating'
    )


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_date')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass
