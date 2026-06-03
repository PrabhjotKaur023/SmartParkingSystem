from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('vehicle-entry/', views.vehicle_entry, name='vehicle_entry'),
    path('vehicle-exit/', views.vehicle_exit, name='vehicle_exit'),
    path('search-vehicle/', views.search_vehicle, name='search_vehicle'),
    path('api/vehicles/',views.vehicle_api, name='vehicle_api'),
]