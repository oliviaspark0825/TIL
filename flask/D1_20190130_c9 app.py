c9 app.py

```pyth
from flask import Flask, render_template
import os
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello there!'
    
#5월 20부터 d-day 카운트 출력
@app.route('/dday')
def dday():
    # date(2019, 05, 20) - date.today()
    # datetime.timedelta(1)
    time1 = datetime.datetime(2019, 5, 20)
    time2 = datetime.datetime.now()
    x = (time1 - time2).days
    return f'{x}일 남았습니다.'
    
    
#variable routing
@app.route('/hi/<string:name>')
def hi(name):
    return f'안녕, {name}'

@app.route('/cube/<string:x>')
def cube(x):
    cubes = int(x)**3
    return f'{x}의 세제곱은 {cubes}입니다.'
    # flask에서는 리턴이 문자밖에안됨
    
@app.route('/ho/<string:name>')
def greeting(name):
    return render_template('greeting.html', html_name = name)
    # 변수 할당은 오른쪽에서 왼쪽으로 가고, 왼쪽 = html / 오른쪽 = py

@app.route('/movie')
def movie():
    movies = ['극한직업', '정글북', '캡틴마블', '보헤미안랩소디', '완벽한 타인']
    return render_template('movie.html', movie = movies)
   

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)
    # 어떤 환경에서든지 알아서 주소를 가지고 옴
    
    
```

templates

```python
<!doctype html>
<title>Hello from Flask</title>
{% if html_name == '박수현' %}
  <h1>{{ html_name }} 왔닝?</h1>
{% else %}
  <h1>{{ html_name }} 너 누구야?</h1>
{% endif %}




<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS"
        crossorigin="anonymous">
    <title>Document</title>
</head>
<body>
     <div class="container">
    <h1>영화목록</h1>
    <div class='row'>
      {% for movie in movies %}
      <div class="card" style="width: 18rem;">
        <img class="card-img-top" src="..." alt="Card image cap">
        <div class="card-body">
          <h5 class="card-title">{{ movie }}</h5>
          <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
          <a href="#" class="btn btn-primary">Go somewhere</a>
        </div>
      </div>
      {% endfor %}
    </div>
  </div>
    
</body>
</html>
```

