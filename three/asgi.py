"""
ASGI config for three project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from django.urls import path
from channels.routing import ProtocolTypeRouter , URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

# from three.game.consumers import TestConsumer
# from . import routing
# from three.game.routing import ws_urlpatterns
from game.routing import ws_urlpatterns


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'three.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(ws_urlpatterns)
        )
    )
})


