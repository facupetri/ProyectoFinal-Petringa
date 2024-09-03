from django.db import models

class Post(models.Model):
    autor = models.CharField(max_length=40)
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=40, null=True, blank=True)
    posteo = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True)

    def __str__(self):
        return self.titulo