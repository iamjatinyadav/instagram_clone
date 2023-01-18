from django.urls import path
from .views import *
urlpatterns = [
    path("", index, name="home"),
    path("search/", search, name="search"),
    path("explore/", explore, name="explore"),
]