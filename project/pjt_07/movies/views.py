from django.shortcuts import render, redirect
from .models import Genre, Movie, Score
# Create your views here.
from django.shortcuts import render, redirect
from django.db.models import Avg
from .models import Genre, Movie, Score
# Create your views here.

def index(request):
    # movies = Movie.objects.all()
    movies = Movie.objects.annotate(score_avg=Avg('score__score')).all()
    
    context = {
        'movies':movies,
    }
    return render(request, 'movies/index.html', context)

def detail(request, movie_pk):
    movie = Movie.objects.annotate(score_avg=Avg('score__score')).get(pk=movie_pk)
    # movie = Movie.objects.get(pk=movie_pk)
    scores = movie.score_set.all()
    context = {
        'scores':scores,
        'movie':movie,
    }
    return render(request, 'movies/detail.html', context)
    
def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:index')
    else:
        return redirect('movies:detail', movie_pk)
    
    # 평점 생성하기
def score_new(request, movie_pk):
    
    movie = Movie.objects.get(pk=movie_pk)
    score = request.POST.get('score')
    content = request.POST.get('content')
    # 클래스 인스턴스를 생성해서 저장하는 방법
    # score = Score(score=score, movie=movie, content=content)
    # score.save()
    Score.objects.create(movie=movie, content=content, score=score)
   
    return redirect('movies:detail', movie.pk)
    
def score_delete(request, movie_pk, score_pk):
    movie = Movie.objects.get(pk=movie_pk)
    score = Score.objects.get(pk=score_pk)
    if request.method == 'POST':
        score.delete()
        return redirect('movies:detail', movie.pk)
    else:
        return redirect('movies:detail', movie.pk)