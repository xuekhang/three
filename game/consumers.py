import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async

from .models import (Game, Config, Player, GlobalCategory, LocalCategory,
                     Round, CategoryInRound, Question, Answer)


class TestConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)

        other_user = "other user"
        me = "me"
        # print(other_user,me)
        room = "thread_1"
        self.room = room
        await self.channel_layer.group_add(room, self.channel_name)

        await self.send({"type": "websocket.accept"})

        # await asyncio.sleep(5)

    async def websocket_receive(self, event):
        print("receieved", event)
        front_text = event.get('text', None)
        if front_text is not None:
            loaded_dict_data = json.loads(front_text)
            msg = loaded_dict_data.get('message')
            print(msg)
            myResponse = {'message': msg, 'username': 'jimmy'}

            # new_event = {
            # "type": "websocket.send",
            # "text": json.dumps(myResponse)
            # }
            await self.channel_layer.group_send(self.room, {
                "type": "chat_message",
                "text": json.dumps(myResponse)
            })
            # await self.send()

    async def chat_message(self, event):
        # print('message', event)
        # sends actual message
        await self.send({"type": "websocket.send", "text": event['text']})

    async def websocket_disconnect(self, event):
        print("disconnected", event)
        await self.send({"type": "websocket.close"})


class LobbyConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('connected', event)
        game_code = self.scope['url_route']['kwargs']['game_code']
        self.game_code = game_code
        await self.channel_layer.group_add(game_code, self.channel_name)

        await self.send({"type": "websocket.accept"})

        # game = Game.objects.get(code=game_code)
        # players = Player.objects.filter(game=game)
        players_obj = await self.get_players(game_code=game_code)
        players_list = []
        start_game = False
        for player in players_obj:
            players_list.append(player.name)
            print(player)
        self.players_list = players_list
        response = {'player_list': players_list, 'start_game': start_game}

        await self.channel_layer.group_send(game_code, {
            'type': 'send_lobby_data',
            'text': json.dumps(response)
        })
        # await self.send({'type': 'websocket.send', 'text': json.dumps(players_list)})

    async def send_lobby_data(self, event):
        await self.send({"type": "websocket.send", "text": event['text']})

    async def websocket_receive(self, event):
        print('receieved', event)
        # self.game_code
        print('game code', self.game_code)
        front_text = event.get('text', None)
        print(front_text)
        if front_text is not None:
            loaded_dict_data = json.loads(front_text)
            start_game = loaded_dict_data.get('start_game')
            print(start_game)
            if start_game == True:
                print('starting da game')
                # await self.channel_layer.group_send
                response = {
                    'player_list': self.players_list,
                    'start_game': start_game
                }
                await self.channel_layer.group_send(
                    self.game_code, {
                        'type': 'send_lobby_data',
                        'text': json.dumps(response)
                    })

    async def websocket_disconnect(Self, event):
        print('disconnect', event)

    @database_sync_to_async  # can't return queryset when using this decorator
    def get_players(self, game_code):
        game = Game.objects.get(code=game_code)
        # players = Player.objects.filter(game=game)[0]
        return list(Player.objects.filter(game=game))


class BoardConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        game_code = self.scope['url_route']['kwargs']['game_code']
        self.game_code = game_code
        await self.channel_layer.group_add(game_code, self.channel_name)
        await self.send({"type": "websocket.accept"})

    async def websocket_receive(self, event):
        # todo accept a start message from client and
        # send start to everyone
        print('testing')
        front_text = event.get('text', None)
        print('received', event)
        if front_text is not None:
            loaded_dict_data = json.loads(front_text)
            start_timer = loaded_dict_data.get('start_timer')

            if start_timer == True:
                print('starting da timer')
                response = {
                    # 'player_list': self.players_list,
                    'start_timer': start_timer
                }
                await self.channel_layer.group_send(
                    self.game_code, {
                        'type': 'send_board_data',
                        'text': json.dumps(response)
                    })
    async def websocket_disconnect(self, event):
        print('disconnect', event)

    async def send_board_data(self, event):
        await self.send({"type": "websocket.send", "text": event['text']})
