from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'painel/home.html', {
        'nome':'Igor Lemões'
    })

def conexoes(request):
    return render(request, 'painel/conexoes.html', {
        'numero':'53991900889'
    })
