from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from .models import Movie, Payment, MovieSession
from .forms import RegisterForm, ReserveTicketForm, ConfirmTicketForm


class IndexView(generic.ListView):
    template_name = "catalog/index.html"
    context_object_name = "movies_list"

    def get_queryset(self):
        return Movie.objects.order_by("-year_of_production")[:5]


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Movie
    template_name = "catalog/detail.html"
    login_url = "/login/"

    def post(self, session):
        return Payment(userId=self.request.user.id, movie_session=session).id


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


class ReserveTicket(generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        form = ReserveTicketForm(self.request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            session = get_object_or_404(MovieSession, pk=form_data.get('session_id'))

            new_payment = Payment(userId=self.request.user.id, movie_session=session)
            new_payment.save()
            return f'/catalog/confirm_pay/{new_payment.id}'


class ConfirmReservation(generic.DetailView):
    model = Payment
    template_name = 'catalog/confirm_pay.html'


class ConfirmationHandler(generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        form = ConfirmTicketForm(self.request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            payment = get_object_or_404(Payment, pk=form_data.get('payment_id'))
            if "cancel" in self.request.POST:
                payment.status = 'd'
            else:
                payment.status = 's'
            payment.save()
        return reverse("catalog:index")


class MyTickets(generic.ListView):
    template_name = 'catalog/my_tickets.html'
    context_object_name = "tickets_list"

    def get_queryset(self):
        return Payment.objects.filter(userId__exact=self.request.user.id, status__exact='s').all()
