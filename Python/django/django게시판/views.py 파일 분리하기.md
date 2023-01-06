# 1. views.py 파일 분리하기
이 방법은 views.py 파일을 분리하고, 나머지 파일을 수정하지 않는 방법이다.  
이 방법이 전체 코드의 변화가 가장 적다.


### views 디렉터리 생성하기
pybo/views 디렉터리 생성

### views.py 파일을 분리해 views 디렉터리에 각각 저장하기
views.py 파일에 정의한 함수를 기능별로 분리하여 views 디렉터리에 아래 표처럼 저장

| 파일명               | 기능    | 함수                                                         |
|-------------------|-------|------------------------------------------------------------|
| base_views.py     | 기본 관리 | index, detail                                              |
| question_views.py | 질문 관리 | question_create, question_modify, question_delete          |
 | answer_views.py   | 답변 관리 | answer_create, answer_modify, answer_delete                |
 | comment_views.py  | 댓글 관리 | comment_create, question, ..., comment_delete_answer(총 6개) |


### base_views.py 파일 작성

