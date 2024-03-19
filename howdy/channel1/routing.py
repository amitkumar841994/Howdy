from django.urls import path,include
from . import consumers

websocket_urlpatterns=[
    path('wc/sc/',consumers.ChatConsumer.as_asgi())

]