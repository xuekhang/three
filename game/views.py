from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse
from urllib.parse import urlencode
from .forms import ConfigForm
from .models import Game, Config, Player, Category
from django.utils.crypto import get_random_string
import random
import logging

# Create your views here.
def home(request):    
    myList = [1,2]
    context = {
        'title':'home'}   
    if request.method == 'POST':
        return redirect('config')
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
        test = request.POST.get('letters')

        if form.is_valid():
            obj = form.save(commit=False)
            obj.game_code = game
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
    try:
        Game.objects.get(code=game_code)        
    except:
        return redirect('home')
    if game_code != '':
        game = Game.objects.get(code=game_code)
        # all_categories = Category.objects.all()
        # x = [1,2,3,4]
        # random.shuffle(x)
        all_categories = sorted(Category.objects.all(), key=lambda x: random.random())
        categories = all_categories[:10]

        context = {
            'title':'board',
            'game_code': game_code,
            'categories': categories
        }
    
    return render(request, 'game/board.html', context)
