from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import salvar_sugestao, listar_sugestoes, deletar_sugestao
from .views import custom_login


app_name = 'agro'

urlpatterns = [
    path('', views.index, name='index'),  
    path('sugestao/', salvar_sugestao, name='salvar_sugestao'),
    path('listagem_sugestoes/', listar_sugestoes, name='listar_sugestoes'),
    path('lagartas/', views.lagartas, name='lagartas'),
    path('agrotoxico/', views.agrotoxico, name='agrotoxico'),
    path('gafanhotos/', views.gafanhotos, name='gafanhotos'),
    path('sobre_nos/', views.sobre_nos, name='sobre_nos'),
    path('formulario/', views.formulario, name='formulario'),
    path('deletar_sugestao/<int:pk>/', deletar_sugestao, name='agro-delete'),  
    path('login/', custom_login, name='custom_login'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('nova_praga/', views.nova_praga, name='nova_praga'),
    path('agro_list/', views.agro_list, name='agro_list'),
    path('pragas/<int:praga_id>/', views.agro_detalhe, name='agro_detalhe'),
    path('agro_editar/<int:pk>/', views.agro_editar, name='agro_editar'),
    path('agro_deletar/<int:pk>/', views.agro_deletar, name='agro_deletar'),
    path('like/<int:praga_id>/', views.like_praga, name='like'),
    path('dislike/<int:praga_id>/', views.dislike_praga, name='dislike'),
    path('sair/', views.sair, name="sair")
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



