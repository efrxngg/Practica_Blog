from django.urls import path
from .views import *
from django.contrib import admin

urlpatterns=[
    path('', home, name = 'blog_index'),
    path('generales/', generales, name='blog_generales'),
    path('programacion/', programacion, name='blog_programacion'),
    path('videojuegos/', videojuegos, name = 'blog_videojuegos'),
    path('technologia/', technologia, name='blog_technologia'),
    path('tutoriales/', tutoriales, name='blog_tutoriales'),
    path('admin/', admin.site.urls),

    # Va al final 
    path('<slug:slug>/', detalle_post, name= 'blog_detalle_post'), 
    
]







