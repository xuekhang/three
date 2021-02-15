from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

class Game(models.Model):
    code = models.CharField(max_length=6)
    def __str__(self):
        return self.code

class Config(models.Model):
    letter_choices = (
        ('A','A'), ('B','B'), ('C','C'), ('D','D'),
        ('D','D'), ('E','E'), ('F','F'), ('G','G'),
        ('H','H'), ('I','I'), ('J','J'), ('K','K'),
        ('L','L'), ('M','M'), ('N','N'), ('O','O'),
        ('P','P'), ('Q','Q'), ('R','R'), ('S','S'),
        ('T','T'), ('U','U'), ('V','V'), ('W','W'),
        ('X','X'), ('Y','Y'), ('Z','Z')
    )
    game = models.OneToOneField(Game, on_delete=models.CASCADE)
    num_of_players = models.IntegerField()
    num_of_rounds = models.IntegerField()
    num_of_cat_per_round = models.IntegerField()
    letters = MultiSelectField(choices=letter_choices)
    def __str__(self):
        return self.game.code + '   ' + str(self.num_of_players)

class Player(models.Model):    
    name = models.CharField(max_length=100)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    is_host = models.BooleanField()
    def __str__(self):
        return self.name
class Global_Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Local_Category(models.Model):
    game = models.OneToOneField(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)