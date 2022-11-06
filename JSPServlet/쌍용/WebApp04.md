#웹어플리케이션 #JSP개념 #스크립트릿 #Servlet실습

# 웹 어플리케이션

어떤 방식으로 요청했느냐에 따라 같은 페이지지만 다른 응답을 내놓을 수 있다. 이것이 웹 어플리케이션이다. 서로 다른 접근자가 접근했을 때 같은 화면을 내놓는다면 이것은 웹 어플리케이션이라고 할 수 없다.

### 웹 어플리케이션의 개념

웹 어플리케이션은 웹 브라우저의 요청에 대하여 처리한 결과를 보여주는 프로그램을 의미한다. 사용자가 어떤 상태로 무엇을 요청했느냐에 따라 스스로 판단하여 자동으로 각각에 대한 처리 결과를 보여주는 프로그램이다.

### 웹 어플리케이션의 구성 요소

1.  웹 브라우저
2.  웹 서버(WAS : Web Application Server)
-   웹 서버란 웹 브라우저를 이용하여 World Wide Web을 상요하는 클라이언트에게 미리 저장된 하이퍼텍스트(Hyper Text)를 제공하는 서버이다.
-   대표적으로는 MS 기반의 IIS 서버와 유닉스 기반의 아파치 서버 등이 있다.
3.  어플리케이션 서버
-   처리 결과값을 웹 서버에 전달
-   클라이언트가 어떤 페이지를 요청했느냐에 따라 그 문서를 동적으로 만들어 전달
-   JSP, Servlet 등으로 동적 웹 페이지 구축
4.  데이터베이스

### 웹 어플리케이션의 구분

1.  어플리케이션의 서버 방식
-   웹 어플리케이션 서버를 통해 간접적으로 웹 어플리케이션 프로그램을 실행한다.
-   대용량 처리에 유리하며, CGI(Common Gateway Interface) 방식에 비해 메모리 사용량이 적다.
2.  스크립트 방식
-   코드 형태 : 컴파일 되지 않은 스크립트 코드
-   실행 방식 : 스크립트 코드를 해석한 뒤 실행
-   코드 변경 : 스크립트 코드만 수정

### 웹 어플리케이션

1.  Servlet(Server + Applet)
-   SUN 사에서 내놓은 기술로서 JAVA라는 언어를 기반으로 하여 동적인 컨텐츠를 생산하는 기술 JAVA라는 코드 안에 HTML 태그가 혼재되어 있어 효율성이 다소 떨어질 수 있다. → JAVA가 HTML을 품고 잇는 형태. 확장자는 .java → .class

2.  JSP(Java Server Page)
-   JSP 또한 JAVA 라는 언어를 기반으로 하여 만들어진 것이지만, ASP, PHP 처럼 동적인 컨텐츠를 생성하기 위해 스크립트 언어 형식으로 프로그램을 작성할 수 있어서 개발자에게 비교적 쉬운 개발을 할 수 있게 한다. 사용자가 직접 태그를 정의해서 사용할 수 있는 사용자 정의 태그를 지정할 수 있는 기능도 갖고 있다. → HTML 이 JAVA 를 품고 있는 형태. 확장자는 .jsp → .html 서블릿이 구버전 JSP 신버전 기술 어떤 계층이냐에 따라 서블릿이 사용되기도, JSP가 사용되기도 모든 JSP는 서블릿으로 변환된다. 즉 순수한 JSP는 없다.

# JSP(Java Server Pages)

### 1. JSP(Java Server Pages) : 웹 프로그램 작성 언어의 한 종류

JSP(Java Server Pages)는 동적(Dynamic)인 웹 페이지를 비교적 간단히 만들 수 있는 방법을 제공하는 자바 기반으로 하고 있는 스크립트 언어(Server Side Script)로 자바 엔터프라이즈 어플리케이션에서 UI(User Interface) 영역을 담당하고 있다. JSP는 자바를 서버 환경에서 사용하는 스크립트 방식의 언어로 단일 스레드로 클라이언트의 요청에 서비스한다. 요청이 있을 때마다, 즉, 객체가 생성될 때 마다 프로세스를 생성하는 기존의 CGI와는 달리 하나의 메모리를 공유하면서 서비스되는 원리를 갖고 있다. 이러한 원리는 서버측 부하를 줄여주며, JSP 내부에는 보여주는 코드만 작성하고 직접 작업하는 부분은 자바 빈으로 구성하여 둘을 분리할 수 있다. 이는 서로 영향을 주지 않으면서수정할 수 있는 장점을 취하며, JAVA가 갖고 있는 장점인 재사용성을 높일 수 있게 한다. 
클라이언트 <---------------------------> 서버 
HTML, CSS, Javascript <--------------> JSP(JAVA) 
브라우저(IE, CR, FF 등) <---------------> 웹서비스(톰캣), 오라클 
요청 <---------------------------------> 응답(HTML 웹페이지)

