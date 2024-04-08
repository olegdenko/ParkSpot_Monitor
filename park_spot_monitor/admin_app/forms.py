from django import forms
from .models import RegisteredNumberPlate, ParkingRate, BlacklistedVehicle

class NumberPlateForm(forms.ModelForm):
    class Meta:
        model = RegisteredNumberPlate
        fields = ['plate_number']

class ParkingRateForm(forms.ModelForm):
    class Meta:
        model = ParkingRate
        fields = ['name', 'rate']

class BlacklistForm(forms.ModelForm):
    class Meta:
        model = BlacklistedVehicle
        fields = ['plate_number']
