## page 디렉티브 buffer 속성 및 autoFlush

### cf) JSP 출력 buffer

JSP는 기본적으로 페이지 처리결과를 곧바로 클라이언트로 출력하여 응답하지 않고, 출력 버퍼에 모아두었다가 한꺼번에 응답합니다.

![[Pasted image 20221117024624.png]]

**버퍼 사용시 장점** 굳이 곧바로 출력하지 않고 버퍼에 모아두었다가 처리하는 이유는 다음과 같은 장점들이 있기 때문입니다.

**성능 향상** 버퍼에 처리 결과를 모아두었다가 한꺼번에 출력하게 되면 출력 성능이 향상되는데, 처리 결과를 그때그때 조금씩 출력하게 되면 출력 한번한번에 소모되는 비용이 여러번에 반복돼 소모되기 때문에 불필요한 동작들이 발생하게 되는데, 모아두었다가 큰 덩어리로 한번에 출력하게 되면 출력에 관련된 비용을 한번만 사용하면 되는 장점이 있습니다.

**최종 출력 이전에 처리 결과 수정 가능** 버퍼를 사용하지 않고 데이터를 바로 출력해 버리면 엎질러진 물처럼? 중간에 출력 내용을 수정할 수 없습니다. JSP가 처리된 결과는 결국 최종적으로는 HTTP 응답 메시지입니다. 응답 메시지에는 응답 헤더와 응답 본문이 있는데 out 객체나 표현식을 통해 곧바로 출력되버린 결과는 서버를 떠나버렸기 때문에 헤더와 본문등을 수정하고 싶어도 수정이 불가능합니다. 그러나 버퍼를 이용하면 버퍼에 모아두는 중간에 HTTP 응답 헤더등의 수정이 가능해 지는 장점이 있습니다.

\<jsp:forward> 기능이나 에러 처리에 용이**

만약 a.jsp 라는 페이지가 존재하고 보통의 경우에는 a.jsp에서 모든 처리를 다 하지만 특정 조건의 경우에는 b.jsp로 포워딩(forwarding) 해야 하는 경우가 생기면 어떻게 해야할까요? 버퍼가 없는 경우에는 a.jsp에서 일부 처리결과를 클라이언트로 전송해버린 상태에서 b.jsp로 제어가 넘어가서 b.jsp에서 처리된 결과또한 섞여서 출력될 것입니다.

그러나 버퍼를 이용하면 a.jsp의 처리 결과를 출력하던 도중에 특정 조건에서 b.jsp로 포워딩 될 때 출력 버퍼를 비워버리고 제어가 넘어간 b.jsp에서 처리된 결과를 클라이언트로 출력하면 됩니다.

**JSP에서 버퍼 이용 방법**

JSP는 기본적으로 8kb의 버퍼를 사용하도록 되어 있습니다. 만약 버퍼를 제어하고 싶은 경우 page 디렉티브의 두 가지 속성을 이용하면 됩니다. ->

**[[서블릿/JSP] page 디렉티브 사용법 및 속성 설명](http://dololak.tistory.com/137)**

버퍼와 관련된 속성으로 buffer속성과 autoFlush 속성이 있습니다.

```html
<%@ page buffer="8kb" autoFlush="true" %>
```

**buffer 속성**은 버퍼 크기를 kb 단위로 지정할 수 있습니다. 기본적으로 buffer 속성을 통해 크기를 명시해주지 않아도 8kb의 버퍼가 사용되며, 만약 버퍼를 사용하지 않는 경우 none으로 지정해주면 됩니다.

**autoFlush 속성**은 출력 결과가 버퍼에 가득 찼을 경우의 행동을 지정해주는데 true인 경우 버퍼가 가득 차면 버퍼의 내용을 클라이언트로 전달하고 버퍼를 비우게 되며, false인 경우에는 버퍼가 다 찼을 때 IOException(입출력 예외)을 발생시키고 작업을 중단하게 됩니다.

-   버퍼의 내용을 출력하고 버퍼를 비우는 행위를 flush라고 합니다.

출처 : [](https://dololak.tistory.com/151)[https://dololak.tistory.com/151](https://dololak.tistory.com/151)

## include 디렉티브

Test002.jsp

```html
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <meta charset="UTF-8">
    <title>Test002.jsp</title>
</head>
<body>

<div>
    <h1>include 디렉티브 실습</h1>
    <hr>
</div>

<%@ include file="Test003.jsp" %>
<br><br>

<div>
    <h2><%=str %></h2>
    <h2><%=name %></h2>
</div>

</body>
</html>
```

Test003.jsp

```html
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%
  String str = "include 디렉티브와 관련된 실습 진행중";
  String name = "lee";
%>
<html>
<head>
    <meta charset="UTF-8">
    <title>Test003.jsp</title>
</head>
<body>

<div>
  <p>Test002.jsp와는 다른 독립적인 페이지</p>
</div>

</body>
</html>
```