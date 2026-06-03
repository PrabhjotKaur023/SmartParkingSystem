from django.shortcuts import render
from .models import ParkingSlot


def dashboard(request):

    total_slots = ParkingSlot.objects.count()

    available_slots = ParkingSlot.objects.filter(
        is_occupied=False
    ).count()

    occupied_slots = ParkingSlot.objects.filter(
        is_occupied=True
    ).count()

    context = {
        'total_slots': total_slots,
        'available_slots': available_slots,
        'occupied_slots': occupied_slots
    }

    return render(
        request,
        'parking/dashboard.html',
        context
    )