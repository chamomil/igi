from django.views import generic
from django.utils import timezone

from .models import Movie


class IndexView(generic.ListView):
    template_name = "catalog/index.html"
    context_object_name = "movies_list"

    def get_queryset(self):

        return Movie.objects.order_by("-year_of_production")[:5]


class DetailView(generic.DetailView):
    model = Movie
    template_name = "catalog/detail.html"
