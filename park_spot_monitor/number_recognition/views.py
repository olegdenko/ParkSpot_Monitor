from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import View
from users.models import Plates, Sessions
from .number_recognition import recognize_plate
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
import cv2
from admin_app.forms import UploadImageForm
from django.shortcuts import render

@method_decorator(csrf_exempt, name='dispatch')
class UploadImageView(View):
    def get(self, request, *args, **kwargs):
        initial_data = {
            'image': None,  
        }

        form = UploadImageForm(initial=initial_data)  

        context = {
            'form': form,  
        }

        return render(request, 'number_recognition/number_recognition.html', context)    


    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            image_file = request.FILES['image']
            plate_number = recognize_plate(image_file)

            if plate_number:
                try:
                    
                    plate = Plates.objects.get(plate=plate_number)
                    
                    last_session = Sessions.objects.filter(plate=plate).order_by('-entrance_time').first()
                    
                    if last_session and not last_session.exit_time:
                        
                        last_session.exit_time = timezone.now()
                        last_session.save()
                        return HttpResponse(f"Транспортний засіб з номером {plate_number} виїхав.")
                    else:
                        
                        session = Sessions.objects.create(plate=plate)
                        return HttpResponse(f"Транспортний засіб з номером {plate_number} заїхав.")
                except Plates.DoesNotExist:
                    plate = Plates.objects.create(plate=plate_number)
                    session = Sessions.objects.create(plate=plate)

                    return HttpResponse(f"Новий транспортний засіб з номером {plate_number} заїхав.")
            else:
                return HttpResponse("Номер не розпізнано")


