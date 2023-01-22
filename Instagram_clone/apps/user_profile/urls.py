from django.urls import path
from .views import *


urlpatterns = [
    path('', profile, name='profile'),
    path('<user>/', profile, name="profile"),
    path('saved/', user_saved, name="user-saved"),
    # path('<user>/saved/', user_saved, name="user-saved"),
    path('tagged/', user_tagged, name="user-tagged"),
    path('friend-requests/', friendrequest, name="friendrequests"),
]