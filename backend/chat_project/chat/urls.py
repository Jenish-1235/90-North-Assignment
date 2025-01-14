# backend/chat_project/chat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # User registration
    path('', views.chat_home, name='chat_home'),  # Chat interface
]
