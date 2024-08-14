from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lagartas/', views.lagartas, name='lagartas'),
    path('agrotoxico/', views.agrotoxico, name='agrotoxico'),
    path('gafanhotos/', views.gafanhotos, name='gafanhotos'),
    path('sobre_nos/', views.sobre_nos, name='sobre_nos'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('listagem_sugestoes/', views.listagem_sugestoes, name='listagem_sugestoes'),
]
