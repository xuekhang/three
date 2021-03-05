from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.core import serializers
from urllib.parse import urlencode
from .forms import ConfigForm
from .models import (Game, Config, Player, GlobalCategory, LocalCategory,
                     Round, CategoryInRound, Question, Answer, Vote)
from django.utils.crypto import get_random_string
import random
import logging
import json

# Create your views here.


def home(request):
    context = {'title': 'home'}
    if request.method == 'POST':
        player_name = request.POST.get('player_name')
        if player_name == '':
            messages.warning(request, 'Player name required')
            return redirect('home')
        game_code = request.POST.get('game_code')

        # logic for joining a game
        if 'join' in request.POST:
            try:
                game = Game.objects.get(code=game_code)
            except:
                messages.error(request, 'Game code does not exist')
                return redirect('home')
            num_current_players = Player.objects.filter(game=game).count()
            config = Config.objects.get(game=game)

            if num_current_players >= config.num_of_players:
                messages.warning(request, 'Game is full')
                return redirect('home')
            Player.objects.create(game=game, name=player_name, is_host=False)
            if game_code != '':
                return redirect('lobby', game_code, player_name)
                # return redirect('board', game_code, player_name, 1)
            else:
                messages.error(request, 'Game code does not exist')
                return redirect('home')

        # logic for creating a  game
        if 'create' in request.POST:
            game_code = get_random_string(length=6).upper()
            Game.objects.create(code=game_code)
            game = Game.objects.get(code=game_code)
            # create game with defualt settings
            Config.objects.create(game=game,
                              num_of_players=6,
                              num_of_rounds=4,
                              num_of_cat_per_round=10)
            Player.objects.create(game=game, name=player_name, is_host=True)

            return redirect('config', game_code, player_name)
    else:
        form = ConfigForm()

        context = {'title': 'home', 'form': form}
    return render(request, 'game/home.html', context)


def config(request, game_code='', player_name=''):
    if request.method == 'POST':
        
        game_code = request.POST.get('game_code')
        
        game = Game.objects.get(code=game_code)
        config = Config.objects.get(game=game)
        form = ConfigForm(request.POST, instance=config)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.game = game
            obj.save()
            messages.success(request, f'Game config saved')

        letters = list(
            Config.objects.values_list('letters', flat=True).filter(game=game))

        all_categories = []
        global_categories = GlobalCategory.objects.all()
        for category in global_categories:
            all_categories.append(category.name)
        local_categories = LocalCategory.objects.filter(game=game)
        for category in local_categories:
            all_categories.append(category.name)

        num_of_rounds = int(request.POST.get('num_of_rounds'))
        num_of_cat_per_round = int(request.POST.get('num_of_cat_per_round'))
        config = Config.objects.get(game=game)

        for i in range(1, num_of_rounds + 1):
            round = Round(game=game,
                          number=i,
                          letter=random.choice(letters[0]))
            round.save()
            for j in range(1, num_of_cat_per_round + 1):
                CategoryInRound.objects.create(
                    name=random.choice(all_categories), round=round, number=j)

        return redirect('lobby', game_code, player_name)

    messages.success(request, f'Game created')
    form = ConfigForm(initial={
        'num_of_players': 6,
        'num_of_rounds': 4,
        'num_of_cat_per_round': 10
    })
    context = {'title': 'config', 'form': form, 'game_code': game_code}
    return render(request, 'game/config.html', context)


