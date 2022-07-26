from __future__ import print_function
from django.http import HttpResponse
from django.shortcuts import redirect, render
from contas.models import Categoria, Transacao
from .forms import TransacaoForms
# Create your views here.


def home(request):
    data = {}
    # despfix = {}
    data['cat1'] = Transacao.objects.filter(categoria = 1)
    data['cat2'] = Transacao.objects.filter(categoria = 2)
    # despfix ['despfixas'] = Transacao.objects.filter(categoria = 1)
    return render(request, 'contas/home.html', data)
#criacao de uma transação -create-
def nova_transacao(request):
    data = {}
    form = TransacaoForms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    data['form'] = form
    return render(request, 'contas/novo_form.html', data )



#nesta secao estamos construindo um codigo para fazer update em um item ja existente
def update(request, id):
    data = {}
    transacao = Transacao.objects.get(id=id) #aqui pegamos um item ja existente através de seu id
    form = TransacaoForms(request.POST or None, instance=transacao)#caso ele exista e possua informação, estará valido
    if form.is_valid():
        form.save()
        return redirect('/')
    data['form'] = form
    data['transacao'] = transacao
    return render(request, 'contas/novo_form.html', data)

def delete(request, id):
    transacao = Transacao.objects.get(id=id) #estamos recuperando o objeto do banco novamente
    transacao.delete()
    return redirect('/')