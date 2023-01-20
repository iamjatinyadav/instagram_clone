from django.urls import path
from .views import *


urlpatterns = [
    path("", index, name="home"),
    path("search/", search, name="search"),
    path("explore/", explore, name="explore"),
    path("notifications/", notifications, name="notifications"),
    path("login/", HandleLogin.as_view(), name="login"),
    path("logout/", HandleLogout.as_view(), name="logout"),
    path("signup/", signup, name="signup"),
]