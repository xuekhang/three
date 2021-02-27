from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('config/', views.config, name='config'),
    path('config/<game_code>/', views.config, name='config'),
    path('config/<game_code>/<player_name>', views.config, name='config'),
    path('lobby/<game_code>/<player_name>/', views.lobby, name='lobby'),
    path('board/', views.board, name='board'),
    path('board/<game_code>/', views.board, name='board'),
    # path('board/<game_code>/<round>/', views.board, name='board'),
    path('board/<game_code>/<player_name>/<round_num>',
         views.board,
         name='board'),
    path('players_in_game/<game_code>/',
         views.get_players_in_game,
         name='players_in_game'),
    path('review/<game_code>/<player_name>/<round_num>/<question_num>',
         views.review,
         name='review'),
    path('startgame/<game_code>/<player_name>/',
         views.start_game,
         name='start_game')
]
