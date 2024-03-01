from django.urls import path,include
from . import consumers

wesocket_urlpatterns=[
    path('/wc/sc',consumers.SyncConsumer.as_asgi())

]