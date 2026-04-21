from rest_framework import viewsets, generics
from myflix.models import User, Stream, Lista
from myflix.serializers import (
    UserSerializer,
    StreamSerializer,
    ListaSerializer,
    ListaUserSerializer,
    ListaStreamSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StreamViewSet(viewsets.ModelViewSet):
    queryset = Stream.objects.all()
    serializer_class = StreamSerializer

class ListaViewSet(viewsets.ModelViewSet):
    queryset = Lista.objects.all()
    serializer_class = ListaSerializer

# View para listar os filmes de um usuário específico
class ListaUser(generics.ListAPIView):
    def get_queryset(self):
        # O filtro usa o ID passado na URL (pk)
        queryset = Lista.objects.filter(user_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaUserSerializer

# View para listar os usuários de um filme específico
class ListaStream(generics.ListAPIView):
    def get_queryset(self):
        # O filtro usa o ID passado na URL (pk)
        queryset = Lista.objects.filter(stream_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaStreamSerializer