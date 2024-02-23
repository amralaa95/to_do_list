import re
from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from django.contrib import messages
from django.db import IntegrityError
from django.core.exceptions import ValidationError


def signup(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            if len(re.findall(r'[^\S\n\t]+', username)) > 0 :
                raise ValidationError('No spaces allowed in username')

            user = User(username=username)
            user.save()
            messages.success(request, 'User added successfully!')
            response = redirect('tasks:lists')
            response.set_cookie('user', user.id, max_age=604800) # 604800s = 1 week
            return response
        except IntegrityError:
            messages.error(request, 'Username is already exist')
        except Exception as error:
            messages.error(request, error)
    return render(request, 'users/signup.html')


def signin(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            user = get_object_or_404(User, username=username)
            response = redirect('tasks:lists')
            response.set_cookie('user', user.id, max_age=604800) # 604800s = 1 week
            return response
        except Exception:
            messages.error(request, 'Username is not found')
    return render(request, 'users/signin.html')


def logout(request):
    response = redirect('tasks:lists')
    response.delete_cookie('user')
    return response
