from django.shortcuts import render
from users.models import Balance


def main(request):
    Balance.objects.get_or_create(user=request.user)
    return render(request, 'main_app/index.html', {"title": "Main page"})