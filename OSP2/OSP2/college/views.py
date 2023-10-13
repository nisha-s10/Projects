from django.shortcuts import render,HttpResponse,redirect
from college.models import *
from . forms import *
import datetime

from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages

allotedtime = 5

def index(request):
    if request.session['userid']!='':

        a = datetime.datetime.now()

        if int(a.strftime("%M")) < int(request.session['usertime']) + allotedtime:
            request.session['usertime'] = int(a.strftime("%M"))
            
            userid = request.session['userid']
            user = College.objects.get(id=userid)
            
            params = {'user': user,'m':'Login Succesfully','mtype':'success'}
            return render(request, 'college/index.html', params)
        else:
            request.session['userid'] = ''
            param = {'m': 'time out login again'}
            return render(request,'clglog.html',param)
    else:
        param = {'m': 'Login first'}
        return render(request,'clglog.html',param)

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
            w = request.POST['website']
            add = request.POST['address']
            p=request.POST['p']

            College.objects.filter(id=userid).update(cname=fn, cemail=e, cmob=m, cweb=m, cadd=add,cpass=p)
            user = College.objects.get(id=userid)
            params = {'user': user, 'm': 'Profile Updated Succesfully', 'mtype': 'success'}
            return render(request, 'college/prof.html', params)

        else:
            userid=request.session['userid']
            user = College.objects.get(id=userid)
            param={'user':user}
            return render(request, 'college/prof.html', param)
    else:
        param = {'m': 'Login first'}
        return render(request,'clglog.html',param)


def header(request):
    user=request.session['userid']
    user=College.objects.get(id=user)
    data={'user':user}
    return render(request,'college/header.html',data)

def brreg(request,pk=0):
    if request.session['userid']!='':
        userid = request.session['userid']
        user=College.objects.get(id=userid)
        course=Course.objects.get(id=pk)
        if request.method=="POST":
            form=BranchForm(request.POST)
            if form.is_valid():
                branch=Branch(cid=user,coid=course,brname=request.POST['brname'])
                branch.save()
            messages.success(request,f"Branch Added in {course} from {user} Successfully!")
        else:
            form=BranchForm()
        
        branch=Branch.objects.filter(cid=userid,coid=course)
        context={'branch':branch,'form':form,'course':course}
        return render(request,'college/brreg.html',context)
    else:
        param = {'m': 'Login first'}
        return render(request,'clglog.html',param)

def delete_branch(request,pk=None):
    Branch.objects.get(id=pk).delete()
    return redirect("coreg")

def stdprof(request,pk=None):
    if request.session['userid']!='':
        userid = request.session['userid']
        user=College.objects.get(id=userid) 
        student=Student.objects.filter(id=pk)
        context={'user':user,'student':student}
        return render(request,'college/stdprof.html',context)
    else:
        param = {'m': 'Login first'}
        return render(request,'clglog.html',param)

def delete_std(request,pk=None):
    Student.objects.get(id=pk).delete()
    return redirect('showstd')

def coreg(request):
    if request.session['userid']!='':
        userid = request.session['userid']
        user=College.objects.get(id=userid)
        if request.method=="POST":
            form=CourseForm(request.POST)
            if form.is_valid():
                course=Course(cid=user,coname=request.POST['coname'])
                course.save()
            messages.success(request,f"Course Added from {user} Successfully!")
        else:
            form=CourseForm()
        
        course=Course.objects.filter(cid=userid)
        context={'course':course,'form':form,'user':user}
        return render(request,'college/coreg.html',context)
    else:
        param = {'m': 'Login first'}
        return render(request,'clglog.html',param)

def delete_course(request,pk=None):
    Course.objects.get(id=pk).delete()
    return redirect("coreg")

def fac(request):
    if request.session['userid'] != '':
        userid = request.session['userid']
        user = College.objects.get(id=userid)
        faculty=Faculty.objects.filter(cid=user)
        param={'faculty':faculty,'user':user}
        return render(request,'college/fac.html',param)
    else:
        param = {'m': 'Login first'}
        return render(request,'clglog.html',param)

def sub(request,pk=None):
    if request.session['userid']!='':
        userid = request.session['userid']
        user=College.objects.get(id=userid)
        faculty=Faculty.objects.get(id=pk)
        if request.method=="POST":
            form=SubjectForm(request.POST)
            subject=Subject.objects.get(suname=request.POST['suname'])
            branch=Branch.objects.get(id=subject.brid_id)
            course=Course.objects.get(id=subject.coid_id)
            student=Student.objects.get(id=subject.sid_id)
            if form.is_valid():
                sub=Subject.objects.filter(id=subject.id).update(sid=student,fid=faculty)
            messages.success(request,f"Subject Added in {faculty} Successfully!")
        else:
            form=SubjectForm()
        
        subject=Subject.objects.filter(fid=faculty)
        context={'form':form,'faculty':faculty,'user':user,'subject':subject}
        return render(request,'college/sub.html',context)
    else:
        param = {'m': 'Login first'}
        return render(request,'clglog.html',param)

