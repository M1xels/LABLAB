from os import name
from django.urls import path
from django.conf import settings
from . import views

app_name = 'Labapp'
urlpatterns = [ 
    path('', views.index, name='index'),
    path('Login/', views.Login, name='Login'),
    path('register/', views.register, name='register'),
    path('registration/', views.registration, name='registration'),
    path('homepage/', views.homepage, name='homepage'),
    path('software/', views.software, name='software'),
    path('softwaredata/', views.softwaredata, name='softwaredata'),
    path('hardware/', views.hardware, name='hardware'),
    path('equipmentdevice/', views.equipmentdevice, name='equipmentdevice'),
    path('EquipmentDevice/', views.EquipmentDevice, name='EquipmentDevice'),
    path('performrequest/', views.performrequest, name='performrequest'),
    path('records/', views.records, name='records'),
    path('delete/<int:Pcnum>', views.delete, name='delete'),
    path('logout/', views.logoutUser, name='logout'),


    
]