from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']


@admin.register(UserSaved)
class UserSavedAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'post']
