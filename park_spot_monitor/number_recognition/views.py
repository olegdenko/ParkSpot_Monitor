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
from django.utils import timezone

from admin_app.forms import UploadImageForm 
from users.models import Plates, Sessions, Balance
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
     

    def withdrawing_from_balance(self, request, session):
        balance = Balance.objects.get(user=request.user)

        total_hours_spent = (session.exit_time-session.entrance_time).total_seconds() // 3600
        session.total_hours_spent = total_hours_spent
        session.save()

        one_hour_price = 10
        withdrawed_money = one_hour_price
        if total_hours_spent > 0:
            withdrawed_money = total_hours_spent * one_hour_price
        
        balance.balance -= withdrawed_money
        balance.save()

        return withdrawed_money
    

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            image_file = request.FILES.get('image')
            if image_file:
                plate_number = recognize_plate(image_file)
                if plate_number:
                    try:
                        if request.user.is_authenticated:
                            user = request.user
                            balance = Balance.objects.get(user=user)
                            try:
                                plate = Plates.objects.get(plate=plate_number)
                                try:
                                    session = Sessions.objects.get(plate=plate, exit_time=None)
                                    session.exit_time = timezone.now() 
                                    session.save()
                                    withdrawed_money = self.withdrawing_from_balance(request, session)
                                    return JsonResponse({'message': f"Сесію для номера {plate_number} закрито. Плату списано: {withdrawed_money}$"})

                                except ObjectDoesNotExist:
                                    if balance.balance > 0:
                                        session = Sessions.objects.create(plate=plate)
                                    else:
                                        return JsonResponse({'message': f"Недостатньо коштів (баланс - {balance.balance}$)"})
                            except ObjectDoesNotExist:
                                if balance.balance > 0:
                                    plate = Plates.objects.create(plate=plate_number, user=user)
                                    session = Sessions.objects.create(plate=plate)
                                else:
                                    return JsonResponse({'message': f"Недостатньо коштів (баланс - {balance.balance}$)"})

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