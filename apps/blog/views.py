from django.shortcuts import get_object_or_404, render
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.


def home(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado= True)
    # print(queryset)
    if queryset:
        posts = Post.objects.filter(
            # No importa las may o min __icontains == like
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct()

    # lista que se queremos que pagine el core django, la cant de elementos que quiero que pagine
    # lista de paginas, el numero elementos a mostar
    paginacion = Paginator(posts, 2)
    page = request.GET.get('page')
    print(page)
    posts = paginacion.get_page(page)
        
    return render(request, "blog/index.html", {'posts': posts})

def detalle_post(request, slug):
    post = Post.objects.get(slug= slug)
    print(post)
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post.html', {'detalle_post': post})

def generales(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(estado=True, categoria= Categoria.objects.get(nombre__iexact="General"))

    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado= True,
            categoria = Categoria.objects.get(nombre__iexact='General'),
        )

    paginacion = Paginator(posts, 2)
    page = request.GET.get('page')
    print(page)
    posts = paginacion.get_page(page)
    

    return render(request, 'blog/generales.html', {'posts': posts})

def programacion(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(estado=True, categoria= Categoria.objects.get(nombre__iexact="Programacion"))
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado= True,
            categoria = Categoria.objects.get(nombre__iexact='Programacion'),
        )
    paginacion = Paginator(posts, 2)
    page = request.GET.get('page')
    print(page)
    posts = paginacion.get_page(page)
    
    return render(request, "blog/programacion.html", {'posts': posts})

def videojuegos(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(estado=True, categoria= Categoria.objects.get(nombre__iexact="Videojuegos"))
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado= True,
            categoria = Categoria.objects.get(nombre__iexact='Videojuegos'),
        )
    paginacion = Paginator(posts, 2)
    page = request.GET.get('page')
    print(page)
    posts = paginacion.get_page(page)

    return render(request, "blog/videojuegos.html", {'posts': posts})

def tutoriales(request):
    posts = Post.objects.filter(estado=True, categoria= Categoria.objects.get(nombre__iexact="Tutoriales"))
    queryset = request.GET.get('buscar')
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado= True,
            categoria = Categoria.objects.get(nombre__iexact='tutoriales'),
        )
    paginacion = Paginator(posts, 2)
    page = request.GET.get('page')
    print(page)
    posts = paginacion.get_page(page)
    return render(request, "blog/tutoriales.html", {'posts': posts})

def technologia(request):
    posts = Post.objects.filter(estado=True, categoria= Categoria.objects.get(nombre__iexact="Technologia"))
    queryset = request.GET.get('buscar')
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado= True,
            categoria = Categoria.objects.get(nombre__iexact='technologia'),
        )
    paginacion = Paginator(posts, 2)
    page = request.GET.get('page')
    print(page)
    posts = paginacion.get_page(page)

    return render(request, "blog/technologia.html", {'posts': posts})





