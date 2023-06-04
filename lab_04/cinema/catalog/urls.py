from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = "catalog"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("sign-up/", views.sign_up, name="sign_up"),
    path("reserve-ticket", views.ReserveTicket.as_view(), name="reserve_ticket"),
    path(
        "confirm_pay/<int:pk>", views.ConfirmReservation.as_view(), name="confirm_pay"
    ),
    path(
        "confirm_handler", views.ConfirmationHandler.as_view(), name="confirm_handler"
    ),
    path("my_tickets", views.MyTickets.as_view(), name="my_tickets"),
    path(
        "my_tickets/<int:pk>/delete",
        views.DeleteTicketView.as_view(),
        name="my_tickets_delete",
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
