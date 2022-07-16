import json
import time

import requests
from django.http import HttpResponse, StreamingHttpResponse
from django.urls import path

from . import views


def retorno_teste(request):    
    teste = request.GET.get('q')    
    response=requests.get(f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/{teste}/municipios').json()
    return HttpResponse(response)


def consulta(teste):
    for i in range(10000):
        yield '\ndata: {}\n\n'.format('message {}'.format(i+int(teste)))
        time.sleep(1)

def streamFun(request):
    teste = request.GET.get('valor')
    return StreamingHttpResponse(consulta(teste), content_type='text/event-stream')

app_name = 'painel'

urlpatterns = [
    path('', views.home, name='dashboard'),
    path('conexoes/<int:id>/', views.conexoes, name='conexoes'),
    path('clicked/', retorno_teste, name='clicado'),
    path('stream/', streamFun, name='stream')
]
