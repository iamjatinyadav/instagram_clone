from django.contrib import admin
from .models import *


@admin.register(FriendsRequest)
class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ['sender','receiver','action']


@admin.register(UserProfilePic)
class UserProfilePicAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']

