from django.shortcuts import render, redirect

# Create your views here.
def chatPage(request, *args, **kwargs):
	if not request.user.is_authenticated:
		return redirect("login-user")
	context = {}
	return render(request, "chart/chatPage.html", context)

def chatRoom(request, *args, **kwargs):
	return render(request, "chart/chatRoom.html")