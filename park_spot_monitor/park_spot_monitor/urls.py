# main_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('plate/create/', views.plate_create, name='plate_create'),
    path('plate/<int:pk>/', views.plate_detail, name='plate_detail'),
    path('plate/<int:pk>/update/', views.plate_update, name='plate_update'),
    path('plate/<int:pk>/delete/', views.plate_delete, name='plate_delete'),
    
    # Аналогічні маршрути для моделі Sessions
    # path('session/create/', views.session_create, name='session_create'),
    # path('session/<int:pk>/', views.session_detail, name='session_detail'),
    # path('session/<int:pk>/update/', views.session_update, name='session_update'),
    # path('session/<int:pk>/delete/', views.session_delete, name='session_delete'),
]
