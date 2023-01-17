from django.urls import path
from .views import *
urlpatterns = [
    path('', profile, name="profile"),
    path('saved/', user_saved, name="user-saved"),
    path('tagged/', user_tagged, name="user-tagged"),
]