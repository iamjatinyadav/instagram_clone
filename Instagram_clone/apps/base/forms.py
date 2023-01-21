from django import forms
from django.contrib.auth import authenticate, login, get_user_model
from apps.user_profile.models import *
from user.models import *


class LoginForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(LoginForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ["email", "password"]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        user = authenticate(email=email, password=password)
        if not user:
            raise forms.ValidationError("this email does not exist...")
        if not user.check_password(password):
            raise forms.ValidationError("Invalid Password...")
        if not user.is_active:
            raise forms.ValidationError("this user no longer active..")
        return super(LoginForm, self).clean(*args, **kwargs)


class RegisterForm(forms.ModelForm):
    uniquename = forms.CharField(max_length=40)
    phone = forms.CharField(max_length=40)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'uniquename', 'phone']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get("password")
    #     confirm_password = cleaned_data.get("confirm_password")
    #     if password is not None and password != confirm_password:
    #         self.add_error("confirm_password", "Your passwords must match")
    #     return cleaned_data

    def clean(self):
        cleaned_data = super().clean()
        uniquename = cleaned_data.get("uniquename")
        phone = cleaned_data.get("phone")
        finduniquename = UserPersonalInfo.objects.filter(uniquename=uniquename)
        findphone = UserPersonalInfo.objects.filter(phone=phone)
        if finduniquename.exists():
            raise forms.ValidationError("username is taken")
        if findphone.exists():
            raise forms.ValidationError("phone no already register")

        return cleaned_data





