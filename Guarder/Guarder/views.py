from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse
from django.shortcuts import render, redirect


from employee.models import *

import datetime


def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def emplog(request):
    if request.method =='POST':
        try:
            n = request.POST['e_email']
            p = request.POST['e_pass']
            user = Employee.objects.get(email=n, password=p)
            return redirect('./employee/')
        except:
            return render(request, 'login.html')
