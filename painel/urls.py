from django.urls import path

from painel.views import conexoes, home

urlpatterns = [
    path('', home),
    path('conexoes/', conexoes),
]
