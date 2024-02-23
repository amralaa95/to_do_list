from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, List
from users.models import User
from django.contrib import messages


def create_list(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        list = List(name=name)
        list.save()
        messages.success(request, 'List added successfully!')
        return redirect('tasks:lists')

    return render(request, 'tasks/create_list.html')


def lists(request):
    user = User.objects.filter(id=request.COOKIES.get('user'))
    lists = List.objects.all()
    context = {
        'lists': lists,
        'user': user.first().username if user.first() else '',
    }
    return render(request, 'tasks/lists.html', context)


def get_list(request, list_id):
    list = get_object_or_404(List, id=list_id)
    user = User.objects.filter(id=request.COOKIES.get('user'))
    tasks = Task.objects.filter(list_id=list_id)
    context = {
        'list': list,
        'tasks': tasks,
        'user': user.first().username if user.first() else '',
    }
    return render(request, 'tasks/list_tasks.html', context)


def create_task(request, list_id):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        user = User.objects.filter(id=request.COOKIES.get('user')).first()
        list = List.objects.get(id=list_id)
        task = Task(user=user, list=list, title=title, description=description)
        task.save()
        messages.success(request, 'Task added successfully!')
        return redirect('tasks:get_list', list_id)

    return render(request, 'tasks/lists.html', {})



def search_tasks(request, list_id):
    title = request.POST.get('title')
    list = get_object_or_404(List, id=list_id)
    user = User.objects.filter(id=request.COOKIES.get('user'))
    tasks = Task.objects.filter(list_id=list,title=title)
    context = {
        'list': list,
        'tasks': tasks,
        'user': user.first().username if user.first() else '',
    }

    return render(request, 'tasks/list_tasks.html', context)


def update_task(request, list_id, task_id):
    list = get_object_or_404(List, id=list_id)
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        for field in ['title', 'description', 'is_completed']:
            if field in request.POST:
                setattr(task, field, request.POST[field])

        if request.POST['is_completed'] == 'incomplete':
            task.is_completed = False
        else:
            task.is_completed=True
        task.save()
        messages.success(request, 'Task updated successfully!')
        return redirect('tasks:get_list', list_id)

    context = {'task': task}
    return render(request, 'tasks/update_task.html', context)


def delete_task(request, list_id, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    messages.success(request, 'Task deleted succefully!')
    return redirect('tasks:get_list', list_id)


def complete_task(request, list_id, task_id):
    task = Task.objects.get(pk=task_id)
    task.is_completed=True
    task.save()
    messages.success(request, 'Task completed succefully!')
    return redirect('tasks:get_list', list_id)
