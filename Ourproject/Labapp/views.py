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
            return redirect('/Index')

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
            return redirect('/Index')

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
    elif request.user.is_authenticated and request.user.Job_description == "UITC Staff":
        return redirect('/EquipmentDevice')
    elif request.user.is_authenticated and request.user.Job_description == "Computer Instructor":
        return redirect('/homepage')
    return render(request, 'pages/LOG.html')


def Index(request):
    return redirect('http://127.0.0.1:8000/')
    

@login_required(login_url='/Index')
def logoutUser(request):
    logout(request)
    request.user.Job_description = None
    return redirect('/Index')


def register(request):
   return render(request, 'pages/REGISTER.html')   
   
@login_required(login_url='/Index')
def homepage(request):
    if request.user.is_authenticated and request.user.Job_description == 'Computer Instructor':
        return render(request, 'pages/HOMEPAGE.html')
    elif request.user.is_authenticated and request.user.Job_description == 'UITC Staff':
        return redirect('/EquipmentDevice')
    else:
        return redirect('/Index')

@login_required(login_url='/Index')
def hardware(request):
    if request.user.is_authenticated and request.user.Job_description == 'Computer Instructor':
        return render(request, 'pages/HARDWARE.html')
    elif request.user.is_authenticated and request.user.Job_description == 'UITC Staff':
        return redirect('/EquipmentDevice')
    else:
        return redirect('/Index')

@login_required(login_url='/Index')
def software(request):
    if request.user.is_authenticated and request.user.Job_description == 'Computer Instructor':
        return render(request, 'pages/SOFTWARE.html')
    elif request.user.is_authenticated and request.user.Job_description == 'UITC Staff':
        return redirect('/EquipmentDevice')
    else:
        return redirect('/Index')

@login_required(login_url='/Index')
def EquipmentDevice(request):
    if request.user.is_authenticated and request.user.Job_description == 'UITC Staff':
        return render(request, 'pages/EQUIPMENT_DEVICE.html')
    elif request.user.is_authenticated and request.user.Job_description == 'Computer Instructor':
        return redirect('/homepage')
    else:
        return redirect('/Index')

def update(request, id):
    a = perform_request.objects.get(id=id)
    b = '<QuerySet [<perform_request: ' + str(a) + '>]>'
    print(a)
    for x in perform_request.objects.only('id').filter(status= "Ongoing"):
        
        print(x)
        if a == x:
            d = "a"
            print(d)
            x = perform_request.objects.filter(id=id).update(status="Available")
            break
    return redirect('/performrequest')

def delete(request, id):
    a = perform_request.objects.get(id=id)
    b = '<QuerySet [<perform_request: ' + str(a) + '>]>'
    print(a)
    for x in perform_request.objects.only('id').filter(status= "Ongoing"):
        
        print(x)
        if a == x:
            d = "a"
            print(d)
            x = perform_request.objects.get(id=id).delete()
            break
    return redirect('/performrequest')

    

@login_required(login_url='/Index')
def performrequest(request):
    if request.user.is_authenticated and request.user.Job_description == 'UITC Staff':
        data = perform_request.objects.filter(status = "Ongoing")
        return render(request, 'pages/PERFORM_REQUEST.html',{'data':data})
    elif request.user.is_authenticated and request.user.Job_description == 'Computer Instructor':
        return redirect('/homepage')
    else:
        return redirect('/Index')


    
@login_required(login_url='/Index')
def records(request):
    if request.user.is_authenticated and request.user.Job_description == 'UITC Staff':
        return render(request, 'pages/RECORDS.html')
    elif request.user.is_authenticated and request.user.Job_description == 'Computer Instructor':
        return redirect('/homepage')
    else:
        return redirect('/Index')

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
        status = 'Ongoing'
        data = software_reports.objects.create(User_name=Uname, Lab_num=Labno, Pc_num=Pcno, Type_concern=TypeofC, Message=Mess)
        data1 = perform_request.objects.create(name=Uname, Lab_num=Labno, Pc_num=Pcno, Type_report=TypeofC, remarks=Mess, status = status)
        data1.save()
        data.save()
        return redirect('/software')

def hardwaredata(request):
    
    if request.method=='POST':
        name = request.POST.get('name')
        labnum = request.POST.get('labnum')
        pcno = request.POST.get('pcnum')
        s_unit = request.POST.get('sys_unit')
        mtr = request.POST.get('mntor')
        kbrd = request.POST.get('kboard')
        ms = request.POST.get('mouse')
        avr = request.POST.get('AVR')
        cmmt = request.POST.get('comment')
        status = 'Ongoing'
        data = hardware_reports.objects.create(name=name, Lab_num=labnum, Pc_num=pcno, System_unit=s_unit, Monitor=mtr, keyboard=kbrd, Mouse=ms, Avr=avr, Comments=cmmt )
        data1 = perform_request.objects.create(name=name, Lab_num=labnum, Pc_num=pcno, Type_report=s_unit, remarks=cmmt, status = status)
        data1.save()
        data.save()
        return redirect('/hardware')





 


