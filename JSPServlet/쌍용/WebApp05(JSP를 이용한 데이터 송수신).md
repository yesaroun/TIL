## GET 방식과 POST 방식(데이터 전송 / 페이지 요청)

### ○ GET 방식

ex)\https://n.news.naver.com/article/005/0001518197?cds=news_media_pc
가. \https://n.news.naver.com/article/005/0001518197 ? → 요청 페이지 
나. \cds=news_media_pc (『&』 있을 수도 있고 없을수도) → 전송 데이터

-   GET 방식은 엽서를 보내는 방식가 유사한 전송 / 요청 방식 (post는 편지와 유사/ 엽서는 주소도 보이고 적은 내용이 뒷면에 다 보임/ 편지는 주소만 보이고 안에 내용물을 볼 수 없다)
-   주소 + 데이터(모두 노출)
-   전송할 데이터를 문자열 형태(Query String)로 URL 뒤에 인수로 붙여서 전송을 수행하는 방법(방식)이다.
-   URL 뒤에 인수로 붙어있는 내용을 누구나 볼 수 있고 이로 인해 보안성이 취약하다고 할 수 있다.
-   또한, GET 방식은 보낼 수 있는 데이터 량의 한계가 있기 때문에(과거) 많은 데이터를 보내는 경우 일정 크기 이상에서는 잘림 현상이 발생한다.(길이 제한을 가진다는 의미이다. URL 최대 길이 2048char(인터넷 익스플로러말고는 현재는 길이 제한이 없다. 그래도 얼마전까지만 해도 길이 제한이 있었어서 길이 제한이 있는것처럼쓴다))
-   특히나 \<form> 태그에서의 GET 방식은 서버로 데이터를 전송하는 과정에서 서버 처리가 지연될 경우 중복해서 요청이 이루어진다는 문제가 발생할 수 있다는 단점을 가지고 있다.
-   형식 및 구조 『URL주소?속성=데이터&속성=데이터&....』 『URL주소?name=value&tel=value2&...』
-   GET 방식은 select 적인 성격(성향)을 가지고 있다. 서버에서 데이터를 가지고 와서 보여준다거나 하는 용도로 주로 사용한다. 서버의 값이나 상태를 바꾸는 용도로는 사용하지 않는다. 즉, 단순 페이지 요청에 많이 사용된다는 것이다.
-   GET 방식의 장점은 여러가지 형태를 통해 간편한 데이터 전송이 가능하다는 것이다. POST 방식처럼 form 태그를 사용하여 전송도 하고, 링크에 직접 걸어 사용해도 되고, 주소창에 직접 입력해도 된다. 
	ex) 
	\<a href="\http://url?키=값&키=값"> 
	\<form action="\http://url?키=값&키=값"> 
	window.open(href="\http://url?키=값&키=값");
	window.location.href="\http://url?키=값&키=값"; 
	window.location.replace("\http://url?키=값&키=값"); 
	(단점이 많지만 간편한 데이터 전송이라는 장점이 엄청나게 크다)

○ POST 방식 
	ex) \http://localhost:8090/WebApp06/Test001.jsp
-   주소만 노출 / 데이터는 숨김
-   \<form> 태그에서 method 속성을 "post"로 설정해서 요청
-   파일의 형태로 전송되기 때문에 URL 상에서는 내용이 나타나지 않는다. 이로 인해 GET 방식에 비해 보안성이 높다고 할 수 있다.
-   POST 방식은 HTTP Body 안에 숨겨져서 전송된다.
-   GET 방식처럼 URL 뒷부분에 추가해서 보내는 것이 아니라 HTTP Body 안에 넣어서 보내기 때문에 GET 방식에서 발생할 수 있는 보안성 문제를 어느정도 해결할 수 있다.
-   GET 방식에 비해 대용량의 데이터를 전송할 때 사용한다.
-   \<form> 태그를 이용해서 submit 하는 일반적인 형태가 POST 방식이다.
-   POST 방식은 서버의 값이나 상태를 바꾸기 위해 주로 사용한다. 글쓰기를 하게 되면 글의 내용이 데이터베이스에 저장되고 수정을 하게되면 데이터베이스에 수정된 값이 적용될 수 있도록 처리하는 구성인 것이다.

