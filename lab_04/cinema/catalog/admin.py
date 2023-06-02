from django.contrib import admin
from .models import Movie, Country, Genre, MovieSession


class GenreAdmin(admin.ModelAdmin):
    pass


class CountryAdmin(admin.ModelAdmin):
    pass


class MovieSessionAdmin(admin.TabularInline):
    model = MovieSession
    extra = 0


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'display_genre')
    inlines = [MovieSessionAdmin]


admin.site.register(Movie, MovieAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Genre, GenreAdmin)
# admin.site.register(MovieSession, MovieSessionAdmin)
