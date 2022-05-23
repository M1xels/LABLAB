from pickle import TRUE
from sqlite3 import Date
from django.db import models
import os
from django.db.models.deletion import CASCADE
import django.utils.timezone

from django.contrib.auth.models import AbstractUser

class register1(AbstractUser):
    job_option = [
        ('Computer Instructor', 'Computer Instructor'),
        ('UITC Staff', 'UITC Staff'),
    ]
    Job_description = models.CharField(max_length = 40, null=False, choices=job_option)
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')



class index(models.Model):
    id = models.ForeignKey(register1,unique=True, on_delete= CASCADE, primary_key= True,)
    User_name = models.CharField(max_length= 50, null=False)
    Password_data =models.CharField(default= "", max_length =40, null=False, unique = True)


    


class homepage(models.Model):

    Availability = [
        ('AVAILABLE ', 'AVAILABLE '),
        ('OCCUPIED ', 'OCCUPIED '),

        ]
    Section_name= models.CharField(max_length= 50, null=False)
    date = models.DateField( default=django.utils.timezone.now, )
    Time_in = models.TimeField(null=False)
    Time_out = models.TimeField(null=False)
    Status = models.CharField(max_length=50, choices = Availability, null=False)


    
    
    

class hardware_reports(models.Model):
    Laboratories = [
        ('LABORATORY 1', 'LABORATORY 1'),
        ('LABORATORY 2', 'LABORATORY 2'),
        ('LABORATORY 3', 'LABORATORY 3'),
        ('LABORATORY 4', 'LABORATORY 4'),
        ]
    name = models.CharField(max_length=100, null = False)
    Lab_num = models.CharField(max_length=50, choices = Laboratories, null=False)
    Pc_num = models.IntegerField(null=False)
    System_unit = models.CharField(max_length=10, null=True)
    Monitor = models.CharField(max_length=10, null=True)
    keyboard = models.CharField(max_length=10, null=True)
    Mouse = models.CharField(max_length=10, null=True)
    Avr = models.CharField(max_length=10, null=True)
    Comments = models.CharField(max_length=50)

    

class software_reports(models.Model):
    Laboratory_num = [
        ('LABORATORY 1', 'LABORATORY 1'),
        ('LABORATORY 2', 'LABORATORY 2'),
        ('LABORATORY 3', 'LABORATORY 3'),
        ('LABORATORY 4', 'LABORATORY 4'),
        ]
    Concern = [
        ('Request', 'Request'),
        ('Complain', 'Complain'),
        ('Suggest', 'Suggest'),
        ('Others', 'Others'),
        ]
    User_name = models.CharField(max_length=100, null=False)
    Lab_num = models.CharField(max_length=50, choices = Laboratory_num, null=False)
    Pc_num = models.IntegerField(null=False)
    Type_concern = models.CharField(max_length=50, choices = Concern, null=False)
    Message = models.CharField(max_length=256, null=False)

    

class equipmentdevicel1(models.Model):
    lab_num = models.PositiveIntegerField(primary_key=True, null=False)
    pc_num =models.PositiveIntegerField()
    system_unit = models.CharField(max_length=10, null=True)
    monitor = models.CharField(max_length=10, null=True)
    keyboard = models.CharField(max_length=10, null=True)
    mouse = models.CharField(max_length=10, null=True)
    avr = models.CharField(max_length=10, null=True)
    r_choices = [
        ('Good', 'Good'),
        ('Replace', 'Replace'),
        ('On-process', 'Onprocess'),
        ]
    remarks = models.CharField(max_length=20, choices=r_choices)


class perform_request(models.Model):
    date = models.DateField(default=django.utils.timezone.now)
    name = models.CharField(max_length=100)
    Lab_num = models.CharField(max_length=50)
    Pc_num = models.PositiveIntegerField()
    Type_report = models.CharField(max_length=100)
    remarks = models.CharField(max_length=300)
    s_choices = [
        ('Ongoing', 'Ongoing'),
        ('Available to use', 'Available to use'),
    ]
    status = models.CharField(max_length=30, choices= s_choices)

