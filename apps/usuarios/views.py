from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.visitantes.models import Visitantes


@login_required
def index(request):
    todos_visitantes = Visitantes.objects.all()
    context = {"nome_pagina": "Inicio da Dashboard", "todos_visitantes": todos_visitantes}

    return render(request, "index.html", context)
