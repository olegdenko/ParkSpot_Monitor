from django import forms
from users.models import Plates, BlacklistedVehicle, ParkingRate, Settings
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
class UserAdminCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'is_staff', 'is_active')

class UserAdminChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('username', 'email', 'is_staff', 'is_active')

class PlatesForm(forms.ModelForm):
    class Meta:
        model = Plates
        fields = ['plate', 'user']


class BlacklistedVehicleForm(forms.ModelForm):
    class Meta:
        model = BlacklistedVehicle
        fields = ['plate', 'user', 'reason']


class ParkingRateForm(forms.ModelForm):
    class Meta:
        model = ParkingRate
        fields = ['rate_name', 'price_per_hour']


class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = ['key', 'value']
