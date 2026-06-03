from django import forms


class VehicleEntryForm(forms.Form):
    vehicle_number = forms.CharField(max_length=20)
    owner_name = forms.CharField(max_length=100)

    vehicle_type = forms.ChoiceField(
        choices=[
            ('Car', 'Car'),
            ('Bike', 'Bike')
        ]
    )


class VehicleExitForm(forms.Form):
    vehicle_number = forms.CharField(
        max_length=20,
        label="Vehicle Number"
    )