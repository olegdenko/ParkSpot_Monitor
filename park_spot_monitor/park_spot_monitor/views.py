from django.shortcuts import render, get_object_or_404, redirect
from main_app.models import Plates
from .forms import PlateForm

def plate_create(request):
    if request.method == 'POST':
        form = PlateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plate_detail', pk=form.instance.pk)
    else:
        form = PlateForm()
    return render(request, 'plate_form.html', {'form': form})

def plate_detail(request, pk):
    plate = get_object_or_404(Plates, pk=pk)
    return render(request, 'plate_detail.html', {'plate': plate})

def plate_update(request, pk):
    plate = get_object_or_404(Plates, pk=pk)
    if request.method == 'POST':
        form = PlateForm(request.POST, instance=plate)
        if form.is_valid():
            form.save()
            return redirect('plate_detail', pk=pk)
    else:
        form = PlateForm(instance=plate)
    return render(request, 'plate_form.html', {'form': form})

def plate_delete(request, pk):
    plate = get_object_or_404(Plates, pk=pk)
    if request.method == 'POST':
        plate.delete()
        return redirect('plate_list')  # Assuming you have a URL named 'plate_list' for listing plates
    return render(request, 'plate_confirm_delete.html', {'plate': plate})
