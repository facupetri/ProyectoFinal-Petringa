from django.db import models

class Post(models.Model):
    autor = models.CharField(max_length=40)
    titulo = models.CharField(max_length=40)
    posteo = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)