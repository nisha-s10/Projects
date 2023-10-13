from django.shortcuts import render,HttpResponse,redirect
from college.models import *
from . forms import *
import datetime
import os
from django.http import Http404
from django.conf import settings

from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import generic
from youtubesearchpython import VideosSearch
import requests,wikipedia

allotedtime = 20

def index(request):
    if request.session['userid']!='':

        a = datetime.datetime.now()
        print(int(a.strftime("%M")), "<" ,int(request.session['usertime']) + 2)

        if int(a.strftime("%M")) < int(request.session['usertime']) + 2:
            request.session['usertime'] = int(a.strftime("%M"))
            userid = request.session['userid']
            user = Student.objects.get(id=userid)
            clg=College.objects.get(id=user.cid_id)
            params = {'user': user,'clg':clg,'m':'Login Succesfully','mtype':'success'}
            return render(request, 'student/index.html', params)
        else:
            request.session['userid'] = ''
            param = {'m': 'time out login again'}
            return render(request,'stdlog.html',param)
    else:
        param = {'m': 'Login first'}
        return render(request,'stdlog.html',param)

def logout(request):
    request.session['userid']=''
    return redirect('../')

def header(request):
    userid=request.session['userid']
    user=Student.objects.get(id=userid)
    clg=College.objects.get(id=user.cid_id)
    data={'user':user,'clg':clg}
    return render(request,'student/header.html',data)

def checkass(request):
    return render(request,'student/checkass.html')

def showatt(request):
    return render(request,'student/showatt.html')


def prof(request):
    if request.session['userid'] != '':
        if request.method == 'POST':
            userid = request.session['userid']
            user=Student.objects.get(id=userid)
            clg=College.objects.get(id=user.cid_id)
            fn = request.POST['fullname']
            e = request.POST['email']
            m = request.POST['mobile']
            s = request.POST['sem']
            add = request.POST['address']
            p=request.POST['p']

            Student.objects.filter(id=userid).update(sname=fn, semail=e, smob=m, sem=s, sadd=add,spass=p)
            user = Student.objects.get(id=userid)
            params = {'user': user, 'm': 'Profile Updated Succesfully', 'mtype': 'success','clg':clg}
            return render(request, 'student/prof.html', params)

        else:
            userid=request.session['userid']
            user = Student.objects.get(id=userid)
            clg=College.objects.get(id=user.cid_id)
            param={'user':user,'clg':clg}
            return render(request, 'student/prof.html', param)
    else:
        param = {'m': 'Login first'}
        return render(request,'stdlog.html',param)

def subj(request):
    if request.session['userid']!='':
        userid = request.session['userid']
        user=Student.objects.get(id=userid)
        clg=College.objects.get(id=user.cid_id)
        
        subject=Subject.objects.filter(cid=user.cid_id,susem=user.sem,coid=user.coid_id,brid=user.brid_id)
        context={'user':user,'clg':clg,'user':user,'subject':subject}
        return render(request,'student/subj.html',context)
    else:
        param = {'m': 'Login first'}
        return render(request,'stdlog.html',param)

def stdsec(request):
    if request.session['userid']!='':
        userid=request.session['userid']
        user=Student.objects.get(id=userid)
        clg=College.objects.get(id=user.cid_id)
        context={'user':user,'clg':clg}
        return render(request,'student/stdsec.html')
    else:
        param = {'m': 'Login first'}
        return render(request,'stdlog.html',param)

def notes_detail(request,pk):
    notes=Notes.objects.get(id=pk)
    context={'notes':notes}
    return render(request,'student/notes_detail.html',context)

def notes(request):
    if request.session['userid']!='':
        userid = request.session['userid']
        user=Student.objects.get(id=userid)
        clg=College.objects.get(id=user.cid_id)
        if request.method=="POST":
            form=NotesForm(request.POST)
            if form.is_valid():
                notes=Notes(user=user,title=request.POST['title'],description=request.POST['description'])
                notes.save()
            messages.success(request,f"Notes Added from {user} Successfully!")
        else:
            form=NotesForm()
        
        notes=Notes.objects.filter(user=userid)
        context={'notes':notes,'form':form,'clg':clg}
        return render(request,'student/notes.html',context)
    else:
        param = {'m': 'Login first'}
        return render(request,'stdlog.html',param)


