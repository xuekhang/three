from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.core import serializers
from urllib.parse import urlencode
from .forms import ConfigForm
from .models import (
    Game,
    Config,
    Player,
    GlobalCategory,
    LocalCategory,
    Round,
    CategoryInRound,
    Question,
    Answer
)
from django.utils.crypto import get_random_string
import random
import logging

# Create your views here.


def home(request):
    context = {
        'title': 'home'
    }
    if request.method == 'POST':
        player_name = request.POST.get('player_name')
        if player_name == '':
            messages.warning(request, 'Player name required')
            return redirect('home')
        game_code = request.POST.get('game_code')

        # logic for joining a game
        if 'join' in request.POST:
            game = Game.objects.get(code=game_code)
            num_current_players = Player.objects.filter(game=game).count()
            config = Config.objects.get(game=game)

            if num_current_players >= config.num_of_players:
                messages.warning(request, 'Game is full')
                return redirect('home')
            Player.objects.create(
                game=game,
                name=player_name,
                is_host=False
            )

            # todo create questions for players
            # for x in range(1, config.num_of_rounds + 1):
            #     Question.objects.create(
            #         number=x,
            #         round=Round.objects.get(game=game, number=x),
            #         player=Player.objects.get(name=player_name)
            #     )

            if game_code != '':
                # return redirect('lobby', game_code, player_name)
                return redirect('board', game_code, player_name, 1)
            else:
                messages.error(request, 'Game code does not exist')
                return redirect('home')

        # logic for creating a  game
        if 'create' in request.POST:
            game_code = get_random_string(length=6).upper()
            Game.objects.create(code=game_code)
            game = Game.objects.get(code=game_code)
            Player.objects.create(
                game=game,
                name=player_name,
                is_host=True
            )

            return redirect('config', game_code, player_name)
    else:
        form = ConfigForm()

        context = {
            'title': 'home',
            'form': form
        }
        return render(request, 'game/home.html', context)


def config(request, game_code='', player_name=''):
    if request.method == 'POST':
        form = ConfigForm(request.POST)
        game_code = request.POST.get('game_code')
        game = Game.objects.get(code=game_code)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.game = game
            obj.save()
            messages.success(request, f'Game config saved')
        all_letters = str(Config.objects.values_list(
            'letters', flat=True).filter(game=game))
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
        config = Config.objects.get(game=game)

        for i in range(1, num_of_rounds+1):
            round = Round(
                game=game,
                number=i,
                letter=random.choice(letters)
            )
            round.save()
            for j in range(1, num_of_cat_per_round+1):
                categoryInRound = CategoryInRound(
                    name=random.choice(all_categories),
                    round=round
                )
                categoryInRound.save()
                # Question.objects.create(
                #     number=j,
                #     round=Round.objects.get(game=game, number=i),
                #     player=Player.objects.get(name=player_name, game=game)
                # )

        # todo add host to answer table

        # for x in range(1, config.num_of_rounds + 1):
        #     Question.objects.create(
        #         number=x,
        #         round=Round.objects.get(game=game, number=x),
        #         player=Player.objects.get(name=player_name,game=game)
        #     )

        return redirect('lobby', game_code, player_name)
        

    messages.success(request, f'Game created')
    form = ConfigForm(initial={
        'num_of_players': 6,
        'num_of_rounds': 4,
        'num_of_cat_per_round': 10
    })
    context = {
        'title': 'config',
        'form': form,
        'game_code': game_code
    }
    return render(request, 'game/config.html', context)


def board(request, game_code='', player_name='', round_num=''):
    # todo record submitted answers and send to next page
    if request.method == 'POST':
        # answers = list(request.POST.items())
        # answers = []
        game = Game.objects.get(code=game_code)
        round = Round.objects.get(game=game, number=round_num)
        player = Player.objects.get(game=game, name=player_name)
        for key, value in request.POST.items():
            if str(key).startswith('answer'):
                answer = value
                # gets the number of the answer
                answer_number = str(key).replace('answer', '')

                question = Question.objects.get(number=int(
                    answer_number), round=round, player=player)
                Answer.objects.create(answer=value, question=question)

        return redirect('review', game_code, player_name, round_num, 1)

    try:
        Game.objects.get(code=game_code)
    except:
        messages.error(request, f'Game code does not exist')
        return redirect('home')
    if game_code != '':
        if round_num != '':
            game = Game.objects.get(code=game_code)
            all_letters = str(Config.objects.values_list(
                'letters', flat=True)[0])
            letters = list(all_letters.split(","))

            max_rounds = Config.objects.get(game=game).num_of_rounds
            rounds = []
            for x in range(1, max_rounds + 1):
                rounds.append(x)

            # todo get the letter for each round
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
                'letter': random.choice(letters),
                'round_is_played': current_round.is_played,
                'is_player_host': player.is_host
            }
        else:
            messages.warning(request, 'Game round does not exist')
            return redirect('home')

    return render(request, 'game/board.html', context)


def lobby(request, game_code='', player_name=''):
    game = Game.objects.get(code=game_code)
    context = {
        'title': 'Lobby',
        'players': Player.objects.filter(game=game)
    }

    if request.method == 'POST':
        # todo: put logic to create player answers here
        game = Game.objects.get(code=game_code)
        players = Player.objects.filter(game=game)
        config = Config.objects.get(game=game)
        for player in players:
            for i in range(1, config.num_of_rounds +1):
                for j in range(1, config.num_of_cat_per_round +1):
                    Question.objects.create(number=j, round=Round.objects.get(game=game, number=i),player=player)


        # Question.objects.create(
        #     number=j,
        #     round=Round.objects.get(game=game, number=i),
        #     player=Player.objects.get(name=player_name, game=game)
        # )


        return redirect('board', game_code, player_name, 1)
    return render(request, 'game/lobby.html', context)


def review(request, game_code='', player_name='', round_num='', question_num=''):
    if request.method == 'POST':
        return redirect('board',game_code, player_name, int(round_num)+1)
    game = Game.objects.get(code=game_code)
    round = Round.objects.get(game=game,number=round_num)
    questions = Question.objects.filter(number=question_num,round=round)
    # answer = Answer.objects.filter()
    # answers = ['agfdg','bdfbb','bbgb','dbgbg','dfe','dbgbrfrvrg','dvrvbgbg','dbgrbg','drbgbg']
    answers = []
    for question in questions:
        try:
            player_answer = Answer.objects.get(question=question)
            answers.append(player_answer.answer)
        except:
            answers.append('    ')
            ## someone hasn't entered there answers.        
        
    context = {
        'title': 'Review',
        'game_code': game_code,
        'answers':answers
    }

    # todo: get all the answers for this round number and present to
    return render(request, 'game/review.html', context)


def get_players_in_game(request, game_code):
    game = Game.objects.get(code=game_code)
    players = Player.objects.filter(game=game)
    players_json = serializers.serialize('json', players)
    # return JsonResponse(players_json, safe=False)
    return HttpResponse(players_json, content_type='application/json')
