from django.db import models

# Create your models here.

class Game(models.Model):
    code = models.CharField(max_length=6)

class Config(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    num_of_player = models.IntegerField()

class Player(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


