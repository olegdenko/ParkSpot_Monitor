from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main_app/index.html', {"title": "Main page"})

def balance_insufficient(request):
    return render(request, 'main_app/templates/main_app//balance_insufficient.html')
