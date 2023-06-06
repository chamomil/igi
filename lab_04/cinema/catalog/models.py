from django.db import models
from django.utils import timezone


class Movie(models.Model):
    title = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    duration = models.DurationField()
    genre = models.ManyToManyField("Genre", help_text="choose genre")
    budget = models.CharField(max_length=200)
    poster = models.ImageField(upload_to="static/catalog/posters/")
    description = models.TextField()
    rating = models.FloatField()
    year_of_production = models.CharField(max_length=4)

    def __str__(self):
        return self.title


class MovieSession(models.Model):
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)
    date = models.DateField()
    time_begin = models.TimeField()
    lounge = models.ForeignKey("Lounge", on_delete=models.CASCADE)
    price_per_ticket = models.FloatField(default=10.0)

    def is_valid(self):
        return (
            self.date >= timezone.now().date()
            and self.payment_set.count() < self.lounge.capacity
        )

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


class Payment(models.Model):
    userId = models.IntegerField()
    movie_session = models.ForeignKey("MovieSession", on_delete=models.CASCADE)
    PAY_STATUS = (
        ("p", "Pending"),
        ("s", "Success"),
        ("d", "Declined"),
    )

    status = models.CharField(
        max_length=1,
        choices=PAY_STATUS,
        blank=True,
        default="p",
    )

    def __str__(self):
        return self.status
