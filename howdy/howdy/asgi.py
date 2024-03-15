"""
ASGI config for howdy project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
import channel1.routing



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'howdy.settings')

# application1 = get_asgi_application()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket":URLRouter(
        channel1.routing.websocket_urlpatterns
    )
    # Just HTTP for now. (We can add other protocols later.)
})
