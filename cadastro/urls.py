from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.home, name='home'),             # Rota para o Humano (Navegador)
    path('api/listar/', views.listar_pessoas, name='api'),  # Rota para o Robô (JavaScript)
]