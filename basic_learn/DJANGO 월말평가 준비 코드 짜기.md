DJANGO 월말평가 준비 코드 짜기

```python
# 프로젝트 폴더 만들기
mkdir <practice>
cd practice/
#가상환경 활성화
pyenv local django-venv
#장고 설치
pip install django
#프로젝트 생성
django-admin startproject <프로젝트 이름> .
#서버 실행
python manage.py runserver $IP:$PORT
# SETTINGS.PY
ALLOWED_HOSTS = ['*']
# gitignore
#프로젝트 구조
PROJECT01/
    manage.py
    django_intro/
        __init__.py
        settings.py
        urls.py
        wsgi.py
	db.sqlite3
# 앱 생성
$ python manage.py startapp home
```

