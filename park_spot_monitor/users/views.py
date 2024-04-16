from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages

from .forms import RegisterForm, PlateForm
from .models import Balance, Sessions, Plates
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

import csv
from django.http import HttpResponse


@login_required
def logout_view(request):
    if request.method == 'GET':
        username = request.user.username
        logout(request)
        return render(request, "users/signout.html", {"title":"Logout user", "username": username})
    return redirect(to="mian_app:main")

def user_dashboard(request):
    entries = Sessions.objects.all()[:10]  # Останні 10 записів
    balance = Balance.objects.get(user=request.user).amount  # Баланс користувача
    payment_due = True  # Перевірте, чи є оплата
    return render(request, 'users/user_dashboard.html', {'entries': entries, 'balance': balance, 'payment_due': payment_due})


def top_up_balance(request):
    # Отримання балансу користувача
    balance = Balance.objects.get(user=request.user)
    # Оновлення балансу на 100 балів
    balance.amount += 100
    balance.save()
    # Після успішного поповнення перенаправлення на сторінку користувача
    return redirect('users:user_dashboard')


class RegisterView(View):
    form_class = RegisterForm
    template_name = "users/signup.html"

    def get(self, request):
        return render(request, self.template_name, {"title":"Register new user", "form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f'Вітаємо, {username}! Ваш акаунт успішно створений')
            return redirect(to='users:login')
        return render(request, self.template_name, {"form": form})

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    html_email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')
    success_message = "An email with instructions to reset your password has been sent to %(email)s."
    subject_template_name = 'users/password_reset_subject.txt'


# Plates
@login_required
def show_plates(request):
    plates = None
    if request.user.is_authenticated:
        plates = Plates.objects.all()
    
    return render(request, 'users/show_plates.html', {"plates": plates})


@login_required
def manage_plate(request, plate_id):
    plate = get_object_or_404(Plates, pk=plate_id)
    return render(request, 'users/manage_plate.html', {"plate": plate})


@login_required
def add_plate(request):
    form = PlateForm(request.POST)
    if form.is_valid(): 
        new_plate = form.save(commit=False)
        new_plate.user = request.user
        new_plate.save()
        return redirect(to='main_app:main')
    else:
        return render(request, 'users/add_plate.html', {'form': form})


def blocked_account_view(request):
    return render(request, 'users/blocked_account.html')
  

@login_required
def delete_plate(request, plate_id):
    Plates.objects.get(id=plate_id, user_id=request.user.id).delete()
    return redirect(to='users:show_plates')


# Sessions report
@login_required
def generate_report_csv(request):
    sessions = Sessions.objects.all()

    field_names = ['Plate', 'User', 'Entrance Time', 'Exit Time']

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="parking_report.csv"'

    writer = csv.DictWriter(response, fieldnames=field_names)
    writer.writeheader()

    for session in sessions:
        writer.writerow({
            'Plate': session.plate.plate,
            'User': session.plate.user.username,
            'Entrance Time': session.entrance_time,
            'Exit Time': session.exit_time if session.exit_time else "Not exited yet"
        })
    return response