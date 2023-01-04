# 템플릿을 표준 HTML 구조로 바꾸기

모든 템플릿 파일을 표준 HTML 구조로 변경하면 body 엘리먼트 바깥 부분은 모두 같은 내용으로 중복된다. 그리고 CSS 파일 이름이 변경되거나 새로운 CSS 파일이 추가되면 head 엘리먼트의 내용을 수정하려고 템플릿 파일을 일일이 찾아다녀야 하는 불편함도 있다.
이러한 불편함을 해소하기 위해 장고는 템플릿 상속(extends) 기능을 제공

## 템플릿 파일의 기본 틀 작성하기
templates/base.html 생성
```html
{% load static %}
<!doctype html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport"
        content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" type="text/css" href="{% static 'bootstrap.min.css' %}">
  <link rel="stylesheet" type="text/css" href="{% static 'style.css' %}">
  <title>Hello, pybo</title>
</head>
<body>
<!-- 기본 템플릿 안에 삽입될 내용 Start -->
{% block content %}
{% endblock %}
<!-- 기본 템플릿 안에 삽입될 내용 End -->
</body>
</html>
```
body 엘리먼트에 {% block content %}와 {% endblock %} 템플릿 태그가 있는데 이 부분이 base.html 템플릿 파일을 상속한 파일에서 구현해야 하는 영역이다.

## 질문 목록 템플릿 수정하기
templates/pybo/question_list.html
```html
<!-- 기존 코드 삭제 후 추가 -->
{% extends 'base.html' %}
{% block content %}
<div class="container my-3">
  ... 생략
</div>
{% endblock %}    <!-- 추가 -->
```
question_detail.html도 같은 방법으로 수정