### 2. JSP 실행 구조

1단계. 웹 클라이언트에서 웹 서버에 웹 프로그램(페이지) 요청 2단계. 웹 서버에서 웹 클라이언트가 요청한 JSP 프로그램(페이지) 로드 3단계. JSP 페이지에 대한 변환 실행 ※ 이 과정에서 일반 『.java』인 파일로 변환된다. 『→ Servlet』 4단계. 『.java』인 파일로 변환된 Servlet 의 컴파일(.class) 및 실행 5단계. 실행 결과로 동적 생성된 HTML Document를 클라이언트 측에 응답 6단계. 웹 클라이언트는 응답받은 HTML Document를 브라우저에서 웹 페이지 형태로 출력

### 3. 이클립스 JSP 개발 환경 구축

1.  프로젝트(new) 생성 시 『Dynamic Web Project』 선택
2.  프로젝트 명 입력 시 식별자 작성 규칙을 준수 원래 규칙에 따르면 『JspTest001.jsp』와 같이 명명해야 하지만, 클라이언트 측에서 (대소문자 구분없이) 좀 더 편하게 상요할 수 있도록 일단 지금은 『jsptest001.jsp』와 같이 명명한다.
3.  Target Runtime 지정 → 톰캣 설치 디렉터리 연결
4.  프로젝트 생성 후에는 Server 탭에서 톰캣 서버 등록 (단, 서버를 새로 등록했을 경우 서버 관련 설정을 재구성)
5.  톰캣 서버에 프로젝트 등록 → add and remove
6.  톰캣 서버 시작(재시작) ※ 이 시점에서 포트번호 설정 및 확인 필요 (오라클이 웹 상에서 port8080 을 사용하기 때문에 충돌 방지) 『Project Explorer』 의 『Server』 디렉터리 노드를 확장하면 『server.xml』 파일이 존재하며, 이 파일을 열어 63 ~ 65 정도의 라인 내용을 수정한다

```xml
 <Connector URIEncoding="UTF-8" ... port="8090" />
	    ------------------              ----------
		↑추가		                    	↑수정(기본 8080)
  ※ xml 파일을 수정한 이후에는 반드시 서버를 지시작해야 한다. check~!!!
```

1.  JSP 페이지 작성(확장자 『.jsp』) → WebContent 디렉터리 하위에 작성 ※ 페이지 작성 전에 Encoding 방식을 체크 및 설정한다. (UTF-8) ※ JSP 기본 페이지의 템플릿을 HTML5 기반으로 수정하여 설정한다.(기본 HTML 4.01)
    
2.  톰캣 서버가 실행되고 있는 상태에서 웹 브라우저의 URL 주소 창에 다음과 같은 주소를 요청한다. (클라이언트 입장)
    
    \http://서버주소:포트번호/프로젝트이름/파일이름.jsp
    \http://localhost:8090/WebAppxxx/jsptest001.jsp
    127.0.0.1 ※원격 접속인 경우는 localhost(127.0.0.1) 대신 목적지 서버의 IP Address 를 작성해야 한다.
    

## JSP 구성 요소

### 1. 디렉티브(지시어)

-   페이지에 대한 설정 정보 지정. 클래스 속성을 변경. \<%@ %\>

page 페이지에 대한 기본 정보 입력 (생성하는 문서의 타입, 출력 버퍼의 크기, 에러 페이지 등) 현재 문서를 나타내는 객체. page 디렉티브는 JSP 페이지와 관련된 속성을 정의하고 이 속성들은 웹 컨테이너 정보를 제공한다. 또한, 한 페이지에 page 디렉티브는 여러 번 등장할 수 있고 위치도 관계가 없다. 하지만 보통 페이지 상단에 기술한다. 주요 속성
-   language : 스크립트 코드에서 사용되는 프로그래밍 언어 지정
-   contentType : 생성할 문서 타입
-   import : 사용할 자바 클래스 지정
-   session : 세션 사용 여부 지정
-   buffer : 출력 버퍼 크기 지정
-   autoFlush : 출력 버퍼가 다 채워졌을 경우 자동으로 버퍼에 있는 데이터를 비우게 만들지의 여부 지정
-   info : 페이지에 대한 설명
-   errPage : 실행 도중 에러 발생시 보여줄 페이지 지정
-   pageEncoding : 페이지 자체의 캐릭터 인코딩 지정

