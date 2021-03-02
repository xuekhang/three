from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.


class Game(models.Model):
    code = models.CharField(max_length=6)

    def __str__(self):
        return self.code


class Config(models.Model):
    letter_choices = (
        ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'),
        ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'),
        ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'),
        ('L', 'L'), ('M', 'M'), ('N', 'N'), ('O', 'O'),
        ('P', 'P'), ('Q', 'Q'), ('R', 'R'), ('S', 'S'),
        ('T', 'T'), ('U', 'U'), ('V', 'V'), ('W', 'W'),
        ('X', 'X'), ('Y', 'Y'), ('Z', 'Z')
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


class GlobalCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class LocalCategory(models.Model):
    game = models.OneToOneField(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Round(models.Model):
    number = models.IntegerField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    letter = models.CharField(max_length=3)
    is_played = models.BooleanField(default=False)

    def __str__(self):
        return str(self.game) + ' Round: ' + str(self.number)


class CategoryInRound(models.Model):
    name = models.CharField(max_length=100)
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    number = models.IntegerField()

    def __str__(self):
        return self.name


class Question(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    # round = models.ForeignKey(Round, on_delete=models.CASCADE)
    category_in_round = models.ForeignKey(CategoryInRound, on_delete=models.CASCADE)
    
    # answer = models.CharField(max_length=150)

    def __str__(self):
        # + ' Answer: ' + self.answer
        return ' Player: ' + str(self.player)


class Answer(models.Model):
    answer = models.CharField(max_length=150)
    question = models.OneToOneField(Question, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.question) + ' Ans: ' + self.answer


class Vote(models.Model):
    vote_choices = [
        ('up','up'),('down','down')
    ]
    vote = models.CharField(max_length=10,choices=vote_choices)
    player = models.ForeignKey(Player,on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.vote