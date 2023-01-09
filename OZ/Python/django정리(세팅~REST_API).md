# Django 프로젝트 세팅

## poetry 세팅
```zsh
# poetry를 이용한 가상 환경 설정
# 해당 폴더에서
poetry init

# django 설치
poetry add Django
```

#### pyproject.toml
관련 링크 [poetry-pyproject.toml](https://python-poetry.org/docs/pyproject/)
Django 프로젝트 환경에 대한 정보를 담고 있는 파일   
package.json 파일과 같은 역할

### 가상환경에서 django 실행
```zsh
poetry shell    # 가상환경 접속
django-admin    # 가상환경의 django 실행
deactivate      # 가상환경만 종료
exit            # 터미널 및 가상환경 종료
```

### django 프로젝트 생성
```zsh
django-admin startproject config .    # 현재 폴더에 프로젝트 생성
```

## django 서버 실행
```zsh
python manage.py runserver
```

### admin 계정 생성
```zsh
python manage.py createsuperuser
```


# django 모델 개념
## Model
### 모델이란
- DB에서 하나의 테이블과 같은 개념
- django 모델을 통해 sql 없이도 데이터베이스 생성 및 수정이 가능하다.
- 모델이라는 객체를 사용해 프로그램에 명령은 내리는 방식

### app 생성
```zsh
python manage.py startapp users     # users라는 모델을 생성
```

__파일 구조__
- admin.py : 관리자 페이지 관련
- apps.py : 메인 파일
- models.py : 모델 관련 파일
- views.py : 화면을 그려주는 파일

#### config/settings.py에 users.app 등록하기
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig',      # users.apps 경로 가면 UsersConfig 메서드 존재하고, 이 메서드 등록하기
]
```

#### users/models.py 에 Model을 상속받는 클래스 작성
```python
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20)  # Model을 상속받는다.
    description = models.TextField()        # 긴 텍스트 문장
    age = models.PositiveIntegerField()     # 양의 정수형
    sex = models.CharField(max_length=10)
    is_business = models.BooleanField(default=False)
```

[Model field reference](https://docs.djangoproject.com/ko/3.2/ref/models/fields/)
꼭 보기! (내가 정리한 것도 다른 폴더에 있음!!!)

#### users/admin.py 에 models 등록
```python
from django.contrib import admin

class UserAdmin(admin.ModelAdmin):
    pass
```
이렇게 한 이후 모델을 DB에 migrate해줘야 한다.  
makemigrations : 새로 생성한 모델 또는 모델의 데이터에 변경사항이 있을 때 Django 에 알려주는 역할  
migrate : Django에 알려준 새로 생성한 모델 또는 변경된 모델에 대한 데이터를 DB에 적용시키는 명령어


## Admin Panel 관리
### 패널에 보이는 이름 관리 
```python
# users/models.py

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20)  
    description = models.TextField()       
    age = models.PositiveIntegerField()   
    sex = models.CharField()

    def __str__(self):          #
        return self.name
```

### 테이블의 컬럼 추가(admin페이지에서 보이는 컬럼)
users/admin.py
```python
from django.contrib import admin
from .models import Users

@admin.register(User)   # UserAdmin에 등록할 Model 지정(Decorator)
class UserAdmin(admin.ModelAdmin):              # ModelAdmin을 상속
    list_display = ["name", "age", "sex", ]     # 테이블의 컬럼 추가(admin페이지에서 보이는 컬럼)
    list_filter = ["sex", "is_business"]        # 필터 추가 
    search_fields = ["name"]                    # 검색 기능 추가
```


## Admin 유저 상속받기
[Customizing authentication in Django](https://docs.djangoproject.com/en/4.1/topics/auth/customizing/)
위 공식 문서 꼭 보기!!
- 이미 장고에서 제공하는 비밀번호를 해쉬화, 비밀번호 저장 등의 기능을 굳이 직접 만들지 않고, 있는 기능 활용하기!!!

#### users/models.py 수정
```python
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    name = models.CharField(max_length=150)
    is_business = models.BooleanField()
```
#### users/admin.py 
```python
from .models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # fields = ("email", "password", "name", "is_business")
    fieldsets = (
        ("Profile", {
                "fields": ("password", "name", "email", "is_business", "gender"),
                "classes": ("wide",),
            },
        ),
        ("Permissions",{
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "user_permissions",
                ),
            },
        ),
        ("Important Dates", {
                "fields": ("last_login", "date_joined"),
                "classes": ("collapse",),
            },
        ),
    )

    list_display = ("username", "email", "name", "is_business",)
```
#### config/settings.py
```python
AUTH_USER_MODEL = "users.User"      # 맨 밑에 추가
```

[The Django admin site](https://docs.djangoproject.com/ko/3.2/ref/contrib/admin/)
장고 admin 관련 문서!!!










