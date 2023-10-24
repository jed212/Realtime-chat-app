from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def chatPage(request, *args, **kwargs):
	if not request.user.is_authenticated:
		return redirect("login-user")
	context = {}
	return render(request, "chatPage.html", context)

def chatRoom(request, *args, **kwargs):
	return render(request, "chatRoom.html")

def LoginView(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or home page
            home_url = 'chat-page'
            return redirect(home_url)
        else:
            # Handle authentication failure
            return render(request, "loginPage.html", {"error_message": "Invalid login credentials"})
    return render(request, "loginPage.html")

def LogoutView(request):
    logout(request)
    # Redirect to a logout success page or home page
    return redirect("home")