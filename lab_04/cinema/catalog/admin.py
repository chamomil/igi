from django.contrib import admin
from django.utils import timezone

from .models import Movie, Genre, Lounge, MovieSession, Payment


class MovieSessionInLine(admin.TabularInline):
    model = MovieSession
    extra = 0


class MovieAdmin(admin.ModelAdmin):
    fields = [
        "title",
        "year_of_production",
        "genre",
        "country",
        "duration",
        "budget",
        "rating",
        "description",
        "poster",
    ]
    inlines = [MovieSessionInLine]
    list_display = ["title", "year_of_production"]
    list_filter = ["year_of_production", "genre"]
    search_fields = ["title"]


class IncomeAdmin(admin.ModelAdmin):
    month = timezone.now().month
    monthly_payment = Payment.objects.filter(movie_session__date__month=month)


admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre)
admin.site.register(Lounge)
admin.site.register(Payment, IncomeAdmin)
