# HTML & CSS

# HTML

## 웹(Web) 개요

### 웹 개요

사용자가 웹에 접속하면 자신의 브라우저에 그 웹사이트가 보여지며 이런
사이트는 전부 페이지 (page) 단위로 구성된다.
이 가운데 첫 번째로 나오는 페이지를 ‘홈페이지(home page)’라고 하 나머
지 페이지들을 단순히 ‘웹 문서(웹 페이지)’라고 한다.
이러한 웹 문서에는 정보전달의 가장 기본이 되는 텍스트 및 그래픽,사운드,
동영상 등 거의 모든 정보들을 삽입하거나 연결할 수 있으며 HTML을 사용
하여 구축한다.

### 웹 표준

- W3C : 국제적 표준화 단체가 수집,정리한 것으로서 W3C가 가장 중심적인 역할 담당.
- 웹 표준 목적 : 특정 기기와 상관없이 누구든지 정보에 접근할 수 있는 웹을 만들어야 함. 데이터 구조는 HTML이 담당하고, 디자인과 레이아웃은 CSS가 담당하며동작 및 컨트롤은 Javascript와 DOM이 담당.
- HTML : 웹페이지를 구성하고 표현하는 기본 언어
- CSS : 웹페이지의 호환성 유지 및 다양한 액세스 기술을 사용
- XML : HTML이나 CSS로서 표현되지 못하는 영역을 DTD를 이용하여 정의하여 사용자 정의 태그를 생성하여 제작할 수 있음.
- DOM : 컨텐츠, 구조, 문서 스타일을 프로그램과 스크립트가 동적으로 접근하고 수정할 수 있는 플랫폼.
- ECMAScript(Javascript) : W3C표준으로 제정된 것이 아님.

### HTML5 개요

- 종료 태그가 없는 요소 : area, base, br, col, command, embed, hr, img, inptut 등
- 태그 생략이 가능한 요소 : html, head, body, li, dt, dd, p, tr, td 등
- 속성 값 생략 가능
- 대소문자 구별 없음
- 시멘틱(semantic) 태

## HTML 개요

### html 기본 구조

```html
<!DOCTYPE html>
<html lang="en">
<head>
    
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
```

## 태그

### head 태그

- **title 태그**
    - 문서의 타이틀을 지정한다.
    - 브라우저의 툴 바에 타이틀이 지정되며 ‘즐겨찾기’를 추가할 때 페이지의 타이틀이 추가된다.
    
    ```html
    <!DOCTYPE html>
    <html>
    <head>
    <title>웹 페이지의 제목</title>
    </head>
    <body>
    ```
    
- **base 태그**
    - 문서 내의 모든 링크에 대한 기본 주소 및 target을 명시한다.
    
    ```html
    <head>
    <!-- base 코드로 이미지 경로 defalut로 지정 -->
    <base href="http://127.0.0.1:5500/html_source/images/" target="_blank">
    <meta charset="UTF-8">
    <title>base 태그 실습</title>
    </head>
    
    <body>
    <!-- 이미지 경로 없이 파일명만 명시해도 적용됨. -->
    <img src="001.png" width="100" height="100">
    <img src="main.png" width="100" height="100">
    
    <!-- base태그 없을 경우 -> 이미지 경로 같이 명시해야 함. -->
    <img src="images/001.png" width="100" height="100">
    <img src="images/main.png" width="100" height="100">
    </body>
    </html>
    ```
    
    <aside>
    💡 base 태그가 있을 경우에는 파일명만 명시해도 적용됨.
    base 태그가 없을 경우에는 경로+파일명 모두 명시해야 함.
    
    </aside>
    
    <aside>
    💡 target="_blank" : 새 탭에서 실행됨.
    
    </aside>
    
- **link 태그**
    - 문서에서 사용하는 외부파일 경로를 지정할 때 사용
    - 일반적으로 외부 css 파일 및 favicon 을 지정할 때 사용
    
    ```html
    <head>
    <link rel=“stylesheet” type=“text/css” href=“mystyle.css”>
    </head>
    ```
    
    ```html
    <head>
    <meta charset="UTF-8">
    <!-- rel 속성 : 현재 문서와 링크된 문서 사이의 연관 관계(relationship)를 명시
     -->
     <!-- type 속성 : <input> 요소가 나타낼 타입을 명시,type의 기본값은 text -->
     <!-- href 속성 : 연결할 주소를 지정 -->
    
    <!-- external 방식 : link -->
    <link rel="stylesheet" type="text/css" href="css/mystyle.css">
    <link rel="icon" type="images/icon" href="images/favicon.ico">
    <title>link 태그 실습</title>
    </head>
    ```
    
