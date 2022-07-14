from django.urls import path

from . import views

app_name = 'painel'

urlpatterns = [
    path('', views.home, name='dashboard'),
    path('conexoes/<int:id>/', views.conexoes, name='conexoes'),
]
