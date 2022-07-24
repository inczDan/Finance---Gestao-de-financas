from django import views
from django.urls import path
from .views import home, nova_transacao
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('nova-transacao/', views.nova_transacao)
]