- **style 태그**
    - html 문서의 스타일 정보를 지정할 때 사용
    - 일반적으로 내부 css 파일을 지정할 때 사용
    
    ```html
    <head>
    <style type=“text/css”>
    p{ color:red; }
    </style>
    </head>
    ```
    
- **script 태그**
    - 자바스크립트를 명시할 때 사용
    
    ```html
    <script>
      // internal 방식
      //웹브라우저 콘솔에 출력됨. (웹브라우저-F12-conssol)
      console.log("Hello World");
      console.log( "<h1>Hello World</h1>"); 
    </script>
    
    ```
    
    ```html
    <!-- external 방식 -->
    <script src="JS/test.js"></script>
    ```
    

### header 태그

- header는 <h1>에서 <h6>까지 제공된다.
- 검색엔진은 웹 페이지의 구조와 내용을 참조하기 위해 header를 사용한다.

```html
<h1>This is header 1</h1>
<h2>This is header 2</h2>
<h3>This is header 3</h3>
<h4>This is header 4</h4>
<h5>This is header 5</h5>
<h6>This is header 6</h6>
```

### hr 태그

- 내용을 분리하기 위하여 사용하며 웹 페이지에 수평선을 생성한다.

```html
<h1>This is header 1</h1>
<hr/>
<h2>This is header 2</h2>
<h3>This is header 3</h3>
<hr size="10" noshade />
<h4>This is header 4</h4>
<h5>This is header 5</h5>
<hr size="3" width="500" noshade="noshade" />
<h6>This is header 6</h6>
```

![Untitled](HTML%20&%20CSS%20e60dfbeaea184c2495676b5375e51950/Untitled.png)

### p 태그

- 문서의 문단(paragraph)을 지정할 때 사용한다.
(빈 여백 또는 내용 분리 목적으로 사용하지 않는다.)

```html
<!-- 단락을 표현할 때 사용. 빈 여백 처리용이 아니다.-->
  <p>
	첫 번째 문단입니다.
  </p>
	
  <p>두 번째 문단입니다.</p>
```

### br 태그

- 새로운 문단이 아닌 개행(new line)할 때 사용하고 종료 태그를 갖지 않는다.

```html
<body>
첫 번째 라인입니다.<br>
두 번째 라인입니다.<br>
세 번째 라인입니다.<br>

<!-- span : 대표적인 inline sytle -->
<!-- inline을 block으로 변경시 css와 함께 사용한다. -->
<!-- 줄 바꿈이 적용되지 않는다. -->
<span>a1</span>
<span>a2</span>
<span>a3</span>
</body>
```

![Untitled](HTML%20&%20CSS%20e60dfbeaea184c2495676b5375e51950/Untitled%201.png)

### text 포맷용 태그

| 태그 이름 | 설명 |
| --- | --- |
| b | 굵은 글자 태그 |
| i | 기울어진 글자 태그 |
| small | 작은 글자 태그 |
| sub | 아래에 달라 붙는 글자 태그  |
| sup | 위에 달라붙는 글자 태그 |
| ins | 밑줄 글자 태그 |
| del | 가운데 줄이 그어진 글자 태그 |

```html
<!-- 권장은 css 사용 -->
<b>문자열을 진하게</b><br>
<strong>문자열 강조</strong><br>
<i>문자열을 이탤릭체로</i><br>
HTML5<sub>아래첨자로</sub><br>
HTML5<sup>위 첨자로</sup><br>
<address>서울시 강남구 역삼동 34-21 번지</address>
<del>20000원</del>1000원<br>
<ins>밑줄 쫘악~</ins>
```

![Untitled](HTML%20&%20CSS%20e60dfbeaea184c2495676b5375e51950/Untitled%202.png)

### a 태그

