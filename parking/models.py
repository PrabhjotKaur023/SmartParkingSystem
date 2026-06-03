from django.db import models


class ParkingSlot(models.Model):
    slot_number = models.CharField(max_length=10)
    vehicle_type = models.CharField(max_length=20)
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return self.slot_number


class Vehicle(models.Model):
    vehicle_number = models.CharField(max_length=20)
    owner_name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=20)

    def __str__(self):
        return self.vehicle_number


class ParkingRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    slot = models.ForeignKey(ParkingSlot, on_delete=models.CASCADE)

    entry_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True, blank=True)

    amount = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
    )

    def __str__(self):
        return self.vehicle.vehicle_number