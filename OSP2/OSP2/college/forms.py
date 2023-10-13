from django import forms
from django.forms import widgets
from . models import *


class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields=['coname']

class BranchForm(forms.ModelForm):
    class Meta:
        model=Branch
        fields=['brname']

class SubjectForm(forms.ModelForm):
    class Meta:
        model=Subject
        fields=['suname']