- 외부 페이지 이동
    
    서로 다른 웹페이지 또는 하나의 웹 페이지 내부에서 특정한 위치로 이동 가능. hyperlink는 텍스트 및 이미지 모두 가능하며 타겟은 href 속성을 이용한다.
    

```html
<body>
	<!-- "target.html" => 내부 html(로컬 호스트) 안에 있는 파일 -->
	<!-- 내부 html에 있는 파일 링크 -> 가장 일반적 -->
	<a href="target.html" title="target.html 로컬 페이지" target="_blank"><!--새창으로 보기-->
		로컬 페이지 이동</a><br>
	<a href="http://www.daum.net" >외부 페이지 이동</a>
</body>
```

<aside>
💡 html 내부에 있는 파일 링크를 연결할 때 일반적으로 사용

</aside>

```html
<body>
  <a href="#Java">java 행으로 이동</a>
<a href="#oracle">Oracle 행으로 이동</a>
<a href="target2.html#html">다른페이지의 html 행으로 이동</a>
<p>
test test test test test test test test test test test test test test<br>
test test test test test test test test test test test test test test test test <br> test test test test test test test test test test<br>
</p>

<a id="Java">여기서 부터는 자바행</a>
JavaJavaJavaJavaJavaJavaJavaJavaJavaJavaJavaJavaJavaJavaJavaJavaJava
<br>
JavaJavaJavaJavaJavaJavaJavaJavaJavaJavaJavaJavaJavaJavaJavaJavaJava
<br>
JavaJavaJavaJavaJavaJavaJavaJavaJavaJavaJavaJavaJavaJavaJavaJavaJava
   .....
<br>
<a id="oracle">여기서 부터는 오라클행</a>
<p>
	OracleOracleOracleOracleOracleOracleOracleOracleOracleOracleOracleOracle<br>
</p>
</body>
```

- target 속성
    
    
    | 속성 | 설명 |
    | --- | --- |
    | _blank | 새로운 윈도우 창 또는 tab에 문서를 open한다. |
    | _self | default로서 현재 클릭한 창 또는 tab에 문서를 open한다. |
    | _parent | parent 프레임에 문서를 open한다. |
    | _top | 현재 윈도우에 전체화면으로 open한다. |

### table 태그

| 태그 이름 | 설명 |
| --- | --- |
| tr | 표 내부의 행 태그 |
| th | 행 내부의 제목 셀 태그 |
| td | 행 내부의 일반 셀 태그 |
| caption | 캡션 |
- **일반**
    
    ```html
    <table border="1"> <!--테이블 라인 두께-->
    		<caption>캡션 실습</caption>
    		<tr>
    			<th>1열 제목</th> 
    			<th>2열 제목</th>
    		</tr>
    		<tr>
    			<td>1행 1열</td>
    			<td>1행 2열</td>
    		</tr>
    		<tr>
    			<td>2행 1열</td>
    			<td>2행 2열</td>
    		</tr>
    </table>
    ```
    
    ![Untitled](HTML%20&%20CSS%20e60dfbeaea184c2495676b5375e51950/Untitled%203.png)
    
- **중첩 테이블 / 중첩 리스트**
    
    ```html
    <table border="1">
    		<tr>
    			<td>
    				<p>첫 번째 단락입니다.</p>
    				<p>두 번째 단락입니다.</p>
    			</td>
    			<td>중첩 테이블:
    				<table border="1">
    					<tr>
    						<td>A</td>
    						<td>B</td>
    					</tr>
    					<tr>
    						<td>C</td>
    						<td>D</td>
    					</tr>
    				</table>
    			</td>
    		</tr>
    		<tr>
    			<td>중첩 리스트:
    				<ul>
    					<li>사과</li>
    					<li>바나나</li>
    					<li>딸기</li>
    				</ul>
    			</td>
    			<td>안녕하세요</td>
    		</tr>
    	</table>
    ```
    
    ![Untitled](HTML%20&%20CSS%20e60dfbeaea184c2495676b5375e51950/Untitled%204.png)
    
