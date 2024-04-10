from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages

from .forms import RegisterForm, PlateForm
from .models import Balance, Sessions, Plates
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

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