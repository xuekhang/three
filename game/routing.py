from django.conf.urls import url
from django.urls import path

from .consumers import TestConsumer
# routing for websockets
ws_urlpatterns = [
    path('',TestConsumer.as_asgi())
]