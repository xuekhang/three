from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'game/home.html', {'title':'home'})

def config(request):
    return render(request, 'game/config.html', {'title':'config'})

def board(request):
    return render(request, 'game/board.html', {'title':'board'})