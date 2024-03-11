from django.urls import path,include
from . import consumers

websocket_urlpatterns=[
    path('wc/sc/',consumers.MysyncConsumer.as_asgi())

]