◎ HTTP 헤더와 바디 
	헤더는 정보, 바디는 내용


## JSP를 이용한 데이터 송수신

ex) Aaa.html → Bbb.jsp Aaa.html → Bbb.java(Servlet) Aaa.jsp → Bbb.jsp Aaa.jsp → Bbb.java(Servlet) (html은 클라이언트 언어여서 데이터 수신이 불가) Aaa(보내는 쪽) 페이지에서는 \<form> 태그 및 action, method 속성 필요(method속석 생략시 get방식)  
\<input> 이나 \<button> 태그의 type="submit" 속성 필요 Bbb(받는 쪽) 페이지에서는 request 객체의 getParameter() 메소드 필요

1.  request 내부 객체 request 내부 객체는 웹 브라우저에서 JSP(또는 Servlet) 페이지로 전달되는 정보의 모임으로 HTTP 헤더와 HTTP 바디로 구성되며, 웹 컨테이너는 요청된 HTTP 메세지를 통해 HttpServletRequest 객체 타입인 request 객체로 사용한다. 즉, request 객체는 웹 브라우저가 JSP(또는 Servlet) 페이지로 보내진 내용에 대한 정보를 갖고 있는 내부 객체인 것이다.
    
2.  String getParameter(name) 이름이 name인 파라미터에 할당된 값을 리턴하며 지정된 파라미터 값이 없는 경우 null을 리턴한다.
    
3.  String[] getParameterValues(name) 이름이 name인 파라미터의 모든 값을 String 배열로 반환한다. 주로 checkbox 등 동일한 이름을 사용하는 form 태그의 값을 리턴받기 위해 사용한다.
    
4.  void setCharacterEncoding(encode) 전송된 데이터의 문자 인코딩 방식을 지정한다.
    

## Hap.jsp → HapOk.jsp

\<form>의 action속서 지정 시[HapOk.jsp]로 지정해도 되고 [/WebApp05/HapOk.jsp]형태로 지정해도 된다. 단, [/HapOk.jsp]로 지정하면 안된다.

```html
<form action="HapOk.jsp" method="post">
<!-- 또는 -->
<form action="/WebApp05(프로젝트경로)/HapOk.jsp" method="post">
```

다른 페이지로부터 넘어온 데이터를 수신할 때, 문자열로 받아오기 때문에 형변환을 해야 한다. 이 과정에 예외 처리를 해주는 것이 좋다.

```java
try {
    int n1 = Integer.parseInt(str1);
} catch (Exception e) {
    // 예외 발생 시 클라이언트의 브라우저 화면에 출력되지 않고,
    // 서버의 컨솔 창에 오류 메시지가 나오도록 구성된다.
    System.out.println(e.toString());
}
```

이렇게 예외 처리를 한 이후 정수 형태의 숫자가 아닌 변환이 불가능한 문자나 빈 공백을 입력했을 때 결과 확인 버튼 클릭 시 클라이언트의 화면 처리 결과를 try ~ catch 블럭에 의해 항상 0으로 출력된다.

## RadioSelect.jsp → RadioSelectOk.jsp

대표적인 예시

RadioSelct.jsp

```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" type="text/css" href="css/main.css">
</head>
<body>
<div>
    <h1>JSP를 이용한 데이터 송수신 실습 03</h1>
    <hr>
    <p>RadioSelect.jsp 0 -> RadioSelectOk.jsp </p>
</div>
<div>
    <h2>radio, select 데이터 전송</h2>

    <form action="RadioSelectOk.jsp" method="post">
        이름 <input type="text" name="name" class="txt">
        <br>
        
        성별
        <label><input type="radio" value="M" name="gender">남자</label>
        <label><input type="radio" value="F" name="gender">여자</label>
        <br><br>

        정공
        <select name="major" id="">
            <option value="국문학">국문학</option>
            <option value="영문학">영문학</option>
            <option value="컴퓨터공학">컴퓨터공학</option>
            <option value="수학">수학</option>
            <option value="신문방송학">신문방송학</option>
            <option value="경영학">경영학</option>
        </select>
        <br><br>
        
        취미
        <select name="hobby" size="6" multiple="multiple" id="">
            <option value="영화감상">영화감상</option>
            <option value="음악감상">음악감상</option>
            <option value="공원산책">공원산책</option>
            <option value="배낭여행">배낭여행</option>
            <option value="스노클링">스노클링</option>
            <option value="암벽등반">암벽등반</option>
            <option value="종이접기">종이접기</option>
        </select>
        <br><br>

        <input type="submit" value="내용 전송" class="btn control">
    </form>
</div>
</body>
</html>
```

