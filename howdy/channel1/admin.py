from django.contrib import admin

from .models import *

admin.site.register(Contact)
admin.site.register(UserProfile)
admin.site.register(Message)
admin.site.register(UserOtp)