taglib 
태그 라이브러리(tag library) 사용자가 만든 태그 모음(사용자가 직접 기능 설정)

include 
다른 문서를 포함하는 기능 여러 JSP 페이지에서 공통적으로 포함하는 내용이 있을 때 이러한 내용을 매번 반복해서 입력하지 않고 별도의 파일에 저장해 두었다가 JSP 파일에 삽입하도록 하는 것 → 생산성 향상 
include 디렉티브 처리 과정은 정적으로 include 지시자를 사용한 JSP 페이지가 컴파일 되는 과정에서include 되는 JSP 페이지 소스 내용을 그대로 포함해서 컴파일한다. 
즉, 복사&붙여넣기 방식으로 두 개의 파일을 하나로 구성한 후 같이 변환되고 컴파일 된다.

### 2. 스크립트 요소

-   스크립트 릿(Scriptlet) 
  JSP 에 자바 코드를 기술 
  <% %> 
  JSP 문서 내에 JAVA 코드를 기술하는 부분이기 때문에 오로지 자바 코드만 올 수 있다. 
  스크립트 릿에 선언된 변수는 지역 변수의 성격을 가지게 되며(서블릿 안에 있는 service() 메소드 안에 선언된 변수이므로) 자바에서 메소드 내에 선언된 변수라고 할 수 있다.
-   표현식(Expression) 
  HTMl 문서 결과값에 포함시키고자 할 때 사용 
  <%= %> 
  (즉, 브라우저에 등장시킬 수 있는 영역)
-   선언부(Declaration) 
  스크립트 릿이나 표현식에서 사용할 수 있는 함수 작성 시 사용. 
  <%! %> 
  스크립트 릿이나 표현식에서 사용할 수 잇는 변수나 메소드를 정의하는 부분이기 때문에 선언부에서 선언된 변수는 서블릿으로 변환되는 과정에서 멤버 변수의 입장을 취하게 되며 전역 변수의 성격을 가진다. 또한, 『_jspInit()』, 『_jspDestroy()』와 같은 생명주기 운영을 위해 메소드를 재정의할 수 있다.

# 스크립트 릿(Scriptlet)영역

```html
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%
    // 스크립 릿 영역 -> JSP에서 JAVA 코드를 기술하는(사용하는) 영역
    int a = 10, b = 5, c;
    c = a + b;

    // 스크립릿 영역에서 수행된 자바 코드의 실행 결과는
    // 표현식에 의해 HTML 브라우저 영역에 출력된다.
%>
<html>
<head>
    <title>JSP 관찰하기</title>
</head>
<body>
<div>
    <!-- 표현식 -->
    <h2>합 : <%=a %> + <%=b %> = <%=c %></h2>
</div>

<%
    // 스크립릿 영역
    // * <out>은 내장 객체로서 출력 스트림이다.
    out.print("1.합 : " + a + " + " + b + " = " + c);
    out.println("2.합 : " + a + " + " + b + " = " + c);
    out.println("합 : " + a + " + " + b + " = " + c);

    out.println("<br><br>");

    String str = String.format("3.합 : %d + %d = %d", a, b, c);
    out.print(str);
    out.print(str);

    out.println("<br><br>");

    str = String.format("4.합 : %d + %d = %d\\\\n", a, b, c);
    out.print(str);
    out.print(str);

    out.println("<br><br>");

    str = String.format("5.합 : %d + %d = %d<br>", a, b, c);
    out.print(str);
    out.print(str);
%>
</body>
</html>
<!--
합 : 10 + 5 = 15
1.합 : 10 + 5 = 152.합 : 10 + 5 = 15 합 : 10 + 5 = 15

3.합 : 10 + 5 = 153.합 : 10 + 5 = 15

4.합 : 10 + 5 = 15 4.합 : 10 + 5 = 15

5.합 : 10 + 5 = 15
5.합 : 10 + 5 = 15
-->
```

# 선언부 영역

