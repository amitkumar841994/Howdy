from django.urls import path
from .views import *


urlpatterns = [
    path('contact/list/', CreateUser.as_view(), name='createuser'),


]