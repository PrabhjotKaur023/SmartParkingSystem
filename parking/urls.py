from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path(
        'vehicle-entry/',
        views.vehicle_entry,
        name='vehicle_entry'
    ),
]