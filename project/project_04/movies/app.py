import os
from flask import Flask, render_template, request,redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Movie


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#db 에 app 연동
db.init_app(app)

#migrate 초기화 하고 flask 인스턴스와 model
migrate = Migrate(app,db)
#1 INDEX
@app.route('/movies/')
def index():
    movies = Movie.query.all()
    
    return render_template('index.html', movies = movies)

#2 NEW 새 영화 등록할 페이지로 이동
@app.route('/movies/new/')
def new():
    
    return render_template('new.html')
    
#3 CREATE새로운 영화 입력하는 페이지 생성
@app.route('/movies/create/')
def create():
    alls = Movie(title = request.args.get('title'),
        title_en = request.args.get('title_en'),
        audience = request.args.get('audience'),
        open_date = request.args.get('open_date'),
        genre = request.args.get('genre'),
        watch_grade = request.args.get('watch_grade'),
        score = request.args.get('score'),
        poster_url = request.args.get('poster_url'),
        description = request.args.get('description'))
    
    db.session.add(alls)
    db.session.commit()
    # return render_template('index.html', alls = alls)
    return redirect(url_for('show', id=alls.id))

#4 SHOW    
@app.route('/movies/<int:id>/')
def show(id):
    movie = Movie.query.get(id)
    return render_template('show.html', movie = movie)

#5 EDIT
@app.route('/movies/<int:id>/edit/')
def edit(id):
    movie = Movie.query.get(id)
    return render_template('edit.html', movie = movie)
    
#6 UPDATE
@app.route('/movies/<int:id>/update/')
def update(id):
    movie = Movie.query.get(id)
    movie.title = request.args.get('title')
    movie.title_en = request.args.get('title_en')
    movie.audience = request.args.get('audience')
    movie.open_date = request.args.get('open_date')
    movie.genre = request.args.get('genre')
    movie.watch_grade = request.args.get('watch_grade')
    movie.score = request.args.get('score')
    movie.poster_url = request.args.get('poster_url')
    movie.description = request.args.get('description')
    
    db.session.commit()
    return redirect(f"/movies/{movie.id}/")
    # return redirect(url_for('index'))

#7 DELETE
@app.route('/movies/<int:id>/delete/')
def delete(id):
    movie = Movie.query.get(id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('index'))
    
    

    
    
    
    

  



if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)