from django.urls import path, include
from recipe import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('login/', views.login, name='login'),
    path('login/', include('django.contrib.auth.urls')),
    path(' ', LoginView.as_view(), name = 'login' ),
    path('home/', login_required(LoginView.as_view(), redirect_field_name=None), name='login'),
    path('register/', views.register, name='cadastro'),
    path('filter-recipe/', views.filtrarreceita, name='filtrarreceita'),
    path('historico/', views.historico, name='historico'),
    path('novareceita/', views.novareceita, name='novareceita'),
    path('perfil/', views.perfil, name='perfil'),
    path('recomendacoes/', views.recomendacoes, name='recomendacoes'),
]
