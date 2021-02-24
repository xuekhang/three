# import asyncio
# import json
# from django.contrib.auth import get_user_model
# from channels.consumer import AsyncConsumer
# from channels.db import database_sync_to_async

# from .models import (
#     Game,
#     Config,
#     Player,
#     GlobalCategory,
#     LocalCategory,
#     Round,
#     CategoryInRound,
#     Question,
#     Answer
# )

# class TestConsumer(AsyncConsumer):
#     async def websocket_connect(self, event):
#         print("connected", event)
    
#     async def websocket_receive(self, event):
#         print("receieved", event)
    
#     async def websocket_disconnect(self, event):
#         print("disconnected", event)