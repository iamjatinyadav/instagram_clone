from django.shortcuts import render, redirect
from user.models import *
from django.contrib.auth.decorators import *
from .models import *
from django.http import HttpResponseRedirect

# Create your views here.


@login_required()
def profile(request, user):
    user = User.objects.filter(userpersonal__uniquename=user)
    context = {"username": user}
    return render(request, "user_profile/userpost.html", context)


@login_required()
def user_saved(request, user):
    user = User.objects.filter(userpersonal__uniquename=user)
    context = {"username": user}
    return render(request, "user_profile/usersaved.html", context)


@login_required()
def user_tagged(request, user):
    user = User.objects.filter(userpersonal__uniquename=user)
    context = {"username": user}
    return render(request, "user_profile/usertagged.html", context)


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
    receiver = User.objects.get(email=receiver)
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
    return render(request, "user_profile/account.html")


@login_required()
def change_profile_picture(request):

    if request.method == 'POST':
        image = request.FILES.get('profile_pic')
        update_value = {"profile_pic": image}
        obj, created = UserProfilePic.objects.update_or_create(user=request.user, defaults=update_value)
        print("data successfully edit or update")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required()
def change_password(request):
    value = 0
    context = {"abc": value}
    return render(request, "user_profile/account.html", context)

