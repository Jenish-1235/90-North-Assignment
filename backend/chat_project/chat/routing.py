# backend/chat_project/chat/routing.py
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/chat/<str:username>/', consumers.ChatConsumer.as_asgi()),
]
