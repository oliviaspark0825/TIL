20190222 |  DJANGO  PROJECT  완전 정리

```python
mkdir <폴더이름>- 가상 환경을 켜기 위해 
들어가서 가상 환경 설정  pyenv local django-venv
<폴더> 안에 들어가서 project 생성 
(django-venv) oliviaspark0825:~/workspace/PJT06 $ django-admin startproject django_06 .
(django-venv) oliviaspark0825:~/workspace/PJT06 $ ls -al
total 20
drwxr-xr-x 3 ubuntu ubuntu 4096 Feb 22 00:23 ./
drwxrwxr-x 7 ubuntu ubuntu 4096 Feb 22 00:22 ../
-rw-r--r-- 1 ubuntu ubuntu   12 Feb 22 00:22 .python-version
drwxr-xr-x 2 ubuntu ubuntu 4096 Feb 22 00:23 django_06/
-rwxr-xr-x 1 ubuntu ubuntu  541 Feb 22 00:23 manage.py*
(django-venv) oliviaspark0825:~/workspace/PJT06 $ python manage.py startapp movie
(django-venv) oliviaspark0825:~/workspace/PJT06 $ \\
#앱의 models.py 에서 클래스 선언해주고
(django-venv) oliviaspark0825:~/workspace/PJT06 $ python manage.py makemigrations movie
Migrations for 'movie':
  movie/migrations/0001_initial.py
    - Create model Movie
(django-venv) oliviaspark0825:~/workspace/PJT06 $ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, movie, sessions
Running migrations:
    
    
    1,말모이,2224910,드라마
```

```sql
sqlite> .tables
#먼저 테이블을 확인하고

Movie                       auth_user_user_permissions
auth_group                  django_admin_log          
auth_group_permissions      django_content_type       
auth_permission             django_migrations         
auth_user                   django_session            
auth_user_groups            movie_movie    
#내가 models를 통해 만든 테이블 확인
sqlite> .schema movie_movie
CREATE TABLE "movie_movie" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(100) NOT NULL, "audience" integer NOT NULL, "genre" varchar(100) NOT NULL, "score" real NOT NULL, "poster_url" text NOT NULL, "description" text NOT NULL);
sqlite> .import data.csv movie_movie
sqlite> SELECT * FROM movie_movie
   ...> ;
# 테이블에 데이터 import 하기
sqlite> .import data.csv movie_movie
# 데이터 잘 들어가있는지 확인
sqlite> SELECT * FROM movie_movie


```

