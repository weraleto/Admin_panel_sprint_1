from django.contrib import admin
from .models import *


class FilmworkGenreAdmin(admin.TabularInline):
    model = FilmworkGenre


class PersonFilmworkAdmin(admin.TabularInline):
    model = PersonFilmwork


@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'creation_date', 'rating')
    search_fields = ('title',)
    list_filter = ('type',)
    inlines = [
        FilmworkGenreAdmin, PersonFilmworkAdmin
    ]
    readonly_fields = ('created_at', 'updated_at')
    fields = (
        'title', 'type', 'description', 'creation_date', 'certificate',
        'file_path', 'rating', 'created_at', 'updated_at'
    )


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_date')
    search_fields = ('full_name',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ('name',)
