from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('conexoes/<int:id>/', views.conexoes),
]
