from django.contrib import admin
from .models import Config, Game, Player

# Register your models here.
admin.site.register(Config)
admin.site.register(Game)
admin.site.register(Player)
