from django.urls import path
from . import views

app_name = 'app_code'
urlpatterns = [
    path('', views.home, name='home')
]