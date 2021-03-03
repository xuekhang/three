import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async

from .models import (Game, Config, Player, GlobalCategory, LocalCategory,
                     Round, CategoryInRound, Question, Answer, Vote)


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
                # todo: add backend start game logic here
                if await self.start_game(self.game_code) == 'success':
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

    @database_sync_to_async
    def start_game(self, game_code):
        game = Game.objects.get(code=game_code)
        config = Config.objects.get(game=game)
        players = Player.objects.filter(game=game)
        rounds = Round.objects.filter(game=game)

        for round in rounds:
            # this should delete the ansewrs too
            categories_in_round = CategoryInRound.objects.filter(round=round)
            for cat in categories_in_round:
                Question.objects.filter(category_in_round=cat).delete()

        for player in players:
            for round in rounds:
                categories_in_round = CategoryInRound.objects.filter(
                    round=round)
                for cat in categories_in_round:
                    Question.objects.create(player=player,
                                            category_in_round=cat)
        return 'success'


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
                    'startTimer': start_timer
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


class ReviewConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        game_code = self.scope['url_route']['kwargs']['game_code']
        self.game_code = game_code
        await self.channel_layer.group_add(game_code, self.channel_name)
        await self.send({"type": "websocket.accept"})

    async def websocket_receive(self, event):
        print('receive', event)
        front_text = event.get('text', None)
        if front_text is not None:
            loaded_dict_data = json.loads(front_text)
            vote = loaded_dict_data.get('vote')
            answer_id = loaded_dict_data.get('answerId')
            player_id = loaded_dict_data.get('playerId')
            print("vote:", vote, ", answerId:", answer_id, ", playerId:",
                  player_id)
            voting = await self.save_vote(vote, answer_id, player_id)
            print(voting)
            voteUpCount = await self.get_vote_count('up', answer_id)
            voteDownCount = await self.get_vote_count('down', answer_id)
            myResponse = {
                'answerId': answer_id,
                'voteUpCount': voteUpCount,
                'voteDownCount': voteDownCount
            }
            await self.channel_layer.group_send(self.game_code, {
                "type": "send_review_data",
                "text": json.dumps(myResponse)
            })

    @database_sync_to_async
    def save_vote(self, vote, answer_id, player_id):
        player = Player.objects.get(pk=player_id)
        answer = Answer.objects.get(pk=answer_id)
        #todo if already exist then update else create
        try:
            vote_obj = Vote.objects.get(player=player, answer=answer)
        except:
            Vote.objects.create(player=player, answer=answer, vote=vote)
            return 'vote created'
        else:
            vote_obj.vote = vote
            vote_obj.save()
            return 'vote updated'

    @database_sync_to_async
    def get_vote_count(self, vote, answer_id):
        answer = Answer.objects.get(pk=answer_id)
        return Vote.objects.filter(vote=vote, answer=answer_id).count()

    async def send_review_data(self, event):
        await self.send({'type': 'websocket.send', 'text': event['text']})
