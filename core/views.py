from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class UsuarioView(APIView):
    @swagger_auto_schema(
        operation_description="Recupera a lista de usuários",
        responses={200: openapi.Response("Lista de usuários")},
    )
    def get(self, request):
        return Response({"usuarios": ["João", "Maria"]})

# Create your views here.
