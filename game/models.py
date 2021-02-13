from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

class Game(models.Model):
    code = models.CharField(max_length=6)

class Config(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    num_of_player = models.IntegerField()
    letter = models.CharField(max_length=1)

class Player(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class Car(models.Model):
    name = models.CharField(max_length=20)
    color= models.CharField(max_length=2)
    def __str__(self):
        return self.name + '    ' + self.color

class Book(models.Model):
    BOOK_CHOICES = (
        ('A','A'),
        ('B','B'),
        ('C','C'),
        ('D','D')
    )
    title = MultiSelectField(choices=BOOK_CHOICES)
