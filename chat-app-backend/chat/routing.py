from django.urls import path
from .consumers import PersonalChatConsumer

# Here, "" is routing to the URL PersonalChatConsumer which
# will handle the chat functionality.
websocket_urlpatterns = [
	path('ws/chat/<int:id>/' , PersonalChatConsumer.as_asgi()) ,
]
