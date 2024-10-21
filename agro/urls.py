from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import salvar_sugestao, listar_sugestoes, editar_sugestao, deletar_sugestao
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
    path('editar_sugestoes/<int:pk>/', editar_sugestao, name='editar_sugestao'),  

    path('agro/list/', views.AgroListView.as_view(), name='agro-list'),
    path('agro/detail/<int:pk>/', views.AgroDetailView.as_view(), name='agro-detail'),
    path('agro/update/<int:pk>/', views.AgroUpdateView.as_view(), name='agro-update'),
    path('agro/delete/<int:pk>/', views.AgroDeleteView.as_view(), name='agro-delete'),
    path('agro/create/', views.AgroCreateView.as_view(), name='agro-create'),
    path('login/', custom_login, name='custom_login'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