def delete_note(request,pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect("notes")

def homework(request):
    if request.session['userid']!='':
        userid = request.session['userid']
        user=Student.objects.get(id=userid)
        clg=College.objects.get(id=user.cid_id)
        if request.method == "POST":
            form = HomeworkForm(request.POST)
            if form.is_valid():
                try:
                    finished = request.POST['is_finished']
                    if finished == 'on':
                        finished = True
                    else:
                        finished = False
                except:
                    finished = False

                homeworks=Homework(
                    user=user,
                    subject = request.POST['subject'],
                    title = request.POST['title'],
                    description=request.POST['description'],
                    due = request.POST['due'],
                    is_finished = finished
                )
                homeworks.save()
                messages.success(request,f'Homework Added from {user}!!')
        else:
            form=HomeworkForm()
        homework=Homework.objects.filter(user=userid)
        if len(homework)==0:
            homework_done=True
        else:
            homework_done=False
        context={'homeworks':homework,'homeworks_done':homework_done,'form':form,'user':user,'clg':clg}
        return render(request,'student/homework.html',context)
    else:
        param = {'m': 'Login first'}
        return render(request,'stdlog.html',param)


def update_homework(request,pk=None):
    homework = Homework.objects.get(id=pk)
    if homework.is_finished == True:
        homework.is_finished = False
    else:
        homework.is_finished = True
    homework.save()
    return redirect('homework')

def delete_homework(request,pk=None):
    Homework.objects.get(id=pk).delete()
    return redirect('homework')

def youtube(request):
    if request.session['userid']!='':
        if request.method == "POST":
            form = DashboardForm(request.POST)
            text=request.POST['text']
            video = VideosSearch(text,limit=10)
            result_list=[]
            for i in video.result()['result']:
                result_dict = {
                    'input':text,
                    'title':i['title'],
                    'duration':i['duration'],
                    'thumbnail':i['thumbnails'][0]['url'],
                    'channel':i['channel']['name'],
                    'link':i['link'],
                    'views':i['viewCount']['short'],
                    'published':i['publishedTime'],
                }
                desc = ''
                if i['descriptionSnippet']:
                    for j in i['descriptionSnippet']:
                        desc +=j['text']
                result_dict['description'] = desc
                result_list.append(result_dict)
                context={
                    'form':form,
                    'results':result_list
                }
            return render(request,'student/youtube.html',context)
        else:
            form=DashboardForm()
        context = {'form':form}
        return render(request,'student/youtube.html',context)
    else:
        param = {'m': 'Login first'}
        return render(request,'stdlog.html',param)

def todo(request):
    if request.session['userid']!='':
        userid = request.session['userid']
        user=Student.objects.get(id=userid)
        clg=College.objects.get(id=user.cid_id)
        if request.method=="POST":
            form=TodoForm(request.POST)
            if form.is_valid():
                try:
                    finished = request.POST['is_finished']
                    if finished == 'on':
                        finished = True
                    else:
                        finished = False
                except:
                    finished = False
                todos=Todo(
                    user=user,
                    title=request.POST['title'],
                    is_finished=finished
                )
                todos.save()
                messages.success(request,f"Todo Added from {user}!!")
        else:
            form=TodoForm()
        todo=Todo.objects.filter(user=userid)
        if len(todo)==0:
            todos_done=True
        else:
            todos_done=False
        context={'form':form,'todos':todo,'todos_done':todos_done,'user':user,'clg':clg}
        return render(request,'student/todo.html',context)
    else:
        param = {'m': 'Login first'}
        return render(request,'stdlog.html',param)

def update_todo(request,pk=None):
    todo = Todo.objects.get(id=pk)
    if todo.is_finished == True:
        todo.is_finished = False
    else:
        todo.is_finished = True
    todo.save()
    return redirect('todo')

def delete_todo(request,pk=None):
    Todo.objects.get(id=pk).delete()
    return redirect('todo')

def books(request):
    if request.session['userid']!='':
        if request.method == "POST":
            form = DashboardForm(request.POST)
            text=request.POST['text']
            url="https://www.googleapis.com/books/v1/volumes?q="+text
            r=requests.get(url)
            answer=r.json()
            result_list=[]
            for i in range(10):
                result_dict = {
                    'title':answer['items'][i]['volumeInfo']['title'],
                    'subtitle':answer['items'][i]['volumeInfo'].get('subtitle'),
                    'description':answer['items'][i]['volumeInfo'].get('description'),
                    'count':answer['items'][i]['volumeInfo'].get('pageCount'),
                    'categories':answer['items'][i]['volumeInfo'].get('categories'),
                    'rating':answer['items'][i]['volumeInfo'].get('pageRating'),
                    'thumbnail':answer['items'][i]['volumeInfo'].get('imageLinks').get('thumbnail'),
                    'preview':answer['items'][i]['volumeInfo'].get('previewLink'),
                }

                result_list.append(result_dict)
                context={
                    'form':form,
                    'results':result_list
                }
            return render(request,'student/books.html',context)
        else:
            form=DashboardForm()
        context = {'form':form}
        return render(request,'student/books.html',context)
    else:
        param = {'m': 'Login first'}
        return render(request,'stdlog.html',param)

def dictionary(request):
    if request.session['userid']!='':
        if request.method == "POST":
            form = DashboardForm(request.POST)
            text=request.POST['text']
            url="https://api.dictionaryapi.dev/api/v2/entries/en_US/"+text
            r=requests.get(url)
            answer=r.json()
            try:
                phonetics=answer[0]['phonetics'][0]['text']
                audio=answer[0]['phonetics'][0]['audio']
                definition=answer[0]['meanings'][0]['definitions'][0]['definition']
                example=answer[0]['meanings'][0]['definitions'][0]['example']
                synonyms=answer[0]['meanings'][0]['definitions'][0]['synonyms']
                context={
                    'form':form,
                    'input':text,
                    'phonetics':phonetics,
                    'audio':audio,
                    'definition':definition,
                    'example':example,
                    'synonyms':synonyms
                }

            except:
                context={
                    'form':form,
                    'input':''
                }
            return render(request,'student/dictionary.html',context)
        else:
            form=DashboardForm()
            context = {'form':form}
        return render(request,'student/dictionary.html',context)
    else:
        param = {'m': 'Login first'}
        return render(request,'stdlog.html',param)

def wiki(request):
    if request.session['userid']!='':
        if request.method == 'POST':
            text = request.POST['text']
            form = DashboardForm(request.POST)
            search = wikipedia.page(text)
            context = {
                'form':form,
                'title':search.title,
                'link':search.url,
                'details':search.summary
            }
            return render(request,'student\wiki.html',context)
        else:
            form=DashboardForm()
            context = {'form':form}
        return render(request,'student/wiki.html',context)
    else:
        param = {'m': 'Login first'}
        return render(request,'stdlog.html',param)

def conversion(request):
    if request.session['userid']!='':
        if request.method == "POST":
            form = ConversionForm(request.POST)
            if request.POST['measurement'] == 'length':
                measurement_form = ConversionLengthForm()
                context = {
                    'form':form,
                    'm_form':measurement_form,
                    'input':True
                }
                if 'input' in request.POST:
                    first = request.POST['measure1']
                    second = request.POST['measure2']
                    input = request.POST['input']
                    answer = ''
                    if input and int(input) >= 0:
                        if first == 'yard' and second == 'foot':
                            answer = f'{input} yard = {int(input)*3} foot'
                        if first == 'foot' and second == 'yard':
                            answer = f'{input} foot = {int(input)/3} yard'
                    context = {
                        'form':form,
                        'm_form':measurement_form,
                        'input':True,
                        'answer':answer
                    }
            if request.POST['measurement'] == 'mass':
                measurement_form = ConversionMassForm()
                context = {
                    'form':form,
                    'm_form':measurement_form,
                    'input':True
                }
                if 'input' in request.POST:
                    first = request.POST['measure1']
                    second = request.POST['measure2']
                    input = request.POST['input']
                    answer = ''
                    if input and int(input) >= 0:
                        if first == 'pound' and second == 'kilogram':
                            answer = f'{input} pound = {int(input)*0.453592} kilogram'
                        if first == 'kilogram' and second == 'pound':
                            answer = f'{input} kilogram = {int(input)*2.20462} pound'
                    context = {
                        'form':form,
                        'm_form':measurement_form,
                        'input':True,
                        'answer':answer
                    }
        else:
            form = ConversionForm()
            context = {'form':form,'input':False}
        return render(request, 'student\conversion.html',context)
    else:
        param = {'m': 'Login first'}
        return render(request,'stdlog.html',param)

def profile(request):
    userid = request.session['userid']
    user=Student.objects.get(id=userid)
    homeworks=Homework.objects.filter(is_finished=False,user=user)
    todos=Todo.objects.filter(is_finished=False,user=user)
    if len(homeworks) == 0:
        homework_done = True
    else:
        homework_done = False
    if len(todos) == 0:
        todos_done = True
    else:
        todos_done = False
    context={
        'homeworks':homeworks,
        'todos':todos,
        'homework_done':homework_done,
        'todos_done':todos_done
    }
    return render(request,'student/profile.html',context)

def subass(request,pk=None):
    if request.session['userid']!='':
        userid = request.session['userid']
        user=Student.objects.get(id=userid)
        clg=College.objects.get(id=user.cid_id)
        assign=Assignment.objects.get(id=pk)
        subject=Subject.objects.get(id=assign.suid_id)
        if request.method == "POST":
            form = SubmitForm(request.POST,request.FILES)
            if form.is_valid():
                try:
                    finished = request.POST['is_finished']
                    if finished == 'on':
                        finished = True
                    else:
                        finished = False
                except:
                    finished = False
                n=request.FILES['sass']
                assign=Assignment_Sub(
                    assid=assign,
                    sid=user,
                    title = request.POST['title'],
                    description=request.POST['description'],
                    sass=n,
                    is_finished = finished
                )
                assign.save()
                messages.success(request,f'Assignment Submitted in {subject} from {user}!!')
                
        else:
            form=SubmitForm()
        sassign=Assignment_Sub.objects.get(assid=assign.id,title=assign.title)
        context={'form':form,'user':user,'clg':clg,'assign':assign,'subject':subject,'sassign':sassign}
        return render(request,'student/subass.html',context)
    else:
        param = {'m': 'Login first'}
        return render(request,'stdlog.html',param)

def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response=HttpResponse(fh.read(),content_type="application/fass")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response
    raise Http404

def showass(request,pk=None):
    if request.session['userid']!='':
        userid=request.session['userid']
        user=Student.objects.get(id=userid)
        clg=College.objects.get(id=user.cid_id)
        subject=Subject.objects.get(id=pk)
        assign=Assignment.objects.filter(suid=pk)
        print(assign)
        context={'user':user,'clg':clg,'assign':assign,'subject':subject}
        return render(request,'student/showass.html',context)
    else:
        param = {'m': 'Login first'}
        return render(request,'stdlog.html',param)