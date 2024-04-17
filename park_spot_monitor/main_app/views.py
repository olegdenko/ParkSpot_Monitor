from django.shortcuts import render


def main(request):
    return render(request, 'main_app/index.html', {"title": "Main page"})