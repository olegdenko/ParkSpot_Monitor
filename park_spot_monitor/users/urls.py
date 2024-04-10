from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


from .views import RegisterView, ResetPasswordView, logout_view, user_dashboard, top_up_balance, add_plate, show_plates

from .forms import LoginForm

app_name = "users"

urlpatterns = [
     path('dashboard/', user_dashboard, name='user_dashboard'),
     path('top_up_balance/', top_up_balance, name='top_up_balance'),
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
     path('add_plate/', add_plate, name='add_plate'),
     path('show_plates/', show_plates, name='show_plates'),
]