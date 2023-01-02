# 장고 Admin 사용하기

장고 Admin을 사용하려면 super user를 먼저 생성해야 한다. super user는 장고 운영자 계정이라고 생각하면 된다.

## 슈퍼 유저 생성하기

```python
% python manage.py createsuperuser
Username (leave blank to use 'akor1'): admin
Email address: akor1@naver.com  
Password: 1234
Password (again): 1234
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

실제 사이트를 운영한다면 보안에 취약한 비밀번호를 사용해서는 안된다.

[localhost:8000/admin](http://localhost:8000/admin) 에 접속하고 로그인하면 관리자 페이지 나온다.

## 장고 Admin에서 모델 관리하기

모델들을 장고 Admin에 등록하면 손쉽게 모델을 관리할 수 있다. 이전에 장고 셸에서 수행했던 작업을 장고 Admin에서 할 수 있다. 

pybo/admin.py

```python
from django.contrib import admin
from .models import Question

admin.site.register(Question)
```

이렇게 작성하고 장고 Admin으로 Question 모델이 추가되어 있다. 그러면 셸이 아닌 장고 Admin 화면에서 Question 모델을 직관적으로 관리할 수 있다.

## 장고 Admin에 데이터 검색 기능 추가하기

pybo/admin.py

```python
from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)
```

제먹을 검색할 수 있도록 검색 항목을 추가했다. QuestionAdmin 클래스를 추가하고 search_fields에 ‘subject’를 추가했다.
그러면 장고 Admin을 새로고침하면 검색 기능이 추가되었다.