- **그룹핑**
    
    ```html
    <table border="1">
      <thead>
        <tr>
          <th>월요일</th>
          <th>저축</th>
        </tr>
      </thead>
      <tfoot>
        <tr>
          <td>합계</td>
          <td>18000</td>
        </tr>
      </tfoot>
      <tbody>
        <tr>
          <td>1월</td>
          <td>10000</td>
        </tr>
        <tr>
          <td>2월</td>
          <td>8000</td>
        </tr>
      </tbody>
    </table>
    ```
    
    <aside>
    💡 테이블 머리 : thead
    하나 이상의 몸체 : tbody
    바닥행 : tfoot ⇒ 반드시 tbody 앞에 사용해야 한다.
    
    순서는 <thead></thead> -> <tfoot></tfoot> -> <tbody></tbody>
    
    그룹핑 목적 : JS에서 접근하기 위함.
    그룹핑 사용을 권장함. ⇒ JS 프레임워크 사용시 필수 사항인 경우도 있음.
    
    </aside>
    
    ![Untitled](HTML%20&%20CSS%20e60dfbeaea184c2495676b5375e51950/Untitled%205.png)
    
- **행열 병합**
    - 열 병합
    
    ```html
    <table border='1'>
      <tr>
         <th>이름</th>
         <th colspan="2">전화번호</th> <!--colspan : 열병합-->
      </tr>
       <tr>
        <td>홍길동</td>
        <td>55577854</td>
        <td>55577855</td>
      </tr>
    </table>
    ```
    
    ![Untitled](HTML%20&%20CSS%20e60dfbeaea184c2495676b5375e51950/Untitled%206.png)
    
    - 행 병합
    
    ```html
    <table border='1'>
      <tr>
        <th>이름</th>
        <td>홍길동</td>
      </tr>
      <tr>
        <th rowspan="2">전화번호</th> <!--rowspan : 열병합-->
        <td>55577854</td>
      </tr>
      <tr>
        <td>55577855</td>
      </tr>
    </table>
    ```
    
    ![Untitled](HTML%20&%20CSS%20e60dfbeaea184c2495676b5375e51950/Untitled%207.png)
    

### list 태그

- 순서 있는 리스트 (order list : ol)
    
    ```html
    <body>
    	<!-- 순서 있는 리스트 (order list: ol)-->
    	<!-- 대표적인 block style-->
    	<ol> <!--넘버링 start 값 지정안하면 1부터 시작-->
    		<li>사과</li>
    		<li>배</li>
    	</ol>
    	<ol start="3"> <!--넘버링 start 값 지정o 3부터 시작-->
    		<li>사과</li>
    		<li>배</li>
    	</ol>
    </body>
    ```
    
- 순서가 없는 리스트
    
    ```html
    <body>
    	<!-- 순서 없는 리스트, 넘버링 대신 글머리기호로 표시됨-->
    	<ul type="circle">
    		<li>사과
    		<li>배
    	</ul>
    	<ul type="square">
    		<li>사과
    		<li>배
    	</ul>
    	<ul type="disc">
    		<li>사과
    		<li>배
    	</ul>
    </body>
    ```
    

### semantic 태그

- ‘의미를 갖는다’라는 뜻으로, 각 태그가 스스로 의미를 지닌다는 뜻

> header : 사이트에 대한 소개 정보나 메인 메뉴, 사이트 로고 등이 포함됨
nav : 사이트의 메뉴나 링크 같은 네비게이션 요소들이 포함
section : 실제 문서 내용이 들어감
article : 문서 내용이 많을 경우 여러개의 <article> 요소로 나눌 수 있음
aside : 문서의 주요 내용 외의 내용들을 넣어 문서의 주영역 주변에 배치
footer : 작성자 정보나 저작권 정보, 또는 관련 문서 링크 등 부가 정보들을 담고 있음. 주로 문서 하단에 배치
> 

- **header 태그**
    - 그룹화를 위한 요소
    - article 이나 section에서도 header 사용 가능
    - 적어도 한개의 제목(h1~h6)이 들어 있어야 한다.
    
    ```html
    <header>
         <h1>Header</h1>
         <h2>Subtitle</h2>
         <h4>HTML5 Rocks!</h4>
    </header>
    ```
    
