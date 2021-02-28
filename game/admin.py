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


class ConfigAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Config._meta.get_fields()]


class GameAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Game._meta.get_fields()]


class PlayerAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Player._meta.get_fields()]
    list_display = ['id','name','game','is_host']


class GlobalCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in GlobalCategory._meta.get_fields()]


class LocalCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in LocalCategory._meta.get_fields()]


class RoundAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Round._meta.get_fields()]
    list_display = ['id','number','game','is_played']


class CategoryInRoundAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CategoryInRound._meta.get_fields()]


class QuestionAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Question._meta.get_fields()]
    list_display = ['id','player','category_in_round']


class AnswerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Answer._meta.get_fields()]


# Register your models here.
admin.site.register(Config, ConfigAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Player, PlayerAdmin)

admin.site.register(GlobalCategory, GlobalCategoryAdmin)
admin.site.register(LocalCategory, LocalCategoryAdmin)
admin.site.register(Round, RoundAdmin)
admin.site.register(CategoryInRound, CategoryInRoundAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
