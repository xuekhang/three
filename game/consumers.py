import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async

from .models import (
    Game,
    Config,
    Player,
    GlobalCategory,
    LocalCategory,
    Round,
    CategoryInRound,
    Question,
    Answer
)

class TestConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)
        await self.send({
            "type":"websocket.accept"
        })
        other_user = "other user"
        me = "me"
        print(other_user,me)

        # await asyncio.sleep(5)
        await self.send({
            "type": "websocket.send",
            "text": "hello word"
        })
    
    async def websocket_receive(self, event):
        print("receieved", event)
    
    async def websocket_disconnect(self, event):
        print("disconnected", event)
        await self.send({
            "type": "websocket.close"
        })
