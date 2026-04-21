from rest_framework import serializers
from myflix.models import User, Stream, Lista

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']

class StreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stream
        fields = '__all__'

class ListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lista
        fields = '__all__'

# Serializer para mostrar as Streams de um Usuário específico
class ListaUserSerializer(serializers.ModelSerializer):
    stream = serializers.ReadOnlyField(source='stream.descricao')

    class Meta:
        model = Lista
        fields = ['stream']

# Serializer para mostrar os Usuários de uma Stream específica
class ListaStreamSerializer(serializers.ModelSerializer):
    user_nome = serializers.ReadOnlyField(source='user.nome')

    class Meta:
        model = Lista
        fields = ['user_nome']