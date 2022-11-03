from crypt import methods
from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from jogodobicho.models import Aposta, Apostador, Sorteio
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import auth


from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

import random


def homepage(request):
    return render(request, "jogodobicho/index.html", {})


def aposta_jogodobicho(request):
    task = Sorteio.objects.all()
    data = {"task": task}
    return render(request, "jogodobicho/jogodobicho.html", data)


def resultados(request):
    task = Sorteio.objects.all()
    data = {"task": task}
    return render(request, "jogodobicho/resultados.html", data)


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return render(request, "jogodobicho/index.html", {})
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(
        request=request,
        template_name="jogodobicho/register.html",
        context={"register_form": form},
    )


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return render(request, "jogodobicho/index.html", {})
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(
        request=request,
        template_name="jogodobicho/login.html",
        context={"login_form": form},
    )


def logout_request(request):
    logout(request)
    messages.info(request, "Voce esta deconectado.")
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return render(request, "jogodobicho/index.html", {})
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(
        request=request,
        template_name="jogodobicho/login.html",
        context={"login_form": form},
    )


def cria_aposta(request):
	if request.method == 'POST':
		selected_values = request.POST.getlist('animal')
		concursoescolhido= request.POST.get('concursoselecionado')
		user = get_object_or_404(User, pk=request.user.id)
		aposta = Aposta.objects.create(pessoa=user,primeiro_animal=selected_values[0], segundo_animal=selected_values[1], concurso=concursoescolhido)
		aposta.save()
		return render(request, 'jogodobicho/index.html', {})
	else:
		return render(request, 'jogodobicho/jogodobicho.html', {})


def verifica_resultado(request):
    if request.method == "POST":
        task = Sorteio.objects.all()
        concursoescolhido = request.POST.get("concursoselecionado")
        sorteio = Sorteio.objects.get(concurso=concursoescolhido)
        apostas = Aposta.objects.filter(concurso=sorteio)
        result = "Não foi dessa Vez!"
        if apostas and (
            (
                sorteio.primeiro_animal == apostas.first().primeiro_animal
                or sorteio.segundo_animal == apostas.first().segundo_animal
            )
        ):
            result = "Deu bicho! Você ganhou!"
        return render(request, "jogodobicho/resultados.html", {"result": result, "task": task})