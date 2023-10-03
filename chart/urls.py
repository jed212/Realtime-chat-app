from django.urls import path, include
from chart.views import chatPage, chatRoom, LoginView, LogoutView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path("", chatPage, name="chat-page"),
    path("", chatRoom, name="chat-room"),
    
    path("login/", LoginView.as_view
         (template_name="loginPage.html"), name="login-user"),
    path("logout/", login_required(LogoutView.as_view()), name="logout-user"),
]
