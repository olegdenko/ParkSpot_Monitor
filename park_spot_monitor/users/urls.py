from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView



from .forms import LoginForm

app_name = "users"

urlpatterns = [


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
]