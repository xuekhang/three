from django.contrib import admin
from .models import (
    Config, 
    Game, 
    Player,
    GlobalCategory,
    LocalCategory,
    Round,
    CategoryInRound,
    Question,
    Answer
    )

# Register your models here.
admin.site.register(Config)
admin.site.register(Game)
admin.site.register(Player)

admin.site.register(GlobalCategory)
admin.site.register(LocalCategory)
admin.site.register(Round)
admin.site.register(CategoryInRound)
admin.site.register(Question)
admin.site.register(Answer)