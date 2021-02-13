from django.contrib import admin
from .models import Config, Game, Player, Car, Book
from .forms import CarAdminForm

# Register your models here.
admin.site.register(Config)
admin.site.register(Game)
admin.site.register(Player)

class CarAdmin(admin.ModelAdmin):
    form = CarAdminForm

admin.site.register(Car, CarAdmin)

admin.site.register(Book)