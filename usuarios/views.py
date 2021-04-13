from django.shortcuts import render
from visitantes.models import Visitantes


def index(request):
    todos_visitantes = Visitantes.objects.all()
    context = {"nome_pagina": "Inicio da Dashboard", "todos_visitantes": todos_visitantes}

    return render(request, "index.html", context)
