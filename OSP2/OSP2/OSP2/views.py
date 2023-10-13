from django.shortcuts import render,HttpResponse,redirect
from college.models import *

import datetime


from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages


def index(request):
    pat = College.objects.all()
    data = {'cdata':pat,'hstatus':'active'}
    return render(request, 'index.html', data)

def clgreg(request):
    if request.method == 'POST':
        fn = request.POST['fullname']
        w = request.POST['website']
        e = request.POST['email']
        ps = request.POST['pass']
        m = request.POST['mobile']
        add = request.POST['address']
        cty=request.POST['city'] 
        desc=request.POST['desc'] 
        i = request.FILES.get('imag')
        u = request.POST['uni']
        univ = University.objects.get(id=u)
        print(i)
        ins = College(cname=fn, cweb=m, cemail=e, cpass=ps, cmob=m, cadd=add, ccity=cty, cdesc=desc, cimg=i, uid=univ)
        ins.save()
        cl=College.objects.all()
        params = {'data': 'Thank you for registration','rstatus': 'active','cdata':cl}
        return render(request, 'index.html', params)

    else:
        uni = University.objects.all
        print(uni)
        dict={'rstatus': 'active','university':uni,'data': 'Register Your College'}
        return render(request,'clgreg.html',dict)

def clglog(request):
    if request.method =='POST':
        try:
            n = request.POST['email']
            p = request.POST['pass']

            user = College.objects.get(cemail=n, cpass=p)
            print(user.id)
            if(user.cstatus=="Yes"):
                request.session['userid']=user.id
                a = datetime.datetime.now()
                request.session['usertime']=a.strftime("%M")
                print(request.session['usertime'])
                params = {'user': user}
                return redirect('./college/')
            else:
                param = {'m': 'Status inactive...'}
                return render(request, 'clglog.html', param)
        except:
            param = {'m': 'Invalid Credential'}
            return render(request, 'clglog.html', param)

    else:
        dict = {'lstatus': 'active'}
        return render(request, 'clglog.html',dict)

def stdlog(request):
    if request.method =='POST':
        try:
            n = request.POST['email']
            p = request.POST['pass']

            user = Student.objects.get(semail=n, spass=p)
            print(user.id)
            if(user.sstatus=="Yes"):
                request.session['userid']=user.id
                a = datetime.datetime.now()
                request.session['usertime']=a.strftime("%M")
                print(request.session['usertime'])
                params = {'user': user}
                return redirect('./student/')
            else:
                param = {'m': 'Status inactive...'}
                return render(request, 'stdlog.html', param)
        except:
            param = {'m': 'Invalid Credential'}
            return render(request, 'stdlog.html', param)

    else:
        return render(request, 'stdlog.html')

def faclog(request):
    if request.method =='POST':
        try:
            n = request.POST['email']
            p = request.POST['pass']

            user = Faculty.objects.get(femail=n, fpass=p)
            print(user.id)
            if(user.fstatus=="Yes"):
                request.session['userid']=user.id
                a = datetime.datetime.now()
                request.session['usertime']=a.strftime("%M")
                print(request.session['usertime'])
                params = {'user': user}
                return redirect('./faculty/')
            else:
                param = {'m': 'Status inactive...'}
                return render(request, 'faclog.html', param)
        except:
            param = {'m': 'Invalid Credential'}
            return render(request, 'faclog.html', param)

    else:
        return render(request, 'faclog.html')


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')