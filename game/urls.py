
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
    path('board/', views.board, name='board'),    
    path('board/<game_code>/', views.board, name='board'),
    path('board/<game_code>/<round>/', views.board, name='board'),
    path('board/<game_code>/<round>/<player_name>', views.board, name='board')
]
