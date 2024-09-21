from django.shortcuts import render
from .models import Task
# Create your views here.

def index(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request=request, template_name="tasks/list.html", context=context)
