from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from django.http import HttpResponse


from .forms import RegisterForm, PlateForm
from .models import Balance, Sessions, Plates

import csv



@login_required
def logout_view(request):
    """
    Logs out the user and renders a sign-out page.

    :param request: The HTTP request.
    :type request: HttpRequest
    :return: Rendered sign-out page.
    :rtype: HttpResponse
    """
    if request.method == 'GET':
        username = request.user.username
        logout(request)
        return render(request, "users/signout.html", {"title":"Logout user", "username": username})
    return redirect(to="mian_app:main")


class RegisterView(View):
    """
    Class-based view for user registration.

    :param View: Base class for all views.
    :type View: django.views.View
    """
    form_class = RegisterForm
    template_name = "users/signup.html"

    def get(self, request):
        """
        Renders the registration form page.

        :param request: The HTTP request.
        :type request: HttpRequest
        :return: Rendered registration form page.
        :rtype: HttpResponse
        """
        return render(request, self.template_name, {"title":"Register new user", "form": self.form_class})

    def post(self, request):
        """
        Handles the submission of the registration form.

        :param request: The HTTP request.
        :type request: HttpRequest
        :return: Redirects to the login page upon successful registration.
        :rtype: HttpResponse
        """
        form = self.form_class(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f'Вітаємо, {username}! Ваш акаунт успішно створений')
            return redirect(to='users:login')
        return render(request, self.template_name, {"form": form})

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    """
    Class-based view for password reset.
    """
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    html_email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')
    success_message = "An email with instructions to reset your password has been sent to %(email)s."
    subject_template_name = 'users/password_reset_subject.txt'


# Plates
@login_required
def show_plates(request):
    """
    Renders the page displaying all registered plates.

    :param request: The HTTP request.
    :type request: HttpRequest
    :return: Rendered page displaying all registered plates.
    :rtype: HttpResponse
    """
    plates = None
    if request.user.is_authenticated:
        plates = Plates.objects.all()
    
    return render(request, 'users/show_plates.html', {"plates": plates})


@login_required
def manage_plate(request, plate_id):
    """
    Renders the page for managing a specific plate.

    :param request: The HTTP request.
    :type request: HttpRequest
    :param plate_id: The ID of the plate to manage.
    :type plate_id: int
    :return: Rendered page for managing the plate.
    :rtype: HttpResponse
    """
    plate = get_object_or_404(Plates, pk=plate_id)
    return render(request, 'users/manage_plate.html', {"plate": plate})


@login_required
def add_plate(request):
    """
    Adds a new plate for the authenticated user.

    :param request: The HTTP request.
    :type request: HttpRequest
    :return: Redirects to the main app page upon successful addition.
    :rtype: HttpResponse
    """
    form = PlateForm(request.POST)
    if form.is_valid(): 
        new_plate = form.save(commit=False)
        new_plate.user = request.user
        new_plate.save()
        return redirect(to='main_app:main')
    else:
        return render(request, 'users/add_plate.html', {'form': form})


def blocked_account_view(request):
    """
    Renders the blocked account page.

    :param request: The HTTP request.
    :type request: HttpRequest
    :return: Rendered blocked account page.
    :rtype: HttpResponse
    """
    return render(request, 'users/blocked_account.html')
  

@login_required
def delete_plate(request, plate_id):
    """
    Deletes a plate associated with the authenticated user.

    :param request: The HTTP request.
    :type request: HttpRequest
    :param plate_id: The ID of the plate to delete.
    :type plate_id: int
    :return: Redirects to the page displaying all registered plates.
    :rtype: HttpResponse
    """
    Plates.objects.get(id=plate_id, user_id=request.user.id).delete()
    return redirect(to='users:show_plates')


# Balance
@login_required
def show_balance(request):
    balance = Balance.objects.get(user=request.user)
    return render(request, 'users/show_balance.html', {"balance": balance})


@login_required
def top_up_balance(request):
    balance = Balance.objects.get(user=request.user)
    balance.balance += 10
    balance.save()
    return redirect('users:show_balance')



# Sessions
@login_required
def sessions_history(request):
    ...


@login_required
def generate_report_csv(request):
    """
    Generates and downloads a CSV report of parking sessions.

    :param request: The HTTP request.
    :type request: HttpRequest
    :return: CSV file response containing parking session data.
    :rtype: HttpResponse
    """
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