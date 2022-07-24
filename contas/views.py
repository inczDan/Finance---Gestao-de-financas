from __future__ import print_function
from django.http import HttpResponse
from django.shortcuts import redirect, render
from contas.models import Categoria, Transacao
from .forms import TransacaoForms
# Create your views here.


def home(request):
    desp_fix = {}
    desp_fix ['transacoes'] = Transacao.objects.all() 
    return render(request, 'contas/home.html', desp_fix)

def nova_transacao(request):
    data = {}
    form = TransacaoForms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(home)
    data['form'] = form
    return render(request, 'contas/novo_form.html', data)
