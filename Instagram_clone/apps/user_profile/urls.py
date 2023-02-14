from django.urls import path
from .views import *


urlpatterns = [
    path('<str:user>/', profile, name="profile"),
    path('<str:user>/saved/', user_saved, name="user-saved"),
    path('<str:user>/saved/allsaved/', user_saved_all, name="user-saved-all"),
    path('<str:user>/tagged/', user_tagged, name="user-tagged"),
    path('<user>/friend-requests/', friendrequest, name="friend-requests"),
    path('requests/<int:pk>/', accept_friend_request, name="accept-requests"),
    path('send_request/<str:receiver>/', send_friend_request, name="send-requests"),
    path('account/edit/', account_edit, name="account-edit"),
    path('account/edit/change_profile_pic/', change_profile_picture, name="change_profile"),
    path('change_password/', change_password, name="change_password"),

]