- **nav 태그**
    - 다른 도큐먼트를 링크하건나 링크를 모아 놓은 그룹/섹션
    - 주요 네비게이션 링크를 그룹화함
    - 모든 하이퍼링크에 nav 사용은 아님
    - footer의 링크는 nav를 사용하지 않음
    
    ```html
    <nav>
      <h3>Nav</h3>
      <a href="">Link 1</a>
      <a href="">Link 2</a>
      <a href="">Link 3</a>
    </nav>
    ```
    
- **section 태그**
    - 문서의 주제별로 섹션을 구분
    - article 안에 포함되기도 하고 article을 포함시키기도 함.
    
    ```html
    <section>
    <article>
        <header>
            <h1>Article Header</h1>
        </header>
        <p>Lorem ipsum dolor HTML5 nunc aut nunquam sit amet, consectetur adipiscing elit. Vivamus at est eros, vel fringilla urna.</p>
        <p>Per inceptos himenaeos. Quisque feugiat, justo at vehicula pellentesque, turpis lorem dictum nunc.</p>
        <footer>
            <h2>Article Footer</h2>
        </footer>
    </article>
    </section>
    ```
    
- **article 태그**
    - 독립적인 컨텐츠 구성
    - 블로그, 기사, 본문의 댓글 등에 사용
    - 댓글이나 Q&A 등의 하나의 글들 모두 aricle임
    
    ```html
    <article>
        <header>
            <h1>Article Header</h1>
        </header>
        <p>HTML5: "Lorem ipsum dolor nunc aut nunquam sit amet, consectetur adipiscing elit. Vivamus at est eros, vel fringilla urna. Pellentesque odio</p>
        <footer>
            <h2>Article Footer</h2>
        </footer>
    </article>
    ```
    
- **aside 태그**
    - 본문과 무관한 내용의 간접적인 컨텐츠 섹션
    - 없어져도 상관없는 섹션
    - 배너 광고 등에서 사용
    
    ```html
    <aside>
        <h3>Aside</h3>
        <p>HTML5: "Lorem ipsum dolor nunc aut nunquam sit amet, consectetur adipiscing elit. Vivamus at est eros, vel fringilla urna. Pellentesque odio rhoncus</p>
    </aside>
    ```
    
- **footer 태그**
    - 작성자, 관련 문서의 링크 또는 저작권자 등의 컨텐츠 작성
    - 다수의 엘리먼트 사용 가능
    - section, article에서 사용 가능
    
    ```html
    <footer>
        <h2>Footer</h2>
    </footer>
    ```
    

### 태그 그룹핑

- **그룹핑 개요**
    - div 태그와 span 태그는 HTML 태그들을 그룹화할 수 있는 태그들이다.
    - 태그들은 block level과 inline level로 구분되어 진다.
    - block level (세로 배치)
        
        브라우저에서 보여질 때 new line을 생성해서 보여준다. 전체 너비를 사용.
        
        ![Untitled](HTML%20&%20CSS%20e60dfbeaea184c2495676b5375e51950/Untitled%208.png)
        
    - inline level (가로 배치)
        
        inline level은 new line 없이 보여준다. 필요한 만큼의 너비만 사용.
        
        ![Untitled](HTML%20&%20CSS%20e60dfbeaea184c2495676b5375e51950/Untitled%209.png)
        
- **div 태그**
    - block level 태그
    - HTML태그들을 그룹화하기 위한 컨테이너 역할
    - 일반적으로 CSS와 같이 사용
    - width 와 height 속성을 설정하여 너비와 높이를 지정
    
    ```html
    <body>
         <!--  컨텐츠나 특정요소를 묶을때 사용 , 무분별하게 사용하지 말고, 논리그룹으로 만들때 사용권장-->
      <div>
      	<h1>오만과 편견</h1>
        <div>
         <h2>1권</h2>
          <div>
          	<h3>1장</h3>
          	 <p>돈 많은 독신남에게 아내가 필요하다는 것은....</p>
            <p>이런 진실은 주변 이웃들의 마음 속에 단단히 박혀...</p>	
          </div>
        </div>
       </div>
    </body>
    ```
    
    ![Untitled](HTML%20&%20CSS%20e60dfbeaea184c2495676b5375e51950/Untitled%2010.png)
    
