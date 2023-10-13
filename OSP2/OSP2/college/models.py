from django.db import models

# Create your models here.
class University(models.Model):
    uname=models.CharField(max_length=50)

    def __str__(self):
        return self.uname

class College(models.Model):
    uid=models.ForeignKey(University,on_delete=models.CASCADE)
    cname=models.CharField(max_length=50)
    cemail=models.CharField(max_length=50)
    cmob=models.CharField(max_length=12)
    cadd=models.CharField(max_length=100)
    ccity=models.CharField(max_length=50)
    cweb=models.CharField(max_length=50)
    cdesc=models.CharField(max_length=500)
    cimg=models.ImageField(upload_to='college/', default='college/Screenshot.png')
    cstatus=models.CharField(max_length=10,blank=True)
    cpass=models.CharField(max_length=50,default='12345')

    def __str__(self):
        return self.cname

class Course(models.Model):
    cid=models.ForeignKey(College,on_delete=models.CASCADE)
    coname=models.CharField(max_length=20)


    def __str__(self):
        return self.coname

class Branch(models.Model):
    cid=models.ForeignKey(College,on_delete=models.CASCADE,default='0')
    coid = models.ForeignKey(Course,on_delete=models.CASCADE,default='0')
    brname = models.CharField(max_length=50)

    def __str__(self):
        return self.brname



class Student(models.Model):
    cid=models.ForeignKey(College, on_delete=models.CASCADE,default='0')
    rolno = models.CharField(max_length=50,default='0')
    coid=models.ForeignKey(Course, on_delete=models.CASCADE,default='0')
    brid = models.ForeignKey(Branch, on_delete=models.CASCADE,default='0')
    sem = models.CharField(max_length=50,default='0')
    sname=models.CharField(max_length=50,default='')
    semail=models.CharField(max_length=50,default='')
    smob=models.CharField(max_length=12,default='')
    swa=models.CharField(max_length=12,default='')
    sadd=models.CharField(max_length=100,default='')
    scity=models.CharField(max_length=50,default='')
    sdesc=models.CharField(max_length=500,default='')
    penass=models.CharField(max_length=10,default='0')                                #pending assignment
    simg = models.ImageField(upload_to='student/', default='college/Screenshot.png')
    sstatus=models.CharField(max_length=10,blank=True)
    spass = models.CharField(max_length=50, default='12345')

    def __str__(self):
        return self.sname

class Faculty(models.Model):
    cid=models.ForeignKey(College, on_delete=models.CASCADE,default='0')
    fname=models.CharField(max_length=50,default='')
    femail=models.CharField(max_length=50,default='')
    fmob=models.CharField(max_length=12,default='')
    fwa=models.CharField(max_length=12,default='')
    fadd=models.CharField(max_length=100,default='')
    fcity=models.CharField(max_length=50,default='')
    fdesc=models.CharField(max_length=500,default='')
    fimg = models.ImageField(upload_to='faculty/', default='college/Screenshot.png')
    fstatus=models.CharField(max_length=10,blank=True)
    fpass = models.CharField(max_length=50, default='12345')

    def __str__(self):
        return self.fname

class Subject(models.Model):
    coid=models.ForeignKey(Course,on_delete=models.CASCADE,default='0')
    brid = models.ForeignKey(Branch,on_delete=models.CASCADE,default='0')
    sid = models.ForeignKey(Student,on_delete=models.CASCADE,default='0')
    cid=models.ForeignKey(College,on_delete=models.CASCADE,default='0')
    fid = models.ForeignKey(Faculty,on_delete=models.CASCADE,blank=True,default='0')
    suname = models.CharField(max_length=50)
    susem= models.CharField(max_length=50,default='0')

    def __str__(self):
        return self.suname

class Notes(models.Model):
    user=models.ForeignKey(Student,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    description=models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="notes"
        verbose_name_plural="notes"

class Homework(models.Model):
    user=models.ForeignKey(Student,on_delete=models.CASCADE)
    subject=models.CharField(max_length=50)
    title=models.CharField(max_length=100)
    description=models.TextField()
    due=models.DateTimeField()
    is_finished=models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Todo(models.Model):
    user=models.ForeignKey(Student,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    is_finished=models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Assignment(models.Model):
    suid=models.ForeignKey(Subject, on_delete=models.CASCADE)
    fid=models.ForeignKey(Faculty, on_delete=models.CASCADE)
    sid=models.ForeignKey(Student, on_delete=models.CASCADE,default='0')
    title=models.CharField(max_length=100)
    description=models.TextField(default="-")
    fass=models.FileField(upload_to='student/assignment/', default='college/Screenshot.png')
    due=models.DateTimeField()
    is_finished=models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Assignment_Sub(models.Model):
    assid=models.ForeignKey(Assignment, on_delete=models.CASCADE)
    sid=models.ForeignKey(Student,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    sass=models.FileField(upload_to='faculty/assignment/', default='college/Screenshot.png')
    description=models.TextField(default="-")
    is_finished=models.BooleanField(default=False)

    def __str__(self):
        return self.title