def board(request, game_code='', player_name='', round_num=''):
    if request.method == 'POST':
        game = Game.objects.get(code=game_code)
        
        round = Round.objects.get(game=game, number=round_num)
        player = Player.objects.get(game=game, name=player_name)
        for key, value in request.POST.items():
            if str(key).startswith('answer'):
                answer = value
                # gets the number of the answer
                answer_number = str(key).replace('answer', '')
                cat_in_round = CategoryInRound.objects.get(
                    round=round, number=answer_number)

                question = Question.objects.get(player=player,
                                                category_in_round=cat_in_round)

                Answer.objects.create(answer=value, question=question)

        return redirect('review', game_code, player_name, round_num)

    try:
        Game.objects.get(code=game_code)
    except:
        messages.error(request, f'Game code does not exist')
        return redirect('home')
    if game_code != '':
        if round_num != '':
            game = Game.objects.get(code=game_code)
            round = Round.objects.get(game=game, number=round_num)
            all_letters = str(
                Config.objects.values_list('letters', flat=True)[0])
            letters = list(all_letters.split(","))

            max_rounds = Config.objects.get(game=game).num_of_rounds
            rounds = []
            for x in range(1, max_rounds + 1):
                rounds.append(x)

            current_round = Round.objects.get(game=game, number=round_num)
            categories_in_round = list(
                CategoryInRound.objects.filter(round=current_round))
            categories = []

            for category in categories_in_round:
                categories.append(category.name)
            player = Player.objects.get(game=game, name=player_name)

            context = {
                'title': 'board',
                'game_code': game_code,
                'player_name': player_name,
                'categories': categories,
                'rounds': rounds,
                'round': round_num,
                'letter': round.letter,
                'round_is_played': current_round.is_played,
                'is_player_host': player.is_host
            }
        else:
            messages.warning(request, 'Game round does not exist')
            return redirect('home')

    return render(request, 'game/board.html', context)


def lobby(request, game_code='', player_name=''):
    game = Game.objects.get(code=game_code)
    player = Player.objects.get(game=game, name=player_name)
    context = {
        'title': 'Lobby',
        'players': Player.objects.filter(game=game),
        'is_player_host': player.is_host
    }

    return render(request, 'game/lobby.html', context)


def review(request, game_code='', player_name='', round_num=''):
    if request.method == 'POST':
        return redirect('result', game_code, player_name, round_num)
    game = Game.objects.get(code=game_code)
    max_rounds = Config.objects.get(game=game).num_of_rounds
    rounds = []
    for x in range(1, max_rounds + 1):
        rounds.append(x)
    round = Round.objects.get(game=game, number=round_num)
    categories_in_round = CategoryInRound.objects.filter(round=round)

    answers = []
    for cat in categories_in_round:
        questions = Question.objects.filter(category_in_round=cat)
        player_answers = []
        for q in questions:
            answer = Answer.objects.filter(question=q)
            player_answers.append([answer])
        answers.append([cat, player_answers])

    context = {
        'title': 'Review',
        'game_code': game_code,
        'cat_in_round': categories_in_round,
        'rounds': rounds,
        'round': round_num,
        'answers': answers,
        'player': Player.objects.get(game=game, name=player_name),
        'letter': round.letter,
    }

    return render(request, 'game/review.html', context)


def get_players_in_game(request, game_code):
    game = Game.objects.get(code=game_code)
    players = Player.objects.filter(game=game)
    players_json = serializers.serialize('json', players)
    # return JsonResponse(players_json, safe=False)
    return HttpResponse(players_json, content_type='application/json')


def start_game(request, game_code, player_name):
    game = Game.objects.get(code=game_code)
    config = Config.objects.get(game=game)
    players = Player.objects.filter(game=game)
    rounds = Round.objects.filter(game=game)

    for round in rounds:
        # this should delete the ansewrs too
        categories_in_round = CategoryInRound.objects.filter(round=round)
        for cat in categories_in_round:
            Question.objects.filter(category_in_round=cat).delete()

    for player in players:
        for round in rounds:
            categories_in_round = CategoryInRound.objects.filter(round=round)
            for cat in categories_in_round:
                Question.objects.create(player=player, category_in_round=cat)

    return HttpResponse('success', content_type='application/json')


def result(request, game_code, player_name, round_num):
    if request.method == 'POST':
        return redirect('board', game_code, player_name, int(round_num) + 1)

    game = Game.objects.get(code=game_code)
    players = Player.objects.filter(game=game)
    results = []
    for player in players:
        points = 0
        questions = Question.objects.filter(player=player)
        for q in questions:
            try:
                answer = Answer.objects.get(question=q)
                votes_up = Vote.objects.filter(vote='up',
                                               answer=answer).count()
                votes_down = Vote.objects.filter(vote='down',
                                                 answer=answer).count()
                if votes_up > votes_down and answer.answer != '':
                    points += 1
            except:
                print('cannot find answer')
        results.append([player, points])
    # sort the list based on the points of the players
    def takeSecond(elem):
        return elem[1]

    results.sort(key=takeSecond, reverse=True)

    context = {
        'title': 'Results',
        'player_name': player_name,
        'game_code': game_code,
        'results': results
    }
    return render(request, 'game/result.html', context)