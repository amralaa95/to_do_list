from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')

        user = User(username=username)
        user.save()

        messages.success(request, 'User added successfully!')
        response = redirect('tasks:lists')
        response.set_cookie('user', user.id, max_age=604800) # 604800s = 1 week
        return response

    return render(request, 'users/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')

        user = User.objects.filter(username=username).first()
        response = redirect('tasks:lists')
        response.set_cookie('user', user.id, max_age=604800) # 604800s = 1 week
        return response

    return render(request, 'users/signin.html')

def logout(request):
    response = redirect('tasks:lists')
    response.delete_cookie('user')
    return response
