from django.shortcuts import render
from django.http import HttpResponse
from .forms import ConfigForm
import random
import logging

# Create your views here.
def home(request):
    
    myList = [1,2]

    context = {
        'title':'home'}   

    if request.method == 'POST':
        return render(request, 'game/config.html', context)
    else:
        form = ConfigForm()

    context = {
        'title':'home',
        'form': form}    
    return render(request, 'game/home.html', context)

def config(request):
    context = {'title':'config'}
    return render(request, 'game/config.html', context)

def board(request):
    return render(request, 'game/board.html', {'title':'board'})