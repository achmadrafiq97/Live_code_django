from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Home

# Create your views here.
def home(request):
    homes = Home.objects.all()
    return render(request, 'app_code/home.html', {'homes':homes})
