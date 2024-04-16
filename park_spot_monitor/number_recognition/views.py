from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.cache import never_cache
from django.conf import settings 
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError

from admin_app.forms import UploadImageForm 
from users.models import Plates, Sessions
from .number_recognition import recognize_plate

from datetime import datetime
import cv2
import os
import time

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
            image_file = request.FILES.get('image')
            if image_file:
                plate_number = recognize_plate(image_file)
                if plate_number:
                    try:
                        if request.user.is_authenticated:
                            user = request.user
                            try:
                                plate = Plates.objects.get(plate=plate_number)
                                try:
                                    session = Sessions.objects.get(plate=plate, exit_time=None)
                                    session.exit_time = datetime.now()
                                    session.save()
                                except ObjectDoesNotExist:
                                    session = Sessions.objects.create(plate=plate)
                            except ObjectDoesNotExist:
                                plate = Plates.objects.create(plate=plate_number, user=user)
                                session = Sessions.objects.create(plate=plate)
                            
                            return JsonResponse({'message': f"Номер розпізнано: {plate_number}. Сесія створена.", 'plate_number': plate_number})
                        else:
                            return JsonResponse({'message': "Для створення сесії, потрібно увійти до системи."})
                    except Exception as e:
                        print(f"Error processing plate: {e}")
                        return JsonResponse({'message': "Помилка обробки даних. Спробуйте ще раз."})
                else:
                    return JsonResponse({'message': "Номер не розпізнано"})
            else:
                return JsonResponse({'message': "Файл не було завантажено"})