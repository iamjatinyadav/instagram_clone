from django.shortcuts import render
from user.models import *
from django.contrib.auth.decorators import *
from .models import *
# Create your views here.


@login_required()
def profile(request, user):
    user = User.objects.filter(userpersonal__uniquename=user)
    context = {"value": "profile", "username": user}
    return render(request, "user_profile/profile.html", context)


@login_required()
def user_saved(request):
    context = {"value": "user_saved"}
    return render(request, "user_profile/profile.html", context)


@login_required()
def user_tagged(request):
    context = {"value": "user_tagged"}
    return render(request, "user_profile/profile.html", context)


@login_required()
def friendrequest(request, user):

    user = User.objects.get(userpersonal__uniquename=user)
    user_friend_request = FriendsRequest.objects.filter(receiver=user).order_by("-created")
    if user == request.user:
        context = {"user_friend_request": user_friend_request}
        return render(request, "user_profile/friendrequests.html", context)
    else:
        # user = User.objects.filter(userpersonal__uniquename=user)
        return render(request, "404.html")


