from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required

from apps.visitantes.models import Visitantes
from apps.visitantes.forms import VisitanteForm, AutorizaVisitantesForm

from django.utils import timezone


@login_required
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


@login_required
def informacoes_visitante(request, id):

    visitante = get_object_or_404(Visitantes, id=id)

    form = AutorizaVisitantesForm()
    if request.method == "POST":
        form = AutorizaVisitantesForm(
            request.POST,
            instance=visitante
        )

        if form.is_valid():
            visitante = form.save(commit=False)

            visitante.status = "EM_VISITA"
            visitante.horario_autorizacao = timezone.now()

            visitante.save()

            messages.success(
                request,
                "Entrada de visitante autorizada com sucesso"
            )

            return redirect("index")

    context = {
        "nome_pagina": "Informações do Visitante",
        "visitante": visitante,
        "form": form
    }

    return render(request, "informacoes_visitante.html", context)


@login_required
def finalizar_visita(request, id):

    if request.method == "POST":
        visitante = get_object_or_404(
            Visitantes,
            id=id
        )

        visitante.status = "FINALIZADO"
        visitante.horario_saida = timezone.now()

        visitante.save()

        messages.success(
            request,
            "Visita Finalizada com Sucesso"
        )

        return redirect("index")

    else:
        return HttpResponseNotAllowed(
            ["POST"],
            "Metodo não Permitido"
        )
