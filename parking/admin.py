from django.contrib import admin
from .models import ParkingSlot, Vehicle, ParkingRecord

admin.site.register(ParkingSlot)
admin.site.register(Vehicle)
admin.site.register(ParkingRecord)