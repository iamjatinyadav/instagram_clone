from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import FormView
from django.urls import reverse_lazy
from user.models import *
from apps.user_profile.models import *
from .forms import *
from django.contrib.auth.decorators import *
from django.db.models import Exists, Q
from apps.post.models import *


# Create your views here.


@login_required()
def index(request):
    request_users = list(FriendsRequest.objects.filter(sender=request.user).values_list("receiver__email", flat=True))
    suggest_user = User.objects.exclude(email=request.user.email).exclude(email__in=request_users)
    post_show_users = list(FriendsRequest.objects.filter(action=True).filter(sender=request.user).
                           values_list("receiver__email", flat=True))
    posts = Post.objects.filter(Q(user__email__in=post_show_users) | Q(user__email=request.user))
    context = {'suggest_users': suggest_user, 'posts': posts}
    return render(request, "base/index.html", context)


@login_required()
def search(request):
    return render(request, "base/search.html")


@login_required()
def show_search_result(request):
    if request.method == "GET":
        query = request.GET["search"]
        if len(query) <= 1:
            all_users = User.objects.none()
        else:
            all_users = User.objects.filter(Q(userpersonal__uniquename__icontains=query) |
                                            Q(first_name__icontains=query))
        context = {"all_users": all_users}
        return render(request, "base/search.html", context)



@login_required()
def explore(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "base/explore.html", context)


@login_required()
def notifications(request):
    return render(request, "base/notifications.html")


def handle_login(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')

    return render(request, 'base/login.html')


class HandleRegister(FormView):
    template_name = 'base/signup.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = User.objects.create(email=form.cleaned_data['email'], first_name=form.cleaned_data['first_name'],
                                   last_name=form.cleaned_data['last_name'])
        userinfo = UserPersonalInfo.objects.create(user=user, uniquename=form.cleaned_data['uniquename'],
                                                   phone=form.cleaned_data['phone'])
        user.set_password(form.cleaned_data['password'])
        user.is_active = True
        user.save()
        userinfo.save()
        return super(HandleRegister, self).form_valid(form)


class HandleLogout(LogoutView):
    template_name = "base/index.html"

