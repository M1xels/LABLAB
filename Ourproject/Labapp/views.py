from multiprocessing import context
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
import mysql.connector as sql
from django.contrib.auth.forms import UserCreationForm
from .forms import StaffRegistration, instructorRegistration
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

installed_apps = ['Labapp']

def adminregistration(request):
    form = StaffRegistration()
    if request.method == "POST":
        form = StaffRegistration(request.POST)
        if form.is_valid():
            Job_description = form.cleaned_data.get("UITC Staff")
            form.instance.Job_descriptions = 'UITC Staff'
            form.save()  
            return redirect('/index')

    context = {
        'form':form
    }
    return render(request, 'pages/REGISTER.html', context)


def registration(request):
    form = instructorRegistration()
    if request.method == "POST":
        form = instructorRegistration(request.POST)
        if form.is_valid():
            job_description = form.cleaned_data.get("UITC Staff")
            form.instance.job_description = 'Computer Instructor'
            form.save()  
            return redirect('/index')

    context = {
        'form':form
    }
    return render(request, 'pages/REGISTER.html', context)
        
def index(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None and user.Job_description == "Computer Instructor":
            login(request, user)
            return redirect('/homepage')
        
        elif user is not None and user.Job_description == "UITC Staff":
            login(request, user)
            return redirect('/EquipmentDevice')
        else:
            messages.info(request, 'INVALID CREDENTIALS')
    return render(request, 'pages/LOG.html')


def logoutUser(request):
    logout(request)
    return redirect('/index')


def register(request):
   return render(request, 'pages/REGISTER.html')   
   
@login_required(login_url='/index')
def homepage(request):
    if request.user.is_authenticated and request.user.Job_description == 'Computer Instructor':
        return render(request, 'pages/HOMEPAGE.html')

@login_required(login_url='/index')
def hardware(request):
    if request.user.is_authenticated and request.user.Job_description == 'Computer Instructor':
        return render(request, 'pages/HARDWARE.html')

@login_required(login_url='/index')
def software(request):
    if request.user.is_authenticated and request.user.Job_description == 'Computer Instructor':
        return render(request, 'pages/SOFTWARE.html')

@login_required(login_url='/index')
def Equipmentdevice(request):
    if request.user.is_authenticated and request.user.Job_description == 'UITC Staff':
        return render(request, 'pages/EQUIPMENT_DEVICE.html')

def EquipmentDevice(request):
    data = equipmentdevicel1.objects.last()
    return render(request, 'pages/EQUIPMENT_DEVICE.html',{'data':data})
    
@login_required(login_url='/index')
def performrequest(request):
    if request.user.is_authenticated and request.user.Job_description == 'UITC Staff':
        datasr = software_reports.objects.all()
        return render(request, 'pages/PERFORM_REQUEST.html',{'datasr':datasr})

def delete(request, Pcnum):
    datasr = software_reports.objects.get(Pcnum=Pcnum)
    datasr.delete()
    return redirect('/performrequest')
    
@login_required(login_url='/index')
def records(request):
    if request.user.is_authenticated and request.user.Job_description == 'UITC Staff':
        return render(request, 'pages/RECORDS.html')


def equipmentdevice(request):
    if request.method=='POST':
        Labnum = '1'
        pcnum = "1"
        sysunit = request.POST.get('system_unit')
        mntr = request.POST.get('monitor')
        kbrd = request.POST.get('kboard')
        ms = request.POST.get('mouse')
        Avr = request.POST.get('avr')
        Remarks = request.POST.get('rmrks')
        data = equipmentdevicel1.objects.create(lab_num = Labnum, pc_num=pcnum, system_unit=sysunit, monitor=mntr, keyboard=kbrd, mouse=ms, avr=Avr, remarks=Remarks)
        data.save()
        return redirect("/EquipmentDevice")

def softwaredata(request):
    if request.method=='POST':
        Uname = request.POST.get('Username')
        Labno = request.POST.get('Labnum')
        Pcno = request.POST.get('Pcnum')
        TypeofC = request.POST.get('TypeofConcern')
        Mess = request.POST.get('Message')
        
        data = software_reports.objects.create(User_name=Uname, Lab_num=Labno, Pc_num=Pcno, Type_concern=TypeofC, Message=Mess)
        data.save()
        return redirect('/software')





 


