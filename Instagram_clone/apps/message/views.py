from django.shortcuts import render
from django.contrib.auth.decorators import *

# Create your views here.

# @login_required()
def inbox(request):
    return render(request, "message/inbox.html")
