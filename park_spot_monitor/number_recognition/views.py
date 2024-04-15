from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import View
from users.models import Plates, Sessions
from .number_recognition import recognize_plate
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

                    plate = Plates.objects.create(plate=plate_number)

                    if request.user.is_authenticated:
                        user = request.user
                        session = Sessions.objects.create(plate=plate, user=user)
                        return HttpResponse(f"Номер розпізнано: {plate_number}. Сесія створена.")
                    else:
                        return HttpResponse("Для створення сесії, потрібно увійти до системи.")
                except Exception as e:
                    print(f"Error processing plate: {e}")
                    return HttpResponse("Помилка обробки даних. Спробуйте ще раз.")
            else:
                return HttpResponse("Номер не розпізнано")
