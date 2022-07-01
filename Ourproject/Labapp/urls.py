from os import name
from django.urls import path
from django.conf import settings
from . import views

app_name = 'Labapp'
urlpatterns = [ 
    path('', views.index, name='index'),
    path('Index/', views.Index, name='Index'),
    path('register/', views.register, name='register'),
    path('registration/', views.registration, name='registration'),
    path('homepage/', views.homepage, name='homepage'),
    path('software/', views.software, name='software'),
    path('softwaredata/', views.softwaredata, name='softwaredata'),
    path('hardware/', views.hardware, name='hardware'),
    path('hardwaredata/', views.hardwaredata, name='hardwaredata'),
    path('equipmentdevice/', views.equipmentdevice, name='equipmentdevice'),
    path('EquipmentDevice/', views.EquipmentDevice, name='EquipmentDevice'),
    path('performrequest/', views.performrequest, name='performrequest'),
    path('update/<int:id>', views.update, name='update'),
    path('records/', views.records, name='records'),
    path('emails/', views.emails, name='emails'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('logout/', views.logoutUser, name='logout'),


    
]