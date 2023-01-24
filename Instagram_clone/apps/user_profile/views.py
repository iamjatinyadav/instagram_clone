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


def accept_friend_request(request, pk):
    print(pk)
    accept_request = FriendsRequest.objects.get(pk=pk)
    print(accept_request)
    accept_request.action = True
    accept_request.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # return redirect(request.META['HTTP_REFERER'])


def account_edit(request):
    return render(request, "user_profile/account_edit.html")