```html
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%!
    // 선언부 영역 -> 함수 정의가 가능한 영역

    // 선언부에서 선언한 변수
    int a = 10;

    // 선언부에서 정의한 함수
    int sum(int x) {
        int s = 0;
        for (int i = 1; i <= x; i++) {
            s += i;
        }
        return s;
    }
%>
<%
    // 스크립트 릿 영역

    // 스크립트 릿 영역에서 선언한 변수
    int b = 0;

    a++;
    b++;
%>
<html>
<head>
    <title>JSP 관찰하기</title>
</head>
<body>

<div>
    <h2>변수의 값 확인</h2>
    <h3>a : <%=a %></h3>
    <h3>b : <%=b %></h3>
</div>

<div>
    <h2>함수의 기능 확인</h2>
    <h3><%=sum(100) %></h3>
</div>
</body>
</html>
```

이 페이지의 결과를 확인한 후 새로고침을 반복해보면 a변수(선언부에서 선언한 변수)값만 계속 증가하는 것을 확인할 수 있다. 
JSP 페이지의 스크립트 릿 영역에서 선언된 모든 변수는 지역 변수가 된다. 반면 JSP 페이지의 선언부 영역에서 선언된 모든 변수는 클래스의 전역 변수(인스턴스 변수)가 된다. 
JSP 페이지에서 메소드 정의 시 스크립트 릿 영역 내부에서는 정의할 수 없다. 서블릿으로 변환되는 과정에서 메소드 내부에 또 다른 메소드가 다시 정의되는 상황이 되어버리기 때문에 문법적으로 잘못된 표현이 된다. 
선언부는 비록 사용 빈도가 낮지만, 메소드는 선언부 내부에서만 정의할 수 있다.

# Servlet 실습

## 실습 1

Test004.java

```java
/*
    Test004.java
    - Servlet 실습
 */

// 현재... 자바의 기본 클래스 Test004
// 이를 Servlet으로 구성하는 방법

// GenericServlet을 상속받는 클래스로 설계 -> Servlet

package com.example.webapp004;

import javax.servlet.GenericServlet;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
// import javax.servlet.Servlet;

// public class Test004 implements Servlet {
        // Servlet은 다 상속 받으면 너무 많아ㅏ서 그 하위 객체인 GenericServlet을 상속받겠다.
// public abstract class Test004 extends GenericServlet
        // abstract을 붙여야 하지만 override해서 abstract 없이 하겠다.
public class Test004 extends GenericServlet{
    private static final long serialVersionUID = 1L;

    // GenericServlet의 추상 메소드 재정의~!!!
    @Override
    public void service(ServletRequest request, ServletResponse response) throws ServletException, IOException {
        // 요청에 대한 응답 방법
        response.setContentType("text/html; charset=UTF-8");

        try {
            // 출력 스트림 구성
            PrintWriter out = response.getWriter();

            out.print("<html>");
            out.print("<head>");
            out.print("<title>");
            out.print("Test004.java");
            out.print("</title>");
            out.print("</head>");

            out.print("<body>");
            out.print("<div>");
            out.print("<h1>");
            out.print("서블리 관련 실습");
            out.print("</h1>");
            out.print("</div>");

            out.print("</body>");

            out.print("</html>");

        } catch (Exception e) {
            System.out.println(e.toString());
        }
    }
}
```

web.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="<http://xmlns.jcp.org/xml/ns/javaee>"
         xmlns:xsi="<http://www.w3.org/2001/XMLSchema-instance>"
         xsi:schemaLocation="<http://xmlns.jcp.org/xml/ns/javaee> <http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd>"
         version="4.0">
    <display-name>WebApp00</display-name>
    <welcome-file-list>
        <welcome-file>index.html</welcome-file>
        <welcome-file>index.htm</welcome-file>
        <welcome-file>index.jsp</welcome-file>
        <welcome-file>default.html</welcome-file>
        <welcome-file>default.htm</welcome-file>
        <welcome-file>default.jsp</welcome-file>
    </welcome-file-list>

    <servlet>
        <servlet-name>Test004</servlet-name>
        <servlet-class>com.example.webapp004.Test004</servlet-class>
    </servlet>
    
    <servlet-mapping>
        <servlet-name>Test004</servlet-name>
        <url-pattern>/test004</url-pattern>
    </servlet-mapping>
</web-app>
```

## 실습 2

jsptest005.jsp

```html
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <meta charset="UTF-8">
    <title>jsptest005.jsp</title>
    <link rel="stylesheet" type="text/css" href="WEB-INF/css/main.css">
</head>
<body>

