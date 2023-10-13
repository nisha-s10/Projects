from django import forms
from django.forms import widgets
from college.models import *

class DateInput(forms.DateInput):
    input_type='date'

class AssignForm(forms.ModelForm):
    class Meta:
        model=Assignment
        widgets = {'due':DateInput()}
        fields=['title','description','fass','due',]

