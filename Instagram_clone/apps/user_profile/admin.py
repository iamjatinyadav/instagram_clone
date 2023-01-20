from django.contrib import admin
from user.admin import CustomUserAdmin
# Register your models here.
from .models import UserPersonalInfo
from django.utils.translation import gettext_lazy as _


class UserPersonalInfoAdmin(CustomUserAdmin):
    fieldsets = (
        (_('More Personal info'), {'fields': ('username', 'phone')}),
    )



