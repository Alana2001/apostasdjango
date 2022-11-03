import random
from django.shortcuts import render
from django.http import HttpResponse
from random import randint 

# Create your views here.
lista_numeros=[]
def geraRandomico(request):
    for i in range(1,7):
        numero = random.randint(1, 60)
        lista_numeros.append(numero)

    return HttpResponse(request, 'randomico', {'lista_numeros':lista_numeros})

def MegaSena(request):
    return render(request, 'loteria/MegaSena.html', {})

def ApostaClientesMega(request):
    return render(request, 'loteria/ApostaClientesMega.html', {})

def resultados(request):
    task = MegaSena.objects.all()
    data = {"task": task}
    return render(request, "loteria/resultados.html", data)

def verifica_resultado(request):
    if request.method == "POST":
        task = sorteio.objects.all()
        escolhido = request.POST.get("selecionado")
        sorteio = sorteio.objects.get(concurso=escolhido)
        apostas = apostas.objects.filter(concurso=sorteio)
        result = "Não foi dessa Vez!"
        if apostas and (
            (
                sorteio.lista_numeros == apostas.first().lista_numeros
                or sorteio.lista_numeros_apostados == apostas.first().lista_numeros_apostados
            )
        ):
            result = "Você ganhou!"
        return render(request, "loteria/resultados.html", {"result": result, "task": task})