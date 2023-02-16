from django.urls import path
from .views import *


urlpatterns = [
    path("", index, name="home"),
    path("search/", search, name="search"),
    path("show_result/", show_search_result, name="show-result"),
    path("delete_one_recent/<str:value>/", delete_one_recent, name="delete-one-recent"),
    path("delete_all_recent/", delete_all_recent, name="delete-all-recent"),
    path("explore/", explore, name="explore"),
    path("notifications/", notifications, name="notifications"),
    path("login/", handle_login, name="login"),
    path("logout/", HandleLogout.as_view(), name="logout"),
    path("signup/", HandleRegister.as_view(), name="signup"),
]