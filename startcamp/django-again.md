# django-again

# 수업

URL : 자원의 위치가 있으면

URI

```python
(django-venv) oliviaspark0825:~/workspace $ cd PROJECT03
(django-venv) oliviaspark0825:~/workspace/PROJECT03 $ LS
bash: LS: command not found
(django-venv) oliviaspark0825:~/workspace/PROJECT03 $ django-admin startproject crud .
    # settings.py에 꼭 앱 등록 해야함
(django-venv) oliviaspark0825:~/workspace/PROJECT03 $ python manage.py startapp board
(django-venv) oliviaspark0825:~/workspace/PROJECT03 $ c9 open .gitignore
(django-venv) oliviaspark0825:~/workspace/PROJECT03 $ python manage.py makemigrations 
Migrations for 'board':
  board/migrations/0001_initial.py
    - Create model Board
(django-venv) oliviaspark0825:~/workspace/PROJECT03 $ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, board, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying board.0001_initial... OK
  Applying sessions.0001_initial... OK
(django-venv) oliviaspark0825:~/workspace/PROJECT03 $ python manage.py check
System check identified no issues (0 silenced).
# admin 설정하기
admin.py 들어가서
'''
from django.contrib import admin
from .models import Board

# Register your models here.
class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at', 'updated_at')
    
admin.site.register(Board, BoardAdmin)
'''

(django-venv) oliviaspark0825:~/workspace/PROJECT03 $ createsuperuser
bash: createsuperuser: command not found
(django-venv) oliviaspark0825:~/workspace/PROJECT03 $ python manage.py createsuperuser
사용자 이름 (leave blank to use 'ubuntu'): heyhey
이메일 주소: suhyunpark0825@gmail.com
Password: 
Password (again): 
비밀번호가 너무 짧습니다. 최소 8 문자를 포함해야 합니다.
Bypass password validation and create user anyway? [y/N]: olivia0012
Password: 
Password (again): 
Error: Your passwords didn't match.
Password: 
Password (again): 
Superuser created successfully.
```

