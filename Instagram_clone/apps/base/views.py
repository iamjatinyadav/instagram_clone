from django.shortcuts import render, HttpResponse
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.


def index(request):
    return render(request, "base/index.html")


def search(request):
    return render(request, "base/search.html")


def explore(request):
    return render(request, "base/explore.html")


def notifications(request):
    return render(request, "base/notifications.html")


class HandleLogin(LoginView):
    template_name = "base/login.html"


class HandleLogout(LogoutView):
    template_name = "base/index.html"


def signup(request):
    return render(request, "base/signup.html")