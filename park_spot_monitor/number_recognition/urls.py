from django.urls import path
from .views import UploadImageView

urlpatterns = [
    path('', UploadImageView.as_view(), name='number_recognition'),
]