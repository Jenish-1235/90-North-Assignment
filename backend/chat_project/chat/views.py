# backend/chat_project/chat/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Message
from django.db.models import Q

def register(request):
    """
    Handle user registration.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def chat_home(request):
    """
    Display the chat interface with a list of users.
    """
    users = User.objects.exclude(username=request.user.username)  # Exclude the current user
    return render(request, 'chat/chat_home.html', {'users': users})
