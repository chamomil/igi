from django.contrib import admin

from .models import Movie, Genre, Lounge, MovieSession

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Lounge)
admin.site.register(MovieSession)
