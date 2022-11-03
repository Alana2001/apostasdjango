from django.urls import path,include
from . import views

 

urlpatterns = [
    path("", views.login_request, name="login"),
    path("login", views.login_request, name="login"),
    path('homepage', views.homepage, name='homepage'),
    path('aposta_jogodobicho', views.aposta_jogodobicho, name='aposta_jogodobicho'),
    path("register", views.register_request, name="register"),
    path("logout", views.logout_request, name= "logout"),
    path('cria_aposta', views.cria_aposta, name='cria_aposta'),
    path('resultados', views.resultados, name='resultados'),
    path('verifica_resultado', views.verifica_resultado, name='verifica_resultado'),
]