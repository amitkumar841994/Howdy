from django.urls import path
from . import views


urlpatterns = [
path('register',views.signup),
path('verify',views.verify),
path('index',views.index)

]