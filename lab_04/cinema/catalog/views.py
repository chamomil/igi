from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import generic

from .forms import RegisterForm, ReserveTicketForm, ConfirmTicketForm
from .models import Movie, Payment, MovieSession
from .services import get_random_dog, get_random_joke


class IndexView(generic.ListView):
    template_name = "catalog/index.html"
    context_object_name = "movies_list"

    def get_queryset(self):
        query = Movie.objects.get_queryset()
        search = self.request.GET.get("search")
        genre = self.request.GET.get("genre")

        if search:
            query = query.filter(title__icontains=search)

        if genre:
            query = query.filter(genre__name__icontains=genre)

        return query.order_by("-year_of_production")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search"] = self.request.GET.get("search")
        context["genre"] = self.request.GET.get("genre")
        context["random_dog"] = get_random_dog()
        context["random_joke"] = get_random_joke()
        return context


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Movie
    template_name = "catalog/detail.html"
    login_url = "/login/"


def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/catalog")
    else:
        form = RegisterForm()

    return render(request, "registration/sign_up.html", {"form": form})


class ReserveTicket(generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        form = ReserveTicketForm(self.request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            session = get_object_or_404(MovieSession, pk=form_data.get("session_id"))

            new_payment = Payment(userId=self.request.user.id, movie_session=session)
            new_payment.save()
            return f"/catalog/confirm_pay/{new_payment.id}"


class ConfirmReservation(generic.DetailView):
    model = Payment
    template_name = "catalog/confirm_pay.html"


class ConfirmationHandler(generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        form = ConfirmTicketForm(self.request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            payment = get_object_or_404(Payment, pk=form_data.get("payment_id"))
            if "cancel" in self.request.POST:
                payment.status = "d"
            else:
                payment.status = "s"
            payment.save()
        return reverse("catalog:index")


class MyTickets(LoginRequiredMixin, generic.ListView):
    template_name = "catalog/my_tickets.html"
    context_object_name = "tickets_list"
    login_url = "/login/"

    def get_queryset(self):
        return Payment.objects.filter(
            userId__exact=self.request.user.id, status__exact="s"
        ).all()


class DeleteTicketView(generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            payment = Payment.objects.get(pk=pk)
            payment.delete()

        return reverse("catalog:my_tickets")
