from django.shortcuts import render, redirect
from django.http import HttpResponse

import time

from .forms import TaskForm
from .models import Task
# Create your views here.


def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    context = {
        'tasks': tasks,
        'form': form,
    }
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    elif request.method == "GET":
        return render(request=request, template_name="tasks/list.html", context=context)


def update_task(request, primary_key):
    ...


def remove_task(request, primary_key):
    Task.objects.all().filter(id=primary_key).delete()
    return redirect("/")


def complete_task(request, primary_key):
    ...
