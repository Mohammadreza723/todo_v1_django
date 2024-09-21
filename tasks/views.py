from django.shortcuts import render, redirect

from .forms import TaskForm, TaskUpdateForm
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
    form = TaskUpdateForm()
    context = {
        'form': form,
        'primary_key': primary_key,
    }
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('title')
            Task.objects.filter(id=primary_key).update(title=text)
        return redirect('/')
    elif request.method == "GET":
        return render(request=request, template_name="tasks/update_task.html", context=context)

        


def remove_task(request, primary_key):
    Task.objects.filter(id=primary_key).delete()
    return redirect("/")


def complete_task(request, primary_key):
    situation = Task.objects.filter(id=primary_key).values_list('complete')[0][0]
    Task.objects.filter(id=primary_key).update(complete=not situation)
    return redirect("/")
