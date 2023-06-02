import uuid

from django.db import models


class Movie(models.Model):
    title = models.CharField(help_text="enter title", max_length=200)
    country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField('Genre', help_text="select genre")
    duration = models.DurationField(help_text="enter duration")
    poster = models.ImageField(help_text="put the poster here")
    description = models.TextField(help_text="enter description")
    rating = models.FloatField(help_text="enter rating")

    def __str__(self):
        return self.title

    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre.all()[:3]])

    display_genre.short_description = 'Genre'


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="enter genre")

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=200, help_text="enter country")

    def __str__(self):
        return self.name


class MovieSession(models.Model):
    lounge_number = models.IntegerField(null=True)
    movie = models.ForeignKey('Movie', on_delete=models.SET_NULL, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="id for session")
    date = models.DateField(null=True)
    time_begin = models.TimeField(null=True)
    time_end = models.TimeField(null=True)

    def __str__(self):
        return '%s (%s)' % (self.id, self.movie.title)
