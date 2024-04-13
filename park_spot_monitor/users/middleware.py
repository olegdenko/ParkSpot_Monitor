from django.contrib import messages
from django.shortcuts import redirect
from .models import BlacklistedVehicle
from django.shortcuts import render

class CheckBlacklistMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            try:
                blacklisted = BlacklistedVehicle.objects.filter(user=request.user).exists()

                if blacklisted:
                    messages.error(request, 'Your account has been blocked.')
                    return render(request, 'users/blocked_account.html')
            except BlacklistedVehicle.DoesNotExist:
                pass

        return response
