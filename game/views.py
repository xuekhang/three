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
    Round, 
    CategoryInRound
    )
from django.utils.crypto import get_random_string
import random
import logging

# Create your views here.
def home(request):    
    myList = [1,2]
    context = {
        'title':'home'}   
    if request.method == 'POST':
        game_code = request.POST.get('game_code')
        if game_code != '':
            return redirect('board', game_code)
        else:
            return redirect('home')
    else:
        form = ConfigForm()

        context = {
            'title':'home',
            'form': form}    
        return render(request, 'game/home.html', context)

def config(request):
    if request.method == 'POST':
        form = ConfigForm(request.POST)
        game_code = request.POST.get('game_code')
        game = Game.objects.get(code=game_code)

        # todo: create the rounds
        num_of_rounds = int(request.POST.get('num_of_rounds'))
        for x in range(1,num_of_rounds+1):
            round = Round(game=game, number=x)
            round.save()
        # todo: create the categories per round

        if form.is_valid():
            obj = form.save(commit=False)
            obj.game = game
            obj.save()
            messages.success(request, f'Game created')
            return redirect('board', game_code)
    
    new_game_code = get_random_string(length=6).upper()
    Game.objects.create(code=new_game_code)
    form = ConfigForm(initial={
        'num_of_players' : 6, 
        'num_of_rounds' : 4,
        'num_of_cat_per_round' : 10
        })
    context = {
        'title':'config',
        'form':form,
        'game_code': new_game_code
        }
    return render(request, 'game/config.html', context)

def board(request, game_code=''):
    # if game_code=='':
    #     game_code = request.GET.get('game_code')
    #     redirect('board', game_code)
    # if request.method == 'POST':
    #     redirect('www.google.com')
    try:
        Game.objects.get(code=game_code)        
    except:
        return redirect('home')
    if game_code != '':
        game = Game.objects.get(code=game_code)
        all_categories = sorted(GlobalCategory.objects.all(), key=lambda x: random.random())
        categories = all_categories[:10]
        all_letters = Config.objects.values_list('letters',flat=True)[0]
        test = str(all_letters)
        letters = list(test.split(","))

        context = {
            'title':'board',
            'game_code': game_code,
            'categories': categories,
            'letter' : random.choice(letters)
        }
    
    return render(request, 'game/board.html', context)
