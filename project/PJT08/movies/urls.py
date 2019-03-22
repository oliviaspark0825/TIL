from django.urls import path
from . import views

app_name = 'movies'

urlpatterns=[
    # delete를 시켰을 때 그 값을 일단 url로 보내고, 삭제하자마자 바로 redirect를 하니까 
    #눈에는 안보이지만 행동은 있느거임
    path('<int:movie_pk>/scores/<int:score_pk>/delete/', views.score_delete, name='score_delete'),
    path('<int:movie_pk>/score_create', views.score_create, name='score_create'),
    path('<int:movie_pk>/delete', views.delete, name='delete'),
    path('<int:movie_pk>/update', views.update, name='update'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('', views.index, name='index'),
    ]