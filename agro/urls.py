from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import salvar_sugestao, listar_sugestoes, editar_sugestao, deletar_sugestao



urlpatterns = [
    path('sugestao/', salvar_sugestao, name='salvar_sugestao'),
    path('listagem_sugestoes/', listar_sugestoes, name='listar_sugestoes'),
    path('', views.index, name='index'),
    path('lagartas/', views.lagartas, name='lagartas'),
    path('agrotoxico/', views.agrotoxico, name='agrotoxico'),
    path('gafanhotos/', views.gafanhotos, name='gafanhotos'),
    path('sobre_nos/', views.sobre_nos, name='sobre_nos'),
    path('formulario/', views.formulario, name='formulario'),
    path('deletar_sugestao/', views.deletar_sugestao, name='deletar_sugestao'),
    path('editar_sugestoes/', views.editar_sugestoes, name='editar_sugestoes'),
    path('editar_sugestao/', views.editar_sugestao, name='editar_sugestao')

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)