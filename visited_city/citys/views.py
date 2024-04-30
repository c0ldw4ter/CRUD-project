from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm

def index(request):
    cities = City.objects.all()
    form = CityForm()
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'citys/index.html', {'cities': cities, 'form': form})

def add(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CityForm()
    return render(request, 'citys/index.html', {'form': form})

def delete(request, city_id):
    City.objects.filter(id=city_id).delete()
    return redirect('home')

def edit(request, city_id):
    city = City.objects.get(id=city_id)
    if request.method == 'POST':
        form = CityForm(request.POST, instance=city)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CityForm(instance=city)
    return render(request, 'citys/edit.html', {'form': form, 'city': city})