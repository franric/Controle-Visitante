from django import forms
from visitantes.models import Visitantes


class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitantes
        fields = [
            "nome_completo", "cpf", 'data_nascimento',
            "numero_casa", "placa_veiculo"
        ]
