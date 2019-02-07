# pip install Flask-SQLAlchemy
# pip install Flask-Migrate

# pip install flask_sqlalchemy
# pip install flask_migrate
import os
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, User
# 모델에서 불러와야 사용 가능함

app = Flask(__name__)

# flask app 에 sqlalchemy 관련 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# True가 기본값인데 그대로 두면 sqlalchemy가 데이터 베이스 객체 수정 및 신호방출 등을 추적 - 과도한 메모리 사용하니까 False로 둠

# sqlalchemy 초기화
# db = SQLAlchemy(app)
db.init_app(app)
# 분리되었을 때는 바로 위 형태로 초기화해야함

migrate = Migrate(app, db)
# flask, alchemy의 인스턴스를 인자로 받음

@app.route('/')
#뷰 함수 - 뷰함수의 라우트를 리턴한다
def index():
    # url_for('index') =>>> '/'
    # return redirect(url_for('index'), )
    users = User.query.all() 
    return render_template('index.html', users=users)
    # 저 아래 user에서 모든 것으 다 가지고 올때, index에서 출력
    
    # 이 함수가 받고, def create 함수 실행 -> 받아온 유저네임을 변수에 받고, 그걸 또 db에 넣어주어야 함
@app.route('/users/create')
def create():
    username = request.args.get('username')
    email = request.args.get('email')
    user = User(username=username, email=email) 
    # insert into 하고
    db.session.add(user)
    db.session.commit()
    # db에 유저네임과 이메일이 들어감
    return redirect(url_for('index'))
    
@app.route('/users/delete/<int:id>')
def delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    # 적용시키려면 commit 까지
    db.session.commit()
    return redirect(url_for('index'))
    # 페이지가 딜리트 찍고 다시 이동, 새로운 페이지를 만들어줄 필요는 없으니까 render 안함

@app.route('/users/edit/<int:id>')
def edit(id):
    user = User.query.get(id)
    return render_template('edit.html', user=user)
#  페이지만 띄워주는것이고, update는 다른데서 또 해야함 그래서 2개가 필요한거임

@app.route('/users/update/<int:id>')
def update(id):
    user = User.query.get(id)
    username = request.args.get('username')
    email = request.args.get('email')
    user.username = username
    user.email = email
    db.session.commit()
    return redirect(url_for('index'))
    # 수정한 값을 받아서 기존 컬럼을 바꿔주고, commit하고 redirect


    

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)


        