from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from .models import Movie
from .forms import RegisterForm


class IndexView(generic.ListView):
    template_name = "catalog/index.html"
    context_object_name = "movies_list"

    def get_queryset(self):

        return Movie.objects.order_by("-year_of_production")[:5]


class DetailView(generic.DetailView):
    model = Movie
    template_name = "catalog/detail.html"


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/catalog')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {'form': form})
