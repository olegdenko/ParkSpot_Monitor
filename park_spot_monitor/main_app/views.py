from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import Balance


@login_required
def main(request):
    # Check if Balance object exists for the authenticated user
    balance, created = Balance.objects.get_or_create(user=request.user)

    # If you need to do something with the created object, you can
    # For example, initialize some default balance value
    if created:
        balance.amount = 0  # Set default balance amount
        balance.save()

    return render(request, 'main_app/index.html', {"title": "Main page"})
