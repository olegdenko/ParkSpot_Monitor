from django.shortcuts import render

from users.models import Plates

# Create your views here.
def main(request):
    plates = None
    if request.user.is_authenticated:
        plates = Plates.objects.all()
    
    return render(request, 'main_app/index.html', {"title": "Main page", "plates": plates})