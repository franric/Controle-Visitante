from django.contrib import messages
from django.shortcuts import render, redirect
from visitantes.forms import VisitanteForm


def registrar_visitantes(request):
    form = VisitanteForm()

    if request.method == "POST":
        form =VisitanteForm(request.POST)

        if form.is_valid():
            visitante = form.save(commit=False)

            visitante.registrado_por = request.user.porteiro
            visitante.save()

            messages.success(
                request,
                "Visitante Registrado com Sucesso"
            )

            return redirect("index")

    context = {
        "nome_pagina": "Registrar Visitante",
        "form": form
    }

    return render(request, "registrar_visitante.html", context)