<div>
    <h2>HttpServlet 관련 실습</h2>
    <!--
    * form 태그의 action 속성은 데이터 전송 및 페이지 요청을 해야 하는
    대상 페이지를 등록하는 기능을 수행한다. (생략 시 데이터 전송 및 페이지 요청을 하게 되는 대상은
    자기 자신이 된다.(나한테 전송하고 내가 받는거다.))
    -->
    <form action="/WebApp004_war_exploded/login" method="get">
        <table>
            <tr>
                <th>아이디</th>
                <td>
                    <input type="text" name="userId" size="10" maxlength="10" class="txt">
                </td>
            </tr>
            <tr>
                <th>패스워드</th>
                <td>
                    <input type="password" name="userPwd" size="10" class="pwd">
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <!-- submit 액션 -> form 데이터 전송 및 페이지 요청 -->
                    <input type="submit" value="로그인" class="btn control" style="width: 92px;">
                    <input type="reset" value="다시 입력" class="btn control" style="width: 92px;">
                </td>
            </tr>
        </table>
    </form>
</div>

</body>
</html>
```

Test05.java

```java
/*
    Test005.java
    - Servlet 실습
 */

// 현재 자바의 기본 클래스

package com.example.webapp004;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.io.PrintWriter;

public class Test005 extends HttpServlet {
    private static final long serialVersionUID = 1L;

    // 사용자의 http 프로토콜 요청이 GET 방식일 경우 호출되는 메소드
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // GET 방식의 요청에 대해 처리하는 코드
        doGetPost(request, response);
    }

    // 사용자의 http 프로토콜 요청이 post 방식일 경우 호출되는 메소드
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // POST 방식의 요청에 대해 처리하는 코드
        doGetPost(request, response);
    }

    // 사용자 정의 메소드
    protected void doGetPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // GET 방식이든 POST 방식이든
        // 어떤 방식의 요청에도 모두 처리할 수 있는 사용자 정의 메서드

        // request -> 요청 객체
        // -> 클라이어트로부터 서버로 전송된 데이터 (이 데이터가 담겨 있는) 객체
        // request 객체에 대한 세팅 -> 인코딩 방식 처리 -> 한글 깨짐 방지
        request.setCharacterEncoding("UTF-8");

        String id = request.getParameter("userId");
        String pwd = request.getParameter("userPwd");

        // response -> 응답 객체
        // -> 서버로부터 클라이언트로
        response.setContentType("text/html; charset=UTF-8");

        String str = "아이디 : " + id + ", 패스워드 : " + pwd;

        // 응답을 출력 스트림으로 구성하기 위한 준비
        PrintWriter out = response.getWriter();

        // 출력 스트림을 활용하여 페이지 랜더링
        out.print("<!DOCTYPE html>");
        out.print("<html>");
        out.print("<head>");
        out.print("<meta charset=\\"UTF-8\\">");
        out.print("<title>Test005.java</title>");
        out.print("</head>");

        out.print("<body>");
        out.print("");
        out.print("<div>");
        out.print("<h2>HttpServlet 클래스를 활용한 서블리 테스트</h2>");
        out.print("<p>"+ str +"</p>");
        out.print("</div>");
        out.print("</body>");

        out.print("</html>");
    }
}
```

web.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="<http://xmlns.jcp.org/xml/ns/javaee>"
         xmlns:xsi="<http://www.w3.org/2001/XMLSchema-instance>"
         xsi:schemaLocation="<http://xmlns.jcp.org/xml/ns/javaee> <http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd>"
         version="4.0">
    <display-name>WebApp00</display-name>
    <welcome-file-list>
        <welcome-file>index.html</welcome-file>
        <welcome-file>index.htm</welcome-file>
        <welcome-file>index.jsp</welcome-file>
        <welcome-file>default.html</welcome-file>
        <welcome-file>default.htm</welcome-file>
        <welcome-file>default.jsp</welcome-file>
    </welcome-file-list>

    <servlet>
        <servlet-name>Test004</servlet-name>
        <servlet-class>com.example.webapp004.Test004</servlet-class>
    </servlet>
    
    <servlet-mapping>
        <servlet-name>Test004</servlet-name>
        <url-pattern>/test004</url-pattern>
    </servlet-mapping>

    <servlet>
        <servlet-name>Test005</servlet-name>
        <servlet-class>com.example.webapp004.Test005</servlet-class>
    </servlet>
    
    <servlet-mapping>
        <servlet-name>Test005</servlet-name>
        <url-pattern>/login</url-pattern>
    </servlet-mapping>
</web-app>
```