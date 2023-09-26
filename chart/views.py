from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def chatPage(request, *args, **kwargs):
	if not request.user.is_authenticated:
		return redirect("login-user")
	context = {}
	return render(request, "chart/templates/chatPage.html", context)

def chatRoom(request, *args, **kwargs):
	return render(request, "chart/templates/chatRoom.html")

def LoginView(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or home page
            return redirect("home")
        else:
            # Handle authentication failure
            return render(request, "chart/templates/loginPage.html", {"error_message": "Invalid login credentials"})
    return render(request, "chart/templates/loginPage.html")

def LogoutView(request):
    logout(request)
    # Redirect to a logout success page or home page
    return redirect("home")