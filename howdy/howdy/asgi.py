"""
ASGI config for howdy project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter,URLRouter

from django.core.asgi import get_asgi_application
import channel1.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'howdy.settings')

application = get_asgi_application()

application = ProtocolTypeRouter({
    "http": application,
    "websocket":URLRouter(
        channel1.routing.wesocket_urlpatterns
    )
    # Just HTTP for now. (We can add other protocols later.)
})
