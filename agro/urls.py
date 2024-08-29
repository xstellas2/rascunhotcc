from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import salvar_sugestao, listar_sugestoes, editar_sugestao, deletar_sugestao, search

app_name = 'agro'

urlpatterns = [
    path('', views.index, name='index'),  # A URL base do aplicativo 'agro' corresponde à view 'index'
    path('sugestao/', salvar_sugestao, name='salvar_sugestao'),
    path('search/', search, name='search'),
    path('listagem_sugestoes/', listar_sugestoes, name='listar_sugestoes'),
    path('lagartas/', views.lagartas, name='lagartas'),
    path('agrotoxico/', views.agrotoxico, name='agrotoxico'),
    path('gafanhotos/', views.gafanhotos, name='gafanhotos'),
    path('sobre_nos/', views.sobre_nos, name='sobre_nos'),
    path('formulario/', views.formulario, name='formulario'),
    path('deletar_sugestao/<int:pk>/', deletar_sugestao, name='agro-delete'),
    path('editar_sugestoes/<int:pk>/', editar_sugestao, name='editar_sugestoes'),  # Corrigido para 'editar_sugestao'
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
