from django.db import models
from ckeditor.fields import RichTextField

class Director(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    año = models.IntegerField()
    genero = models.CharField(max_length=100)
    sinopsis = RichTextField()
    imagen = models.ImageField(upload_to='peliculas/', null=True, blank=True)
    fecha_estreno = models.DateField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Critica(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    autor = models.CharField(max_length=100)
    contenido = models.TextField()
    puntaje = models.IntegerField()  # Del 1 al 10

    def __str__(self):
        return f"{self.autor} - {self.pelicula.titulo}"