from django.shortcuts import render
from .forms import VehicleEntryForm, VehicleExitForm
from .models import ParkingSlot, Vehicle, ParkingRecord
from .forms import VehicleEntryForm
from django.utils import timezone
from datetime import timedelta


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


def vehicle_entry(request):

    if request.method == 'POST':

        form = VehicleEntryForm(request.POST)

        if form.is_valid():

            vehicle_number = form.cleaned_data['vehicle_number']
            owner_name = form.cleaned_data['owner_name']
            vehicle_type = form.cleaned_data['vehicle_type']

            slot = ParkingSlot.objects.filter(
                is_occupied=False,
                vehicle_type=vehicle_type
            ).first()

            if slot:

                vehicle = Vehicle.objects.create(
                    vehicle_number=vehicle_number,
                    owner_name=owner_name,
                    vehicle_type=vehicle_type
                )

                ParkingRecord.objects.create(
                    vehicle=vehicle,
                    slot=slot
                )

                slot.is_occupied = True
                slot.save()

                return render(
                    request,
                    'parking/success.html',
                    {'slot': slot}
                )

    else:
        form = VehicleEntryForm()

    return render(
        request,
        'parking/vehicle_entry.html',
        {'form': form}
    )
def vehicle_exit(request):

    if request.method == 'POST':

        form = VehicleExitForm(request.POST)

        if form.is_valid():

            vehicle_number = form.cleaned_data['vehicle_number']

            try:

                vehicle = Vehicle.objects.get(
                    vehicle_number=vehicle_number
                )

                record = ParkingRecord.objects.filter(
                    vehicle=vehicle,
                    exit_time__isnull=True
                ).first()

                if record:

                    record.exit_time = timezone.now()

                    duration = (
                        record.exit_time -
                        record.entry_time
                    )

                    hours = max(
                        1,
                        duration.total_seconds() / 3600
                    )

                    fee = round(hours * 20, 2)

                    record.amount = fee
                    record.save()

                    slot = record.slot
                    slot.is_occupied = False
                    slot.save()

                    return render(
                        request,
                        'parking/receipt.html',
                        {
                            'vehicle': vehicle,
                            'slot': slot,
                            'fee': fee,
                            'hours': round(hours, 2)
                        }
                    )

            except Vehicle.DoesNotExist:
                pass

    else:
        form = VehicleExitForm()

    return render(
        request,
        'parking/vehicle_exit.html',
        {'form': form}
    )