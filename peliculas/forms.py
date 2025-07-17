from django import forms
from .models import Pelicula, Director, Critica

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = '__all__'

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'

class CriticaForm(forms.ModelForm):
    class Meta:
        model = Critica
        fields = '__all__'

class BuscarPeliculaForm(forms.Form):
    titulo = forms.CharField(max_length=200, label="Buscar por título")