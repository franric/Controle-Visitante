from django import forms
from apps.visitantes.models import Visitantes


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


class AutorizaVisitantesForm(forms.ModelForm):
    morador_responsavel = forms.CharField(required=True)

    class Meta:
        model = Visitantes
        fields = [
            "morador_responsavel"
        ]
        error_messages = {
            "morador_responsavel": {
                "required": "Informe o nome do morador responsável pelo visitante"
            }
        }