def delete_sub(request,pk=None):
    faculty=Faculty.objects.get(fname='None')
    Subject.objects.filter(id=pk).update(fid=faculty)
    return redirect("fac")


def facreg(request):
    if request.session['userid'] != '':
        userid = request.session['userid']
        user = College.objects.get(id=userid)
                                    #reg student don't make any change in college data
        if request.method == 'POST':
            fn = request.POST['fullname']
            e = request.POST['email']
            ps = request.POST['pass']
            m = request.POST['mobile']
            add = request.POST['address']
            cty = request.POST['city']
            desc = request.POST['desc']
            i = request.FILES.get('imag')
            ins = Faculty(cid=user,fname=fn, femail=e, fpass=ps, fmob=m,fadd=add, fcity=cty, fdesc=desc, fimg=i)
            # simg=request.GET['imag']
            ins.save()
            params = {'m': 'Thank you for registration','user': user}
            print(params)
            return render(request, 'college/index.html', params)
        else:
            param = {'user': user}
            return render(request,'college/facreg.html',param)
    else:
        param = {'m': 'Login first'}
        return render(request,'clglog.html',param)
   
   

def showfac(request):
    if request.session['userid'] != '':
        userid = request.session['userid']
        user = College.objects.get(id=userid)
        faculty = Faculty.objects.filter(cid=userid)
        param = {'data':faculty,'user':user,'d':'List of all facultys are:'}
        return render(request,'college/showfac.html',param)
    else:
        param = {'m': 'Login first'}
        return render(request,'clglog.html',param)

def update_status1(request,pk=None):
    faculty = Faculty.objects.get(id=pk)
    if faculty.fstatus == "Yes":
        faculty.fstatus = ""
    else:
        faculty.fstatus = "Yes"
    faculty.save()
    return redirect('showfac')

def showstd(request):
    if request.session['userid'] != '':
        if request.method == 'POST':
            try:
                if request.POST['course'] and request.POST['branch']:
                    co = request.POST['course']
                    br = request.POST['branch']
                    print(co, br)
                    print("hello")
                    userid = request.session['userid']
                    user = College.objects.get(id=userid)
                    course = Course.objects.filter(cid=userid)
                    allbranches = Branch.objects.filter(brname='x')
                    for i in course:
                        branches = Branch.objects.filter(coid=i)
                        allbranches = branches.union(allbranches)
                    data = Student.objects.filter(coid=co,brid=br,cid=user)
                    print(data)
                    
              
                    param = {'course': course, 'branch': allbranches, 'user': user, 'data': data,'d':'Search Results are:'}
                    return render(request, 'college/showstd.html', param)
                if request.POST['course']:
                    co = request.POST['course']
                    print(co)
                    print("hello course only")
                    userid = request.session['userid']
                    user = College.objects.get(id=userid)
                    course = Course.objects.filter(cid=userid)
                    allbranches = Branch.objects.filter(brname='x')
                    for i in course:
                        branches = Branch.objects.filter(coid=i)
                        allbranches = branches.union(allbranches)
                    data = Student.objects.filter(coid=co,cid=user)
                    stat=request.GET['stat']
                    print(stat)  
                    param = {'course': course, 'branch': allbranches, 'user': user, 'data': data,'d':'Search Results are:'}
                    return render(request, 'college/showstd.html', param)
                if request.POST['branch']:
                    br = request.POST['branch']
                    print(br)
                    userid = request.session['userid']
                    user = College.objects.get(id=userid)
                    course = Course.objects.filter(cid=userid)
                    allbranches = Branch.objects.filter(brname='x')
                    for i in course:
                        branches = Branch.objects.filter(coid=i)
                        allbranches = branches.union(allbranches)
                    data = Student.objects.filter(brid=br,cid=user)
                    print(data)
                   
                    param = {'course': course, 'branch': allbranches, 'user': user, 'data': data,'d':'Search Results are:'}
                    return render(request, 'college/showstd.html', param)
            except:
                print("it is except")
                userid = request.session['userid']
                user = College.objects.get(id=userid)
                course = Course.objects.filter(cid=userid)
                allbranches = Branch.objects.filter(brname='x')
                for i in course:
                    branches = Branch.objects.filter(coid=i)
                    allbranches = branches.union(allbranches)
                data = Student.objects.filter(cid=user)
               
                param = {'course': course, 'branch': allbranches, 'user': user, 'data': data,'d':'Invalid Cradential'}
                return render(request, 'college/showstd.html', param)
        else:
            userid = request.session['userid']
            user = College.objects.get(id=userid)
            course=Course.objects.filter(cid=userid)
            allbranches = Branch.objects.filter(brname='x')
            for i in course:
                branches = Branch.objects.filter(coid=i)
                allbranches = branches.union(allbranches)
            data = Student.objects.filter(cid=user)
            
           
            param={'course':course,'branch':allbranches,'user':user,'data':data,'d':'List of all Students are:'}
            return render(request,'college/showstd.html',param)
    else:
        param = {'m': 'Login first'}
        return render(request,'clglog.html',param)

