from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    duration = models.DurationField()
    genre = models.ManyToManyField('Genre', help_text="choose genre")
    budget = models.CharField(max_length=200)
    poster = models.ImageField(upload_to='catalog/static/catalog/posters/')
    description = models.TextField()
    rating = models.FloatField()
    year_of_production = models.CharField(max_length=4)

    def __str__(self):
        return self.title


class MovieSession(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    date = models.DateField()
    time_begin = models.TimeField()
    lounge = models.ForeignKey('Lounge', on_delete=models.CASCADE)
    bought_tickets = 0
    price_per_ticket = models.FloatField(default=10.0)

    def __str__(self):
        return self.movie.title


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Lounge(models.Model):
    number = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return self.number.__str__()
