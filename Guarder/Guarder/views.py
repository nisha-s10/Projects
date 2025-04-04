from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse
from django.shortcuts import render, redirect


from employee.models import *

import datetime


def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

import datetime
from django.shortcuts import render, redirect
from employee.models import Employee

def emplog(request):
    if request.method == 'POST':
        try:
            n = request.POST['e_email']
            p = request.POST['e_pass']
            user = Employee.objects.get(email=n, password=p)

            # Store user data in session
            request.session['employee_id'] = user.employee_id
            request.session['employee_email'] = user.email

            # Store full timestamp for accurate session timeout
            current_time = datetime.datetime.now()
            request.session['login_time'] = current_time.strftime("%Y-%m-%d %H:%M:%S")

            return redirect('./employee/')  # Redirect to employee dashboard
        except Employee.DoesNotExist:
            param = {'m': 'Invalid Credentials'}
            return render(request, 'login.html', param)

    return render(request, 'login.html')
