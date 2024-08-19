from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lagartas/', views.lagartas, name='lagartas'),
    path('agrotoxico/', views.agrotoxico, name='agrotoxico'),
    path('gafanhotos/', views.gafanhotos, name='gafanhotos'),
    path('sobre_nos/', views.sobre_nos, name='sobre_nos'),
    path('formulario/', views.formulario, name='formulario'),
    path('listagem_sugestoes/', views.listagem_sugestoes, name='listagem_sugestoes'),
    path('deletar_sugestao/', views.deletar_sugestao, name='deletar_sugestao'),
    path('editar_sugestoes/', views.editar_sugestoes, name='editar_sugestoes'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)