from django.forms import ModelForm
from .models import Transacao


class TransacaoForms(ModelForm): #definição de formulario que o django constroi com facilidades.
    class Meta:
        model = Transacao
        fields = ['data','descricao', 'valor', 'categoria', 'observacoes'] # os campos que queremos que apareça