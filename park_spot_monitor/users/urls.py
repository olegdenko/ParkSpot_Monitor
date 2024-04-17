from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .views import RegisterView, ResetPasswordView, logout_view, add_plate, show_plates, manage_plate, delete_plate,blocked_account_view, generate_report_csv, show_balance, top_up_balance, sessions_history


from .forms import LoginForm

app_name = "users"

urlpatterns = [
     path("signup/", RegisterView.as_view(), name='register'),
     path("login/", LoginView.as_view(template_name='users/signin.html', authentication_form=LoginForm,
                                     redirect_authenticated_user=True), name='login'),
     path("logout/", logout_view, name="logout"),
     path('reset-password/', ResetPasswordView.as_view(), name='password_reset'),
     path('reset-password/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
          name='password_reset_done'),
     path('reset-password/confirm/<uidb64>/<token>/',
          PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html',
                                             success_url='/users/reset-password/complete/'),
          name='password_reset_confirm'),
     path('reset-password/complete/',
          PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
          name='password_reset_complete'),
     path('show_plates/', show_plates, name='show_plates'),
     path('manage_plate/<int:plate_id>', manage_plate, name='manage_plate'),
     path('add_plate/', add_plate, name='add_plate'),
     path('blocked_account/', blocked_account_view, name='blocked_account'),
     path('delete_plate/<int:plate_id>', delete_plate, name='delete_plate'),
     path('generate_report_csv/', generate_report_csv, name='generate_report_csv'),
     path('show_balance/', show_balance, name='show_balance'),
     path('top_up_balance/', top_up_balance, name='top_up_balance'),
     path('sessions_history/', sessions_history, name='sessions_history')
]
