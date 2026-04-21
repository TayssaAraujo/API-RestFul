from django.contrib import admin
from myflix.models import User, Stream, Lista

class Users(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular')
    list_display_links = ('id', 'nome')
    list_per_page = 20
    search_fields = ('nome',)

admin.site.register(User, Users)

class Streams(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'descricao')
    list_display_links = ('id', 'codigo')
    search_fields = ('codigo',)

admin.site.register(Stream, Streams)

class Listas(admin.ModelAdmin):
    list_display = ('id', 'user', 'stream')
    list_display_links = ('id',)

admin.site.register(Lista, Listas)