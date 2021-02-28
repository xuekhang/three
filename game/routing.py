from django.conf.urls import url
from django.urls import path

from .consumers import (TestConsumer, LobbyConsumer, BoardConsumer)
# routing for websockets
ws_urlpatterns = [
    path('', TestConsumer.as_asgi()),
    path('lobby/<game_code>/<player_name>/', LobbyConsumer.as_asgi()),
    path('board/<game_code>/<player_name>/<round_num>',
         BoardConsumer.as_asgi()),
]