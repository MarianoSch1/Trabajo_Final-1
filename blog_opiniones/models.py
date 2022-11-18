from django.db import models

class Opinion (models.Model):
    titulo = models.CharField(max_length=30, default="")
    breve_opinion = models.CharField(max_length=300, default="")
    opinion_detallada = models.CharField(max_length=3000, default="")
    firma = models.CharField(max_length=30, default="")
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to="opiniones", null=True, blank=True)
    
    def __str__(self):
        return f"id:{self.id}, titulo:{self.titulo}"
        
