from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main_app/index.html', {"title": "Main page"})