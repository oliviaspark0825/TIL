from django.shortcuts import render, redirect, get_object_or_404
from .models import Genre, Movie, Score
from django.db.models import Avg
from .forms import MovieForm, ScoreForm
# Create your views here.

def index(request):
    movies = Movie.objects.all()
    movies = Movie.objects.annotate(score_avg=Avg('score__score')).all()
    context = {'movies':movies,}
    return render(request, 'movies/index.html', context)
    
    #당연히 폼을 쓰려면 폼을 불러오야겠지?
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context={'form':form }
    return render(request, 'movies/form.html', context)
    
    
    
    
    # movie_pk는 숫자를 받아오는거고
    # 저아래의 pk는 무비 데이터 가져올때 column에서의 id 임
def detail(request, movie_pk):
    movie = Movie.objects.annotate(score_avg=Avg('score__score')).get(pk=movie_pk)
    scores =movie.score_set.all()
    # form양식을 불러와야지 영화 detail 페이지에서창이 뜰거니까
    form = ScoreForm()
    context = {
        'movie':movie,
        'scores':scores,
        'form': form,
    }
    return render(request, 'movies/detail.html', context)

def update(request,movie_pk):
    # 일단 원래 movie에 있던 데이터를 쫙 가지고 온다음에
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie) #1
        if form.is_valid(): # validation을 다 해주는것
            movie = form.save()             #2
            return redirect('movies:detail', movie.pk)
    
    else:
        form = MovieForm(instance=movie) # 3
  
    context = {
        'form':form,
        'movie': movie,
    }
    return render(request, 'movies/form.html', context)
    
def delete(request,movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:index')
    else:
        # post 아닌 방식으로 맘대로 삭제하려고 하면 지워지면 안되니까 걍 다시 페이지를 띄워주는거임
        return redirect('movies:detail', movie.pk)
        
        
        
        
 # 몇번 글인지를 알아야하니까 무비를 가지고와야함
def score_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        # form에다가값을 저장하고
        form = ScoreForm(request.POST)
        if form.is_valid():
            form.save()
    
            return redirect('movies:detail', movie.pk )

    return redirect('movies:detail', movie.pk)
        
def score_delete(request, movie_pk, score_pk):
    movie = Movie.objects.get(pk=movie_pk)
    score = Score.objects.get(pk=score_pk)
    if request.method == 'POST':
        score.delete()
        return redirect('movies:detail', movie.pk)
    else:
        return redirect('movies:detail', movie.pk)