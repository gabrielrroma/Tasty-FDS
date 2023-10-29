from django.urls import path
from recipe import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='cadastro'),
    path('filter-recipe/', views.filtrarreceita, name='filtrarreceita'),
    path('historico/', views.historico, name='historico'),
    path('novareceita/', views.novareceita, name='novareceita'),
    path('perfil/', views.perfil, name='perfil'),
    path('recomendacoes/', views.recomendacoes, name='recomendacoes'),
]
