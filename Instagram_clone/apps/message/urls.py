from django.urls import path
from .views import *

urlpatterns = [
    path("direct/inbox/", inbox, name="inbox"),
    path("t/chat/", chat, name="personal_chat"),
]