def update_status(request,pk=None):
    student = Student.objects.get(id=pk)
    if student.sstatus == "Yes":
        student.sstatus = ""
    else:
        student.sstatus = "Yes"
    student.save()
    return redirect('showstd')

def stdreg(request):
    if request.session['userid'] != '':
        userid = request.session['userid']
        user = College.objects.get(id=userid)
                                    #reg student don't make any change in college data
        if request.method == 'POST':
            fn = request.POST['fullname']
            rn = request.POST['rolno']
            e = request.POST['email']
            ps = request.POST['pass']
            m = request.POST['mobile']
            c = request.POST['co']
            b = request.POST['br']
            s = request.POST['sem']
            add = request.POST['address']
            cty = request.POST['city']
            desc = request.POST['desc']
            i = request.FILES.get('imag')
            bran = Branch.objects.get(id=b)
            cour=Course.objects.get(id=c)

            ins = Student(cid_id=userid,sname=fn, rolno=rn, semail=e, spass=ps, smob=m, coid_id=c, brid_id=b, sem=s, sadd=add, scity=cty, sdesc=desc, simg=i)
            # simg=request.GET['imag']
            ins.save()
            params = {'m': 'Thank you for registration','user': user}
            print(params)
            return render(request, 'college/index.html', params)
        else:
            courses = Course.objects.filter(cid=userid)
            allbranches = Branch.objects.filter(brname='x')
            for i in courses:
                branches = Branch.objects.filter(coid=i)
                allbranches = branches.union(allbranches)
            param = {'user': user,'branches':allbranches,'courses':courses}
            return render(request,'college/stdreg.html',param)
    else:
        param = {'m': 'Login first'}
        return render(request,'clglog.html',param)


def subreg(request,pk=None):
    if request.session['userid'] != '':
        userid = request.session['userid']
        user=College.objects.get(id=userid)
        branch=Branch.objects.get(id=pk)
        course=Course.objects.get(id=branch.coid_id)
        faculty=Faculty.objects.get(fname='None')
        student=Student.objects.get(sname='None')
        if request.method=="POST":
            form=SubjectForm(request.POST)
            if form.is_valid():
                subject=Subject(coid=course,cid=user,brid=branch,fid=faculty,sid_id=student.id,suname=request.POST['suname'])
                subject.save()
            messages.success(request,f"Subject Added in {course}({branch}) from {user} Successfully!")
        else:
            form=SubjectForm()
        
        subject=Subject.objects.filter(coid=course,brid=branch)
        context={'branch':branch,'form':form,'course':course,'subject':subject}
        return render(request,'college/subreg.html',context)
    else:
        param = {'m': 'Login first'}
        return render(request,'clglog.html',param)

def delete_subject(request,pk=None):
    Subject.objects.get(id=pk).delete()
    return redirect("coreg")

def assign_sub(request):
    if request.session['userid']!='':
        userid = request.session['userid']
        user=College.objects.get(id=userid)
        course=Course.objects.filter(cid=userid)
        branch=Branch.objects.filter(cid=userid)
        subject=Subject.objects.filter(cid=userid)
        if request.method=="POST":
            s=request.POST['suid']
            c=request.POST['coid']
            b=request.POST['brid']
            se=request.POST['sem']
            Subject.objects.filter(id=s).update(coid=c, brid=b,susem=se)                
            messages.success(request,f"Subject updated from {user} Successfully!")
        else:
            course=Course.objects.filter(cid=userid)
            branch=Branch.objects.filter(cid=userid)
            subject=Subject.objects.filter(cid=userid)
        context={'subject':subject,'course':course,'branch':branch,'user':user}
        return render(request,'college/assign_sub.html',context)
    else:
        param = {'m': 'Login first'}
        return render(request,'clglog.html',param)
