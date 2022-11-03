from django.urls import path

from . import views  # arquivo views que ainda não utilizamos

urlpatterns = [
    path('', views.MegaSena, name='MegaSena'),
    path('ApostaClientesMega', views.ApostaClientesMega, name='ApostaClientesMega'),
    path('resultados', views.resultados, name='resultados'),
    path('verifica_resultado', views.verifica_resultado, name='verifica_resultado'),
]