from django import forms

from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']
        
class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']