
기존 question_list.html 템플릿에서 사용된 href를 보면
```python
<li><a href="/pybo/{{ question.id }}">{{ question.subject }}</a></li>
```
이러한 URL규칙을 사용했다. 하지만 이런 URL 규칙은 프로그램을 수정하면서 ‘/pybo/question/2/’ 또는 ‘/pybo/2/question/’으로 수정될 가능성도 있다. 이렇게 URL 규칙이 자주 변경된다면 템플릿에 사용된 모든 href 값들을 일일이 찾아 수정해야 한다. 
이게 URL 하드 코딩의 한계이다.
이런 문제를 해결하려면 해당 URL에 대한 실제 주소가 아닌 주소가 매핑된 URL 별칭을 사용해야 한다.


# URL 별칭으로 URL 하드 코딩 문제 해결하기

## pybo/urls.py 수정하여 URL 별칭 사용하기
pybo/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # 수정
    path('<int:question_id>/', views.detail, name='detail'),  # 수정
]
```
path 함수에 있는 URL 매핑에 name 속성을 부여했다. 이렇게 수정하면 실제 주소 /pybo/ 는 index라는 URL 별칭이, /pybo/2/는 detail이라는 URL 별칭이 생긴다.

## pybo/question_list.html 템플릿에서 URL 별칭 사용하기
앞에서 만든 별칭을 템플릿에서 사용하기 위해 /pybo/{{ question.id }}를 {% url 'detail' question.id %}로 수정한다.
mysite/templates/pybo/question_list.html
```html
{% if question_list %}
  <ul>
    {% for question in question_list %}
      <li><a href="{%  url 'detail' question_id %}">{{ question.subject }}</a></li>   <!-- 수정 -->
    {% endfor %}
  </ul>
{% else %}
  <p>질문이 없습니다.</p>
{% endif %}
```

# URL 네임스페이스 알아보기
현재는 프로젝트에서 pybo 앱 하나만 사용하지만, 이후 pybo 앱 이외의 다른 앱이 프로젝트에 추가될 수도 있다.
이때 서로 다른 앱에서 같은 URL 별칭을 사용하면 중복 문제가 생긴다.

이 문제를 해결하기 위해 pybo/urls.py 파일에 네임스페이스(namespace)라는 개념을 도입해야 한다.
namespace : 각각의 앱이 관리하는 독립된 이름 공간

## pybo/urls.py에 네임스페이스 추가하기
app_name 변수에 네임스페이스 이름을 저장하면 된다.
mysite/pybo/urls.py
```python
from django.urls import path
from . import views

app_name = 'pybo'       # 추가

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
]
```
현재 서버를 실행하면 NoReverseMatch at /pybo/ 오류가 발생한다.
왜냐하면 템플릿에서 아직 네임스페이스를 사용하고 있지 않기 때문이다.
{% url 'detail' question.id %} 을 {% url 'pybo:detail' question.id %} 로 수정한다

## pybo/question_list.html 수정하기
```html
  <ul>
    {% for question in question_list %}
      <li><a href="{%  url 'pybo:detail' question_id %}">{{ question.subject }}</a></li> <!-- 수정 -->
    {% endfor %}
  </ul>
```
detail에 pybo라는 네임스페이스를 붙여준 것이다. 
