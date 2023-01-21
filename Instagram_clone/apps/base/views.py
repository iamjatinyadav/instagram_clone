from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import FormView
from django.urls import reverse_lazy
from user.models import *
from apps.user_profile.models import *
from .forms import *
# Create your views here.


def index(request):
    return render(request, "base/index.html")


def search(request):
    return render(request, "base/search.html")


def explore(request):
    return render(request, "base/explore.html")


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

