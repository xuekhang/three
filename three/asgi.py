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

# from ..game.consumers import TestConsumer



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'three.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application()
    # 'websocket'
})


