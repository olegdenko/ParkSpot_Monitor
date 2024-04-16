from django import forms
from users.models import Plates, BlacklistedVehicle, Settings
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import Form, FileField

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


class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = ['key', 'value']

class UploadImageForm(Form):
    image = FileField(label='Upload Image')
