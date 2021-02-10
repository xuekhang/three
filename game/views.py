from django.shortcuts import render
from django.http import HttpResponse
import random
import logging

# Create your views here.
def home(request):
    context = {'title':'home'}
    myList = [1,2]

    if request.method == 'POST':
        return render(request, 'game/config.html', context)

    return render(request, 'game/home.html', context)

def config(request):
    context = {'title':'config'}
    return render(request, 'game/config.html', context)

def board(request):
    return render(request, 'game/board.html', {'title':'board'})