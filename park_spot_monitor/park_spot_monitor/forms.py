from django import forms
from main_app.models import Plates, Sessions


class PlateForm(forms.ModelForm):
    class Meta:
        model = Plates
        fields = ['plate', 'user']


class SessionForm(forms.ModelForm):
    class Meta:
        model = Sessions
        exclude = ['entrance_time', 'exit_time', 'plate']
