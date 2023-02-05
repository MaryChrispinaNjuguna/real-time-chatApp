from django.urls import path, include
from app.consumers import ChatConsumer

#Here, "" is routing to the URL ChatConsumer which...
# will handle chat functionality

websocket_urlpatterns = [
    path("/",ChatConsumer.as_asgi()),
]