from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ConfigForm, CarAdminForm
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
    
    form = ConfigForm()

    context = {
        'title':'config',
        'form':form}
    return render(request, 'game/config.html', context)

def board(request):
    return render(request, 'game/board.html', {'title':'board'})

def car(request):
    form = CarAdminForm()
    context = {
        'title':'car test',
        'form': form
    }
    return render(request, 'game/car.html', context)