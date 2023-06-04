from django.contrib import admin

from .models import Movie, Genre, Lounge, MovieSession, Payment


class MovieSessionInLine(admin.TabularInline):
    model = MovieSession
    extra = 0


class MovieAdmin(admin.ModelAdmin):
    fields = ["title", "year_of_production", "genre", "country",
              "duration", "budget", "rating", "description",
              "poster"]
    inlines = [MovieSessionInLine]
    list_display = ["title", "year_of_production"]
    list_filter = ["year_of_production"]
    search_fields = ["title"]


admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre)
admin.site.register(Lounge)
admin.site.register(Payment)
