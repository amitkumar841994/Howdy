from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('channel1/',include('channel1.urls')),
    # path('auth/api/',include('auth.urls'))


]
