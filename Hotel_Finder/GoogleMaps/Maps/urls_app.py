from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('places', views.places, name="Places"),
    path('pickup', views.pickup, name="Pickup"),
]