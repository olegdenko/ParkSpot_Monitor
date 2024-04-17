from django.shortcuts import render
from users.models import Balance


def main(request):
    return render(request, 'main_app/index.html', {"title": "Main page"})