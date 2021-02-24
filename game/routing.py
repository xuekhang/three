from django.conf.urls import url
from django.urls import path

from .consumers import TestConsumer, LobbyConsumer
# routing for websockets
ws_urlpatterns = [
    path('',TestConsumer.as_asgi()),
    path('lobby/<game_code>/<player_name>/', LobbyConsumer.as_asgi()),
]