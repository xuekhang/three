from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import ConfigForm
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
    form = ConfigForm()

    context = {
        'title':'config',
        'form':form}
    return render(request, 'game/config.html', context)

def board(request):
    return render(request, 'game/board.html', {'title':'board'})
