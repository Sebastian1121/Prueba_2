from django.contrib import admin

# Register your models here.

from . models import Genre, Juego

admin.site.register(Genre)
admin.site.register(Juego)

