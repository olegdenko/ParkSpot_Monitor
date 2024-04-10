from django.urls import path
from . import views

app_name = 'main_app'

urlpatterns = [
  path('', views.main, name='main'),
  path('balance-insufficient/', views.balance_insufficient, name='balance_insufficient'),
]
