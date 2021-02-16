from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse
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
        'title':'home'
        }   
    if request.method == 'POST':
        if 'join' in request.POST:
            game_code = request.POST.get('game_code')
            if game_code != '':
                return redirect('board', game_code, 1)
            else:
                messages.error(request, 'Game code does not exist')
                return redirect('home')
        if 'create' in request.POST:
            player_name = request.POST.get('player_name')
            if player_name == '':
                messages.warning(request,'Player name required')
                return redirect('home')
            game_code = get_random_string(length=6).upper()
            Game.objects.create(code=game_code)
            # game = Game(game_code)
            # game.save()
            game = Game.objects.get(code=game_code)
            
            # player = Player(
            #     game=game,
            #     name=player_name,
            #     is_host = True
            #     )
            # player.save()
            Player.objects.create(
                game=game,
                name=player_name,
                is_host = True
            )
            return redirect('config', game_code)
    else:
        form = ConfigForm()

        context = {
            'title':'home',
            'form': form
            }    
        return render(request, 'game/home.html', context)

def config(request, game_code=''):
    if request.method == 'POST':
        form = ConfigForm(request.POST)
        game_code = request.POST.get('game_code')
        game = Game.objects.get(code=game_code)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.game = game
            obj.save()
            messages.success(request, f'Game config saved')        
        all_letters = str(Config.objects.values_list('letters',flat=True).filter(game=game))
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
                game = game, 
                number = i, 
                letter = random.choice(letters)
                )
            round.save()
            for j in range(1, num_of_cat_per_round+1):
                categoryInRound = CategoryInRound(
                    name = random.choice(all_categories),
                    round = round
                    )
                categoryInRound.save()

        return redirect('board', game_code, 1)       
    
    # new_game_code = get_random_string(length=6).upper()
    # Game.objects.create(code=new_game_code)
    messages.success(request, f'Game created')
    form = ConfigForm(initial={
        'num_of_players' : 6, 
        'num_of_rounds' : 4,
        'num_of_cat_per_round' : 10
        })
    context = {
        'title':'config',
        'form':form,
        'game_code': game_code
        }
    return render(request, 'game/config.html', context)

def board(request, game_code='', round=''):
    try:
        Game.objects.get(code=game_code)        
    except:
        messages.error(request, f'Game code does not exist')
        return redirect('home')
    if game_code != '':
        if round != '':
            game = Game.objects.get(code=game_code)
            all_categories = sorted(GlobalCategory.objects.all(), key=lambda x: random.random())
            categories = all_categories[:10]
            all_letters = str(Config.objects.values_list('letters',flat=True)[0])
            letters = list(all_letters.split(","))

            context = {
                'title':'board',
                'game_code': game_code,
                'categories': categories,
                'letter' : random.choice(letters)
            }
        else:
            messages.warning(request, 'Game round does not exist')
            return redirect('home')
    
    return render(request, 'game/board.html', context)
