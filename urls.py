from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('registrationpage',views.registrationpage,name="registrationpage"),
    path('show',views.getdata,name="getdata")
]