RadioSelectOk.jsp

```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%
  // 스크립트 릿 영역 -> 이전 페이지(RadioSelect.jsp)로부터 전송된 데이터 수신

  request.setCharacterEncoding("UTF-8");
  // value가 한글이여서 한글 깨짐 방지 처리

  String nameStr = request.getParameter("name");
  String genderStr = request.getParameter("gender");
  String majorStr = request.getParameter("major");
  //-- 선택 상자 (다중 선택이 아니니까) 단일값 수신
  String[] hobbyArr = request.getParameterValues("hobby");
  //-- 다중 선택이 가능한 선택상자일 경우
  // [getParameterValues()]로 데이터 수신 -> 배열 반환

  // gender 수신 및 처리
  String gender = "";
  if (genderStr.equals("M"))
    gender = "남자";
  else if (genderStr.equals("F"))
    gender = "여자";
  else
    gender = "확인불가";

  // hobby 수신 및 처리
  String hobby = "";
  if (hobbyArr != null) {
    for (String item : hobbyArr)
      hobby += " [" + item + "]";
  }
%>
<html>
<head>
  <meta charset="UTF-8">
  <title>Title</title>
  <link rel="stylesheet" type="text/css" href="css/main.css">
</head>
<body>
<div>
  <h1>JSP를 이용한 데이터 송수신 실습 03</h1>
  <hr>
  <p>RadioSelect.jsp -> RadioSelectOk.jsp</p>
</div>
<div>
  <h2>radio, select 데이터 수신 결과 학인</h2>

  <div>
    <p>이름 : <%=nameStr %></p>
    <p>성별 : <%=genderStr %>(<%=gender %>)</p>
    <p>전공 : <%=majorStr %></p>
    <p>취미 : <%=hobby %></p>
  </div>
</div>
</body>
</html>
```

## Table.jsp → TableOk.jsp

table 생성하기

Table.jsp

```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <meta charset="UTF-8">
    <title>Table.jsp</title>
    <link rel="stylesheet" type="text/css" href="css/main.css">
</head>
<body>

<div>
    <h1>JSP를 이용한 데이터 송수신 실습 05</h1>
    <hr>
    <p>Table.jsp 0 -> TableOk.jsp </p>
</div>

<div>
    <form action="TableOk.jsp" method="post">
        <table class="table">
            <tr>
                <th>가로</th>
                <td>
                    <input type="text" name="su1" class="txt">
                </td>
            </tr>
            <tr>
                <th>세로</th>
                <td>
                    <input type="text" name="su2" class="txt">
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <button type="submit" class="btn control" style="width: 100px">
                        결과 확인
                    </button>
                </td>
            </tr>
        </table>
    </form>
</div>

</body>
</html>
```

TableOk.jsp

```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%
  // 데이터 수신(스크립트 릿)
  String s1 = request.getParameter("su1");
  String s2 = request.getParameter("su2");

  int n1 = 0;
  int n2 = 0;

  // 테이블 안에서 1씩 증가시켜 나갈 변수 선언 및 초기화
  int n = 0;

  try {
    // 수신된 데이터 형변환
    n1 = Integer.parseInt(s1);
    n2 = Integer.parseInt(s2);
  } catch (Exception e) {
    System.out.println(e.toString());
  }
%>
<html>
<head>
    <meta charset="UTF-8">
    <title>TableOk.jsp</title>
    <link rel="stylesheet" type="text/css" href="css/main.css">
</head>
<body>

<div>
  <h1>JSP를 이용한 데이터 송수신 실습 05</h1>
  <hr>
  <p>Table.jsp -> TableOk.jsp 0 </p>
</div>

<div>
  <table border="1">
    <%
      for (int i = 0; i < n2; i++) {
    %>
      <tr>
        <%
          for (int j = 0; j < n1; j++) {
        %>
        <td style="width: 70px;">칸</td>
        <%
          }
        %>
      </tr>
    <%
      }
    %>
  </table>
</div>

</body>
</html>
```