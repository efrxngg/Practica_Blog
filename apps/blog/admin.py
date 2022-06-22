from django.contrib import admin
from .models import Autor, Categoria, Post
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class CategoriaResourse(resources.ModelResource):
    class Meta:
        model = Categoria

class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ["id", 'nombre']
    list_display = ('id', 'nombre', 'estado' , 'fecha_creacion')
    resources_class = CategoriaResourse
admin.site.register(Categoria, CategoriaAdmin)



class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor

class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['id', 'nombre', 'apellido']
    list_display = ('id', 'nombres', 'apellidos', 'correo', 'estado', 'fecha_creacion')
    resource_class = AutorResource
admin.site.register(Autor, AutorAdmin)



admin.site.register(Post)