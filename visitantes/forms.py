from django import forms
from visitantes.models import Visitantes


class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitantes
        fields = [
            "nome_completo", "cpf", 'data_nascimento',
            "numero_casa", "placa_veiculo"
        ]
        error_messages = {
            "nome_completo": {
                "required": "O Nome completo do visitante é obrigatório para o registro"
            },
            "cpf": {
                "required": "O CPF do visitante é obrigatório para o registro"
            },
            "data_nascimento": {
                "required": "A data de nascimento do visitante é obrigatória para o registro",
                "invalid": "Informe um formato valido para a data de nascimento (DD/MM/AAAA)"
            },
            "numero_casa": {
                "required": "O numero da casa e obrigatório para o registro"
            },
        }
