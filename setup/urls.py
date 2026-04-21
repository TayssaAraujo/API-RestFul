from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, permissions  # Adicionado o permissions aqui
from myflix.views import UserViewSet, StreamViewSet, ListaViewSet, ListaUser, ListaStream

# Imports do Swagger (conforme sua imagem)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuração da Documentação
schema_view = get_schema_view(
    openapi.Info(
        title="MyFlix API Documentação",
        default_version='v1',
        description="Documentação interativa para a API MyFlix",
        contact=openapi.Contact(email="tayssa@email.com"),  # Seu email aqui
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],  # Permite que qualquer um veja a doc
)

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('streams', StreamViewSet, basename='streams')
router.register('listas', ListaViewSet, basename='listas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('users/<int:pk>/listas/', ListaUser.as_view()),
    path('streams/<int:pk>/listas/', ListaStream.as_view()),

    # Rotas do Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]