"""
URL configuration for meu_projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Importando a sua View lá do app core
from core.views import UsuarioView

# Configuração do Swagger
schema_view = get_schema_view(
   openapi.Info(
      title="API Exemplo",
      default_version="v1",
      description="Documentação interativa da API Exemplo",
      terms_of_service="https://www.seusite.com/terms/",
      contact=openapi.Contact(email="contato@seusite.com"),
      license=openapi.License(name="Licença MIT"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # 1. Admin do Django
    path('admin/', admin.site.urls),

    # 2. Sua nova rota de Usuários
    path('usuarios/', UsuarioView.as_view(), name='usuarios'),

    # 3. Rotas da Documentação (Swagger e Redoc)
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]