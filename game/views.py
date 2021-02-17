from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.core import serializers
from urllib.parse import urlencode
from .forms import ConfigForm
from .models import (
    Game,
    Config,
    Player,
    GlobalCategory,
    LocalCategory,
    Round,
    CategoryInRound
)
from django.utils.crypto import get_random_string
import random
import logging

# Create your views here.

def home(request):
    context = {
        'title': 'home'
    }
    if request.method == 'POST':
        player_name = request.POST.get('player_name')
        if player_name == '':
                messages.warning(request, 'Player name required')
                return redirect('home')
        game_code = request.POST.get('game_code')

        # logic for joining a game
        if 'join' in request.POST:
            game = Game.objects.get(code=game_code)
            num_current_players = Player.objects.filter(game=game).count()
            config = Config.objects.get(game=game)
            if num_current_players >= config.num_of_players:
                messages.warning(request, 'Game is full')
                return redirect('home')
            Player.objects.create(
                game=game,
                name=player_name,
                is_host=False
            )
            if game_code != '':
                return redirect('board', game_code, player_name, 1)
            else:
                messages.error(request, 'Game code does not exist')
                return redirect('home')

        # logic for creating a  game
        if 'create' in request.POST:            
            game_code = get_random_string(length=6).upper()
            Game.objects.create(code=game_code)
            game = Game.objects.get(code=game_code)
            Player.objects.create(
                game=game,
                name=player_name,
                is_host=True
            )
            return redirect('config', game_code, player_name)
    else:
        form = ConfigForm()

        context = {
            'title': 'home',
            'form': form
        }
        return render(request, 'game/home.html', context)


def config(request, game_code='', player_name=''):
    if request.method == 'POST':
        form = ConfigForm(request.POST)
        game_code = request.POST.get('game_code')
        game = Game.objects.get(code=game_code)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.game = game
            obj.save()
            messages.success(request, f'Game config saved')
        all_letters = str(Config.objects.values_list(
            'letters', flat=True).filter(game=game))
        letters = list(all_letters.split(","))

        all_categories = []
        global_categories = GlobalCategory.objects.all()
        for category in global_categories:
            all_categories.append(category.name)
        local_categories = LocalCategory.objects.filter(game=game)
        for category in local_categories:
            all_categories.append(category.name)

        num_of_rounds = int(request.POST.get('num_of_rounds'))
        num_of_cat_per_round = int(request.POST.get('num_of_cat_per_round'))
        for i in range(1, num_of_rounds+1):
            round = Round(
                game=game,
                number=i,
                letter=random.choice(letters)
            )
            round.save()
            for j in range(1, num_of_cat_per_round+1):
                categoryInRound = CategoryInRound(
                    name=random.choice(all_categories),
                    round=round
                )
                categoryInRound.save()

        return redirect('lobby', game_code, player_name)

    messages.success(request, f'Game created')
    form = ConfigForm(initial={
        'num_of_players': 6,
        'num_of_rounds': 4,
        'num_of_cat_per_round': 10
    })
    context = {
        'title': 'config',
        'form': form,
        'game_code': game_code
    }
    return render(request, 'game/config.html', context)


def board(request, game_code='', player_name='', round=''):
    try:
        Game.objects.get(code=game_code)
    except:
        messages.error(request, f'Game code does not exist')
        return redirect('home')
    if game_code != '':
        if round != '':
            game = Game.objects.get(code=game_code)
            
            all_categories = sorted(
                GlobalCategory.objects.all(), key=lambda x: random.random())
            categories = all_categories[:10]
            all_letters = str(Config.objects.values_list(
                'letters', flat=True)[0])
            letters = list(all_letters.split(","))

            max_rounds = Config.objects.get(game=game).num_of_rounds
            rounds = []
            for x in range(1,max_rounds + 1):
                rounds.append(x)

            # todo get the letter for each round
            
            context = {
                'title': 'board',
                'game_code': game_code,
                'player_name': player_name,
                'categories': categories,
                'rounds': rounds,
                'round' : round,
                'letter': random.choice(letters),
            }
        else:
            messages.warning(request, 'Game round does not exist')
            return redirect('home')

    return render(request, 'game/board.html', context)

def lobby(request, game_code='', player_name=''):
    game = Game.objects.get(code=game_code)
    context = {
        'title': 'Lobby',
        'players': Player.objects.filter(game=game)
    }

    if request.method == 'POST':
        return redirect('board', game_code, player_name, 1)
    return render(request, 'game/lobby.html', context)

def get_players_in_game(request, game_code):
    game = Game.objects.get(code=game_code)
    players = Player.objects.filter(game=game)
    players_json = serializers.serialize('json', players)
    # return JsonResponse(players_json, safe=False)
    return HttpResponse(players_json, content_type='application/json')
