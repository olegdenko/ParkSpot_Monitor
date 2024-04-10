from django.shortcuts import redirect
from django.urls import reverse

class BalanceCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        if user.is_authenticated:
            if user.balance <= 0:  # !!!Потрібно трохи виправити, так як я не знайшов "balance"!!!
                return redirect(reverse('balance_insufficient'))

        response = self.get_response(request)
        return response
