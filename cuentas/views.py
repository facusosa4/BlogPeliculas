from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

def registro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('inicio')  # redirige a la vista index en peliculas.urls
    else:
        form = UserCreationForm()
    return render(request, 'cuentas/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect('inicio')  # redirige a la vista index en peliculas.urls
    else:
        form = AuthenticationForm()
    return render(request, 'cuentas/login.html', {'form': form})

@login_required
def perfil_view(request):
    return render(request, 'cuentas/perfil.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # redirige a la vista login en cuentas.urls
