from django.urls import path , include
from accounts.consumers import PersonalChatConsumer

# Here, "" is routing to the URL PersonalChatConsumer which
# will handle the chat functionality.
websocket_urlpatterns = [
	path("" , PersonalChatConsumer.as_asgi()) ,
]
