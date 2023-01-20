from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, "base/index.html")


def search(request):
    return render(request, "base/search.html")


def explore(request):
    return render(request, "base/explore.html")


def notifications(request):
    return render(request, "base/notifications.html")


def login(request):
    return render(request, "base/login.html")


def signup(request):
    return render(request, "base/signup.html")