from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    estado = models.BooleanField(default=True)
    # auto_now es cuando se actuliza al momento de modificar 
    fecha_creacion = models.DateField(verbose_name="Fecha creacion", auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
    
    def __str__(self):
        return self.nombre


class Autor(models.Model):
    # Datos principales
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100, null=False, blank=False)
    apellidos = models.CharField(max_length=100, null=False, blank=False)
    correo = models.EmailField(verbose_name="Correo Electronico", null=False, blank=False)

    # Datos secundarios
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    twiter = models.URLField(null=True, blank=True)
    web = models.URLField(null=True, blank=True)

    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name='autor'
        verbose_name_plural='autores'

    def __str__(self):
        return f"{self.apellidos} {self.nombres}"


class Post(models.Model):
    id = models.AutoField(primary_key=True)    
    titulo = models.CharField(max_length = 90, blank = False, null= False)
    slug = models.CharField(verbose_name="Slug", max_length=100, blank=False, null=False)
    descripcion = models.CharField(max_length= 110, blank=False, null=False)
    contenido = RichTextField()
    img = models.URLField(max_length= 255, blank=False, null=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    
    estado = models.BooleanField(verbose_name="Publicado", default=True)
    fecha_creacion = models.DateField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name= 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.titulo









