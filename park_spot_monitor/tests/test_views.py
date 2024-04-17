import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import Plates
from django.test import Client


@pytest.fixture
def client():
    return Client()

@pytest.fixture
def user(django_db):
    return User.objects.create_user(username='testuser', email='test@example.com', password='password')

def test_user_dashboard(client, user):
    client.login(username='testuser', password='password')
    response = client.get(reverse('users:user_dashboard'))
    assert response.status_code == 200

def test_add_plate(client, user):
    client.login(username='testuser', password='password')
    response = client.post(reverse('users:add_plate'), {'plate': 'ABC123'})
    assert response.status_code == 302  # Redirects after adding plate

def test_show_plates(client, user):
    client.login(username='testuser', password='password')
    response = client.get(reverse('users:show_plates'))
    assert response.status_code == 200

