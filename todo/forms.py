from django import forms
from django.forms import ModelForm, fields

from .models import *

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'🐾 New item...', 'style': 'width: 100%;'}))

    class Meta:
        model = Task
        fields = '__all__'
