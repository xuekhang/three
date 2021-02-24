from django.conf.urls import url
from django.urls import path

from three.game.consumers import TestConsumer
# routing for websockets
ws_urlpatterns = [
    path('ws/some_url',TestConsumer.as_asgi())
]