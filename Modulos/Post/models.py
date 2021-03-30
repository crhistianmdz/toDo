from django.db import models

# Create your models here.
class Post(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=500)
    estados=[
        ('A', 'Abierto'),
        ('C', 'Cerrado')
    ]
    estado=models.CharField(max_length=1, choices=estados,default='A')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'
    
    def __str__(self):
        txt="{0} ,{1}"
        return txt.format(self.titulo,self.estado)