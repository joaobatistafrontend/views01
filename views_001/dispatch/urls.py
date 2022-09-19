from django.urls import path

from .apps import AppConfig
from views_001.dispatch.views import ViewNBloqueado, ViewBloqueado


urlpatterns = [
    path('', ViewNBloqueado.as_view(), name='index'),
    path('bloqueado/', ViewBloqueado.as_view(), name='bloqueado')
]



'''
  - Tarefa 1:
  - ao clicar na ação BLOQUEAR, o sistema deverá ser bloqueado
  redirecionando o usuario para a pagina de bloqueado
  para realizar essa acao usar o metodo dispatch da view
  para direvionar use o metodo redirect que está em django.shortcuts import redirect
'''