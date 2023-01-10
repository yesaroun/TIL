
# CBV로 포스트 목록 페이지 만들기

## ListView로 포스트 목록 페이지 만들기
여러 포스트를 나열할 때는 ListView 클래스를 활용하면 된다.
index() 함수를 대체하는 PostList 클래스를 ListView 클래스를 상속해 만든다. 
이후 model은 Post라고 선언한다.
blog/views.py
```python
from django.shortcuts import render
from django.views.generic import ListView   # 추가
from .models import Post

# 추가
class PostList(ListView):
    model = Post

# 삭제
# def index(request):
#     posts = Post.objects.all().order_by('-pk')
# 
#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts': posts,
#         }
#     )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post': post,
        }
    )
```

## urls.py 수정하기
blog/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.single_post_page),
    path('', views.PostList.as_view),       # 추가
    # path('', views.index),                # 삭제
]
```

## 템플릿 파일 지정하기
여기서 서버를 실행해 '127.0.0.1:8000/blog/' 를 입력하면 TemplateDoseNotExist 오류 메시지가 나타난다.
blog/post_list.html이 필요한 것이다.
왜냐하면 장고에서 제공하는 ListView는 모델명 뒤에 '_list'가 붙은 html 파일을 기본 템플릿으로 사용하도록 설정되어 있다.
즉, Post 모델을 사용하면 post_list.html이 필요하다. 그래서 이 오류는 다음 두 가지 방법으로 해결할 수 있다.
하나는 PostList 클래스에서 template_name을 직접 지정하는 방법이고,
다른 하나는 post_list.html을 바로 만드는 것이다.

### 1. template_name 지정하는 방법
blog/views.py의 PostList 클래스에 template_name = 'blog/index.html'을 추가한다. 이는 이미 만들어 놓은 index.html을 활용하는 방법이다.
```python
class PostList(ListView):
    model = Post
    template_name = 'blog/index.html'
```
이렇게 수정하면 템플릿은 지정되었지만, 실제 포스트 목록 내용은 반영되지 않았다.
왜냐하면 이전에는 템플릿 파일에서 for 문으로 posts에 담긴 Post 레코드를 하나씩 나열했다.
템플릿에서 ListView로 만든 클래스의 모델 객체를 가져오려면 object_list 명령어를 사용하면 된다.
또는 Post 모델을 사용했으니 post_list라고 써도 자동으로 인식한다.
blog/templates/blog/index.html
```html
{% for p in post_list %}    # 수정
  <hr/>
  <h2><a href={{ p.get_absolute_url }}>{{ p.title }}</a></h2>
  <h4>{{ p.created_at }}</h4>
  <p>{{ p.content }}</p>
{% endfor %}
```

### post_list.html을 만드는 방법
그리고 템플릿 명을 명시하지 않으면 post_list.html을 템플릿으로 인식한다. 
views.py에서 template_name = 'blog/index.html'을 삭제한다.
```python
class PostList(ListView):
    model = Post
    # template_name = 'blog/index.html'     # 삭제
```
그리고 blog/templates/blog/index.html의 파일명을 post_list.html로 수정하면 된다.


## 최신 포스트부터 보여주기
앞에서 한 것처럼 최신 글을 맨 위로 배치하겠다. 
장고의 ListView는 이런 기능도 구현해준다.
ordering = '-pk'를 추가해준다. 이는 Post 레코드 중 pk 값이 작은 순서대로 보여달라는 뜻이다.
```python
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-pk'        # 추가


def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post': post,
        }
    )
```


# CBV로 포스트 상세 페이지 만들기

## DetailView로 포스트 상세 페이지 만들기
blog/views.py
```python
# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    ordering = '-pk'


class PostDetail(DetailView):
    model = Post

# def single_post_page(request, pk):        # FBV 방식
#     post = Post.objects.get(pk=pk)
#
#     return render(
#         request,
#         'blog/single_post_page.html',
#         {
#             'post': post,
#         }
#     )
```

## urls.py 수정
blog/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view()),      # 추가
    path('', views.PostList.as_view),
    # path('', views.index),
    # path('<int:pk>/', views.single_post_page),
]
```
blog/views.py에서 PostDetail 클래스를 정의하고, model = Post라고 정의만 했어도,  
이에 맞는 post_detail.html을 찾는다.  
현재 브라우저에서 127.0.0.1:8000/blog/1/을 입력하면 post_detail.html이 없어서 에러가 나온다.  
single_post_page.html의 파일명을 post_detail.html로 수정하면 성공적으로 상세 페이지가 나타난다.








