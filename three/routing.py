from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.securitywebsocket import AllowedHostsOriginValidator, OriginValidator
from django.urls import path

from game.consumers import TestConsumer
# routing for websockets
ws_urlpatterns = [
    # path('ws/some_url',TestConsumer.as_asgi())
]