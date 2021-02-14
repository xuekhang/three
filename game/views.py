from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import ConfigForm
from .models import Game, Config, Player
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
        if form.is_valid():
            form.save()
            messages.success(request, f'Game created')
            return redirect('home')
    
    new_game_code = get_random_string(length=6)
    Game.objects.create(code=new_game_code)
    game = Game.objects.get(code=new_game_code)
    form = ConfigForm({'game_code':game})
    context = {
        'title':'config',
        'form':form}
    return render(request, 'game/config.html', context)

def board(request):
    return render(request, 'game/board.html', {'title':'board'})