- **span 태그**
    - inline level 태그
    - 텍스트(text)을 위한 컨테이너 역할
    - width 와 height 속성이 적용 안됨
    - 일반적으로 CSS와 같이 사용
    - 텍스트(text)의 스타일 변경 목적으로 주로 사용
    
    ```html
    <style type="text/css">
     #red{
      color: red;
      font-size: 100px;
     }
    </style>
    </head>
    <body>
    	<h3>1장</h3>
    	<p>돈 많은<span id="red">독신남</span> 에게 아내가 필요하다는 것은....</p>
      <p>이런 진실은 주변 이웃들의 마음 속에 단단히 박혀...</p>	
    </body>
    ```
    
    ![Untitled](HTML%20&%20CSS%20e60dfbeaea184c2495676b5375e51950/Untitled%2011.png)
    

## 폼

### 개요

- 서버에 데이터를 전송하기 위해 HTML 폼을 사용한다.

| 폼 태그의 속성 | 기능 설명 |
| --- | --- |
| name | 윈도우 객체에 들어있는 모든 프레임을 나타내는 속성 |
| action | 사용자가 입력한 데이터를 처리할 프로그래밍 URL 경로나 문서 |
| method | - 입력된 내용을 어떤 방식으로 전송할 것인가를 지정하는 속성.
- post와 get 중 하나로 지정
- post는 입력 폼이 서버에 데이터베이스화될 때 사용되며 주로 방명록, 게시판에 사용
- get은 URL로 데이터를 전송하는 방식. 입력폼의 내용에 대한 결과를 서버로부터 가져와서 사용자에게 직접 볼 수 있도록 함. 주로 검색엔진의 검색 결과나 방문횟수를 보여주는 카운터 등에 주로 사용 |

### text 필드

- method=”get”

```html
<form action="target.html">
이름1 <input type="text" name="username"><br>
나이 <input type="text" name="age"><br>
<!-- name=" " : query string / key=value 형태
query string과 action 타겟은 구분자 ?로 이어짐. 
(target.html?key=value)
query string이 여러개 있을 경우 구분자 &로 이어짐. 
(key=value&key=value)-->

	<input type="submit" value="전송">
</form> 
	
```

<aside>
💡 method=”get” : Query string이 url에 보이게 전달됨 (보안취약)

</aside>

- method=”post”

```html
<form action="target.html" method="post">
이름1 <input type="text" name="username"><br>
나이 <input type="text" name="age"><br>
<!-- name=" " : query string / key=value 형태
query string과 action 타겟파일은 구분자 ?로 이어짐. (target.html?key=value)
query string이 여러개 있을 경우 구분자 &로 이어짐. (key=value&key=value)-->

<input type="submit" value="전송">
</form>
```

<aside>
💡 method=”post” : Query string이 url에 보이지 않게 숨겨져서 전달됨.

</aside>

### radio 필드

```html
<form name="myForm" action="target.html" method="get">
	<input type="radio" name="gender" value="male" checked>남<br>
	<input type="radio" name="gender" value="female">여<br>

	<input type="submit" value="전송">
</form>
```

<aside>
💡 radio는 name을 동일하게 지정해야 된다.

</aside>

![Untitled](HTML%20&%20CSS%20e60dfbeaea184c2495676b5375e51950/Untitled%2012.png)

### check 필드

```html
<body>
<form name="myForm" action="target.html" method="get">
	<input type="checkbox" name="fruits" value="apple" checked>사과<br> <!-- checked="checked"도 가능-->
	<input type="checkbox" name="fruits" value="banana">바나나<br>

	<input type="submit" value="전송">
	<button>전송2</button>
	<input type="button" value="전송3"> <!-- sumit 불가. 버튼 모양만 생성됨. -->
</form>    	
</body>
```

<aside>
💡 checkbox는 form 태그에서 여러개의 값 선택하여 전달할 수 있음. 체크된 값만 전달됨.

</aside>

![Untitled](HTML%20&%20CSS%20e60dfbeaea184c2495676b5375e51950/Untitled%2013.png)

### select 필드

```html
<body>
<form name="myForm" action="target.html" method="post">
<select name="cars">
  <option value="">선택하시오</option>
  <option value="volvo">볼보</option>
  <option value="saab">사브</option>
  <option value="fiat">피아트</option>
  <option value="audi" selected="selected">아우디</option> <!--selected="selected"도 가능-->
</select>
</form>    	
</body>
```