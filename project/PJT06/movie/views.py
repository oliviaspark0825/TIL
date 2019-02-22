from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    return render(request, 'movie/index.html', {'movies':movies})

def detail(request,pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, 'movie/detail.html',{'movie':movie})
    
def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('/movie/')
