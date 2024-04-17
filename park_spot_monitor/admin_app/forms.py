from django import forms
from users.models import Plates, BlacklistedVehicle, Settings
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import Form, FileField


class UserAdminCreationForm(UserCreationForm):
    """
    A form for creating new users by admins.

    It includes all required fields plus a checkbox for the admin status.
    """
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'is_staff', 'is_active')


class UserAdminChangeForm(UserChangeForm):
    """
    A form for updating users by admins.

    It includes all user fields and allows changing the admin status.
    """
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('username', 'email', 'is_staff', 'is_active')


class PlatesForm(forms.ModelForm):
    """
    A form for creating or updating Plates.

    It includes fields for plate and user.
    """
    class Meta:
        model = Plates
        fields = ['plate', 'user']


class BlacklistedVehicleForm(forms.ModelForm):
    """
    A form for creating or updating BlacklistedVehicle.

    It includes fields for plate, user, and reason.
    """
    class Meta:
        model = BlacklistedVehicle
        fields = ['plate', 'user', 'reason']




class SettingsForm(forms.ModelForm):
    """
    A form for creating or updating Settings.

    It includes fields for key and value.
    """
    class Meta:
        model = Settings
        fields = ['key', 'value']

class UploadImageForm(Form):
    """
    A form for uploading an image file.

    It includes a file field labeled 'Upload Image'.
    """
    image = FileField(label='Upload Image')
