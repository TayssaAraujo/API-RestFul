from django.apps import AppConfig


class MyflixConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myflix'

'''from rest_framework import serializers
from myflix.models import User, Stream

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']

class StreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stream
        fields = '__all__'
'''