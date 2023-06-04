from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = "catalog"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/ticket/", views.BuyTicket.as_view, name="ticket"),
    path("sign-up/", views.sign_up, name="sign_up")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
