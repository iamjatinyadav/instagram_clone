from django.shortcuts import render, redirect
from user.models import *
from django.contrib.auth.decorators import *
from .models import *
from django.http import HttpResponseRedirect

# Create your views here.


@login_required()
def profile(request, user):
    global follower, following
    user = User.objects.filter(userpersonal__uniquename=user)
    # users_detail = user.values("pk")
    for i in user:
        follower = FriendsRequest.objects.filter(receiver=i.pk).filter(action=True)
        following = FriendsRequest.objects.filter(sender=i.pk).filter(action=True)
    context = {"value": "profile", "username": user, "following": following, "follower": follower}
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
    user_friend_request = FriendsRequest.objects.filter(receiver=user).filter(action=False).order_by("-created")
    if user == request.user:
        context = {"user_friend_request": user_friend_request}
        return render(request, "user_profile/friendrequests.html", context)
    else:
        return render(request, "404.html")


@login_required()
def send_friend_request(request, receiver):
    sender = request.user
    print(receiver)
    receiver = User.objects.get(email=receiver)
    print(receiver)
    send_request = FriendsRequest.objects.create(sender=sender, receiver=receiver, action=False)
    send_request.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required()
def accept_friend_request(request, pk):
    accept_request = FriendsRequest.objects.get(pk=pk)
    accept_request.action = True
    accept_request.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required()
def account_edit(request):
    print("hello from account")
    return render(request, "user_profile/account.html")


def change_password(request):
    value = 0
    context = {"abc": value}
    return render(request, "user_profile/account.html", context)

