from django.shortcuts import render, redirect
from .forms import PeliculaForm, DirectorForm, CriticaForm, BuscarPeliculaForm
from .models import Pelicula, Critica
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'peliculas/index.html')

def about(request):
    return render(request, 'peliculas/about.html')

@login_required
def crear_critica(request):
    if request.method == 'POST':
        form = CriticaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = CriticaForm()
    return render(request, 'peliculas/crear_critica.html', {'form': form})

def crear_director(request):
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = DirectorForm()
    return render(request, 'peliculas/crear_director.html', {'form': form})

def crear_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = PeliculaForm()
    return render(request, 'peliculas/crear_pelicula.html', {'form': form})

def buscar_pelicula(request):
    peliculas = None
    if request.method == 'POST':
        form = BuscarPeliculaForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            peliculas = Pelicula.objects.filter(titulo__icontains=titulo)
    else:
        form = BuscarPeliculaForm()
    return render(request, 'peliculas/buscar_pelicula.html', {'form': form, 'peliculas': peliculas})

def lista_criticas(request):
    criticas = Critica.objects.all()
    return render(request, 'peliculas/lista_criticas.html', {'criticas': criticas})
