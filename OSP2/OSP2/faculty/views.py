from django.shortcuts import render,HttpResponse,redirect
from college.models import *
from . forms import *
import datetime

from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
allotedtime = 5

# Create your views here.
def index(request):
    if request.session['userid']!='':

        a = datetime.datetime.now()

        if int(a.strftime("%M")) < int(request.session['usertime']) + allotedtime:
            request.session['usertime'] = int(a.strftime("%M"))
            
            userid = request.session['userid']
            user = Faculty.objects.get(id=userid)
            clg=College.objects.get(id=user.cid_id)
            params = {'user': user,'m':'Login Succesfully','mtype':'success','clg':clg}
            return render(request, 'faculty/index.html', params)
        else:
            request.session['userid'] = ''
            param = {'m': 'time out login again'}
            return render(request,'faclog.html',param)
    else:
        param = {'m': 'Login first'}
        return render(request,'faclog.html',param)

def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response=HttpResponse(fh.read(),content_type="application/fimg")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response
    raise Http404

def header(request):
    userid=request.session['userid']
    user=Faculty.objects.get(id=userid)
    clg=College.objects.get(id=user.cid_id)
    data={'user':user,'clg':clg}
    return render(request,'faculty/header.html',data)

def logout(request):
    request.session['userid']=''
    return redirect('../')

def prof(request):
    if request.session['userid'] != '':
        if request.method == 'POST':
            userid = request.session['userid']
            fn = request.POST['fullname']
            e = request.POST['email']
            m = request.POST['mobile']
            add = request.POST['address']
            p=request.POST['p']

            Faculty.objects.filter(id=userid).update(fname=fn, femail=e, fmob=m, fadd=add,fpass=p)
            user = Faculty.objects.get(id=userid)
            params = {'user': user, 'm': 'Profile Updated Succesfully', 'mtype': 'success'}
            return render(request, 'faculty/prof.html', params)

        else:
            userid=request.session['userid']
            user = Faculty.objects.get(id=userid)
            param={'user':user}
            return render(request, 'faculty/prof.html', param)
    else:
        param = {'m': 'Login first'}
        return render(request,'faclog.html',param)

def sub(request):
    if request.session['userid']!='':
        userid = request.session['userid']
        user=Faculty.objects.get(id=userid)
        clg=College.objects.get(id=user.cid_id)
        
        subject=Subject.objects.filter(cid=user.cid_id,fid=user.id)
        context={'user':user,'clg':clg,'user':user,'subject':subject}
        return render(request,'faculty/sub.html',context)
    else:
        param = {'m': 'Login first'}
        return render(request,'faclog.html',param)

def ass(request,pk=None):
    if request.session['userid']!='':
        userid = request.session['userid']
        user=Faculty.objects.get(id=userid)
        clg=College.objects.get(id=user.cid_id)
        student=Student.objects.get(sname='None')
        subject=Subject.objects.get(id=pk)
        if request.method == "POST":
            form = AssignForm(request.POST,request.FILES)
            if form.is_valid():
                try:
                    finished = request.POST['is_finished']
                    if finished == 'on':
                        finished = True
                    else:
                        finished = False
                except:
                    finished = False
                n=request.FILES['fass']
                assign=Assignment(
                    fid=user,
                    suid=subject,
                    sid_id=student.id,
                    title = request.POST['title'],
                    description=request.POST['description'],
                    fass=n,
                    due = request.POST['due'],
                    is_finished = finished
                )
                assign.save()
                messages.success(request,f'Assignment Added in {subject} from {user}!!')
        else:
            form=AssignForm()
        assign=Assignment.objects.filter(fid=user,suid=pk)
        context={'form':form,'user':user,'clg':clg,'assign':assign,'subject':subject}
        return render(request,'faculty/ass.html',context)
    else:
        param = {'m': 'Login first'}
        return render(request,'faclog.html',param)

def showstds(request):
    if request.session['userid']!='':
        userid = request.session['userid']
        user=Faculty.objects.get(id=userid)
        clg=College.objects.get(id=user.cid_id)
        subject=Subject.objects.filter(fid=userid)
        if request.method=="POST":
          
            sub=Subject.objects.get(id=request.POST['subject'])
            data=Student.objects.filter(sem=sub.susem,coid=sub.coid_id,brid=sub.brid_id,cid=user.cid_id) 
            param={'data':data}              
        else:
            subject=Subject.objects.filter(fid=userid)
        context={'subject':subject,'user':user,'clg':clg,'d':'Search Results are:'}
        return render(request,'faculty/showstds.html',context)
    else:
        param = {'m': 'Login first'}
        return render(request,'clglog.html',param)

def checkass(request,pk=None):
    if request.session['userid']!='':
        userid = request.session['userid']
        user=Faculty.objects.get(id=userid)
        clg=College.objects.get(id=user.cid_id)
        assignm=Assignment.objects.get(id=pk)
        assign=Assignment_Sub.objects.filter(title=assignm.title)
        subject=Subject.objects.get(id=assignm.suid_id)
        branch=Branch.objects.get(id=subject.brid_id)
        course=Course.objects.get(id=branch.coid_id)
        student=Student.objects.get(cid=user.cid_id,sem=subject.susem,coid=course.id,brid=branch.id)
       
        context={'user':user,'clg':clg,'assignm':assignm,'subject':subject,'assign':assign,'student':student}
        return render(request,'faculty/checkass.html',context)
    else:
        param = {'m': 'Login first'}
        return render(request,'faclog.html',param)

def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response=HttpResponse(fh.read(),content_type=("application/fass","applicatio/sass"))
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response
    raise Http404

def update_ass(request,pk=None):
    assign = Assignment_Sub.objects.get(id=pk)
    if assign.is_finished == True:
        assign.is_finished = False
    else:
        assign.is_finished = True
    assign.save()
    return redirect('../faculty/checkass')
