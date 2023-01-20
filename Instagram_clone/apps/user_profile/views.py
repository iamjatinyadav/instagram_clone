from django.shortcuts import render

# Create your views here.


def profile(request):
    context = {"value": "profile"}
    return render(request, "user_profile/profile.html", context)


def user_saved(request):
    context = {"value": "user_saved"}
    return render(request, "user_profile/profile.html", context)


def user_tagged(request):
    context = {"value": "user_tagged"}
    return render(request, "user_profile/profile.html", context)


def friendrequest(request):
    return render(request, "user_profile/friendrequests.html")
