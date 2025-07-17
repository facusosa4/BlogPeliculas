from django.urls import path
from .views import (
    index,
    about,
    crear_pelicula,
    crear_director,
    crear_critica,
    buscar_pelicula,
    lista_criticas, 
)

urlpatterns = [
    path('', index, name='inicio'),
    path('about/', about, name='about'),
    path('crear/', crear_pelicula, name='crear_pelicula'),
    path('crear_director/', crear_director, name='crear_director'),
    path('crear_critica/', crear_critica, name='crear_critica'),
    path('buscar_pelicula/', buscar_pelicula, name='buscar_pelicula'),
    path('criticas/', lista_criticas, name='lista_criticas'),  
]
