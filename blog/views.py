from django.shortcuts import render
from .models import post, categoria


# Create your views here.
def blogs(request):
    posts=post.objects.all()
    return render(request, "blog/blog.html", {"posts":posts})

def categoria(request, categoria_id):
    ##categori= categoria.ob(id=categoria_id)
    posts= post.objects.filter(categori=categoria)
    return render(request, "blog/categoria.html", {'categoria':categoria, "posts": posts})