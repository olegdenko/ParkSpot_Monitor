# import os
# from django.shortcuts import render, redirect
# from .models import RegisteredNumberPlate, ParkingRate, BlacklistedVehicle
# from .forms import NumberPlateForm, ParkingRateForm, BlacklistForm
# from django.contrib.auth import authenticate, login

# def admin_login(request):
#     if request.method == 'POST':
#         admin_username = request.POST.get('admin_username')
#         admin_password = request.POST.get('admin_password')
        
#         # Отримання значень із змінних середовища
#         correct_admin_username = os.environ.get('ADMIN_USERNAME')
#         correct_admin_password = os.environ.get('ADMIN_PASSWORD')
        
#         if admin_username == correct_admin_username and admin_password == correct_admin_password:
#             user = authenticate(username=admin_username, password=admin_password)
#             if user is not None and user.is_staff:
#                 login(request, user)
#                 return redirect('admin_dashboard')  # Перенаправлення на адмінську панель
#             else:
#                 # Якщо ввійти не вдалося, відображення повідомлення про помилку або повернення на сторінку входу
#                 return render(request, 'admin_app/admin_login.html', {'error_message': 'Invalid credentials'})
        
#     return render(request, 'admin_app/admin_login.html', {})

# def add_number_plate(request):
#     if request.method == 'POST':
#         form = NumberPlateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('admin_app:add_number_plate')
#     else:
#         form = NumberPlateForm()
#     return render(request, 'admin_app/add_number_plate.html', {'form': form})

# def delete_number_plate(request, plate_id):
#     plate = RegisteredNumberPlate.objects.get(id=plate_id)
#     if request.method == 'POST':
#         plate.delete()
#         return redirect('admin_app:add_number_plate')
#     return render(request, 'admin_app/delete_number_plate.html', {'plate': plate})

# def configure_parking_rates(request):
#     rates = ParkingRate.objects.all()
#     if request.method == 'POST':
#         form = ParkingRateForm(request.POST)
#         if form.is_valid():
#             hourly_rate = form.cleaned_data['hourly_rate']
#             daily_rate = form.cleaned_data['daily_rate']
#             for rate in rates:
#                 rate.hourly_rate = hourly_rate
#                 rate.daily_rate = daily_rate
#                 rate.save()
#             return redirect('admin_app:configure_parking_rates')
#     else:
#         form = ParkingRateForm()
#     return render(request, 'admin_app/configure_parking_rates.html', {'form': form, 'rates': rates})

# def add_to_blacklist(request):
#     if request.method == 'POST':
#         form = BlacklistForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('admin_app:add_to_blacklist')
#     else:
#         form = BlacklistForm()
#     return render(request, 'admin_app/add_to_blacklist.html', {'form': form})

