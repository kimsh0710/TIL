# WebCrawling

## Before we start

- **Big Data 활용 프로세스**
    
    ![Untitled](WebCrawling%2070252974375c4faf8c9c9f9c70c3226e/Untitled.png)
    

## 개요

### 크롤러와 크롤링

- 크롤러는 자동으로 웹페이지에 있는 정보를 수집하는 프로그램
- 크롤러는 사람이 브라우저로 웹페이지를 조회하고 정보를 수집하는 것과 비교할 수 없을 정도로 대규모의 정보를 단시간에 수집
- 크롤러로 정보를 수집하는 일을 ‘크롤링’이라고 함

### 스크랩핑

- 스크랩핑은 수집한 정보를 분석해서 필요한 정보를 추출하는 것

### 크롤링과 스크랩핑

- 크롤링과 스크랩핑의 프로세스
    
    ![Untitled](WebCrawling%2070252974375c4faf8c9c9f9c70c3226e/Untitled%201.png)
    

### 주의사항

- **웹사이트 접근 시 주의 사항**
    - 웹사이트의 이용 규약을 확인하고 지킨다.
    - robot.txt와 robots 메타 태그의 접근 제한 사항을 지킨다.
    - 제한이 없더라도 상대 서버에 부하가 가지 않을 정도의 속도로 접근한다.
    - rel=’nofollow’가 설정돼 있으면 크롤러로 접근하지 않는다.
    - 크롤링을 거부하는 조치가 있으면 즉시 크롤링을 멈추고 이미 추출한 정보를 모두 삭제한다.
- **수집한 데이터를 다룰 때의 주의사항**
    - 수집한 데이터는 저작권을 지켜서 사용해야 함.
    - 저작권에 문제가 있으면 개인적인 용도로만 사용함.
    - 수집한 데이터를 기반으로 검색 서비스를 제공하는 경우, 웹사이트와 API 등의 사용 규약을 확인하고 없을 때만 제공함
    - 이용 규약이 따로 없을 때도 상대방에서 확인한 뒤에 데이터를 공
- **네트워크 요청 시 주의 사항**
    - 간격 설정하기 : 적어도 1초에 한번 정도만 요청할 수 있도록 권장
    - 타임아웃
        - 요청한 사이트로부터 응답이 오지 않는 경우 타임아웃 설정
        - 3초동안 응답이 없으면 멈춤
    - 재시도
        - 큰 문제가 없는데도 오류를 응답하는 경우
        - 재시도할 때에는 어느 정보의 횟수 제한이 있어야 함
        - 재시도 간격도 고려
- **파싱(분석)**
    - 문자 코드
        - 대부분 UTP-8ㄹ로 작성되어 있지만 HTML 소스 코드는 다양한 문자코드로 작성된 경우가 많음(EUC-KR 등)
    - HTML/XML 파싱
        - 웹페이지 중에는 태그가 잘못 구성돼 있거나 속성 값에 큰 따옴표가 쳐져 있지 않은 경우도 많음
    - JASON 디코드
        - 대부분의 웹 API는 JSON 형식으로 데이터를 응

### 파이썬을 사용하는 이유

- 코드 가독성이 높음
- 문법이 단순하고 명쾌함
- 컴파일이 필요하지 않은 스크립트 언

## HTML 생성

```python
%%writefile C:\JupyterTest\HTML_example.html
<!doctype html>
<html>
    <head>
        <meta charse="utf-8">
        <title>이것은 HTML 예제</title>
    </head>
    <body>
        <h1>출간된 책 정보</h>
        <p id="book_title">이해가 쏙쏙되는 파이썬</p>
        <p id="author">홍길동</p>
        <p id="publisher">위키북스 출판사</p>
        <p id="year">2018</p>
    </body>
</html>
```

<aside>
💡 %%%writefile 경로+파일명
 - 작성한 HTML 코드를 파일로 저장
 - jupyternotebook에서만 사용 가능

</aside>

## HTML 소스 가져오기

- **requests.get**
    - HTTP 요청을 보내고 응답을 받는 역할
    - **`Response`** 객체를 반환 → 응답 상태 코드, 헤더, 본문 등을 확인

```python
import requests

r = requests.get("https://www.google.co.kr")
r

# 결과 : <Response [200]>
```

## URL 열고 가져오기

### webbrowser.open

- 웹 브라우저를 열어 주어진 URL을 표시
- 웹 브라우저를 자동으로 열어 특정 웹 페이지를 사용자에게 보여줌
- 웹 브라우저가 실행되지 않은 상태이면 새로이 웹 브라우저가 실행되어 해당 URL로 이동
- open_new 함수는 이미 웹 브라우저가 실행된 상태에서 새로운 창으로 해당 주소가 열리도록 함.

```python
import webbrowser

webbrowser.open("http://www.naver.com")
```

### urllib로 웹 페이지 추출하기(urlopen)

- 표준 라이브러리 urllib.request 모듈을 사용
- URL에 직접 접근하여 내용을 가져옴
- 주로 웹 스크래핑이나 데이터 추출 등에서 사용되며, 웹 페이지의 HTML, XML, JSON 등의 내용을 가져올 수 있음
- 반환된 내용을 파싱하여 필요한 데이터를 추출하거나 분석

```python
from urllib.request import urlopen

f = urlopen("http://naver.com")
type(f) # HTTPResponse

f.read() # read()메서드로 HTTP 응답 본문(bytes 자료형)을 추출
f.status # 상태 코드를 추출/ 200 <- 성공
f.getheader('Content-Type') # HTTP 헤더값을 추출
```

<aside>
💡 urlopen() 함수는 HTTPResponse 자료형의 객체를 반환

</aside>

### 네이버에서 특정 검색어 입력해 결과 얻어 오기

```python
import webbrowser

naver_search_url = "http://search.naver.com/search.naver?query="
search_word = '파이썬'
url = naver_search_url + search_word

webbrowser.open_new(url)
```

### 여러개의 웹 사이트에 접속하기

- **URL 주소 리스트와 for 문 이용**
    
    ```python
    import webbrowser
    
    urls = ['www.naver.com', 'www.daum.net', 'www.google.com']
    
    for url in urls:
        webbrowser.open_new(url)
    ```
    
- **여러 단어 리스트와 for 문 이용**
    
    ```python
    import webbrowser
    
    google_url = "www.google.com/search?q="
    serach_words = ['python web scraping', 'python webbrowser']
    
    for search_word in serach_words:
        webbrowser.open_new(google_url + search_word)
    ```
    

## (문자)데이터 추출

### BeautifulSoup란?

- 웹 스크래핑 및 웹 데이터 추출을 위한 파이썬 라이브러리
- HTML 및 XML 문서에서 데이터를 파싱(데이터 구조화)하고 추출하는 데 사용
- 웹 페이지의 내용을 쉽게 탐색하고 조작할 수 있음
- 각 요소를 선택하거나 필터링하기 위해 CSS 선택자, 태그 이름, 속성 등을 사용할 수 있음
- **파싱**
    
    ```python
    from bs4 import BeautifulSoup
    
    # 테스트용 html 코드
    html = """<html><body><div><span>\
            <a href=http://www.naver.com>naver</a>\
            <a href=https://www.google.com>google</a>\
            <a href=http://www.daum.net/>daum</a>\
            </span></div></body></html>"""
    
    # BeautifulSoup를 이용해 HTML 소스를 파싱
    soup = BeautifulSoup(html, 'lxml')
    soup
    ```
    
    > <html><body><div><span> <a href="http://www.naver.com">naver</a> <a href="https://www.google.com">google</a> <a href="http://www.daum.net/">daum</a> </span></div></body></html>
    > 
    
- **prettify( ) : 파싱 결과를 보기 편하게 HTML 구조의 형태로 확인**
    
    ```python
    print(soup.prettify())
    ```
    
    > <html>
     <body>
      <div>
       <span>
        <a href="http://www.naver.com">
         naver
        </a>
        <a href="https://www.google.com">
         google
        </a>
        <a href="http://www.daum.net/">
         daum
        </a>
       </span>
      </div>
     </body>
    </html>
    > 

### find( ) 함수

- **find( ) : 해당 '태그'가 있는 첫번째 요소를 찾아서 반환**
    
    ```python
    soup = BeautifulSoup(html, 'lxml')
    
    soup.find('a')
    ```
    
    > <a href="http://www.naver.com">naver</a>
    > 
    
- **find_all( ) : 특정 태그 모두 가져오기**
    
    ```python
    soup.find_all('a')
    ```
    
    > [<a href="http://www.naver.com">naver</a>,
     <a href="https://www.google.com">google</a>,
     <a href="http://www.daum.net/">daum</a>]
    > 
    
    <aside>
    💡 리스트로 반환
    
    </aside>
    
- **BeautifulSoup.find('태그', '속성') : 특정 태그 중 특정 속성을 가진 요소만 반환**
    - 모든 p 태그 요소
    
    ```python
    soup2.find_all('p')
    ```
    
    > [<p id="book_title">토지</p>,
     <p id="author">박경리</p>,
     <p id="book_title">태백산맥</p>,
     <p id="author">조정래</p>,
     <p id="book_title">감옥으로부터의 사색</p>,
     <p id="author">신영복</p>]
    > 
    - id가 “book_title”인 요소만 반환
    
    ```python
    soup2.find('p', {"id":"book_title"})
    ```
    
    > <p id="book_title">토지</p>
    > 
    - id가 “author”인 요소만 반환
    
    ```python
    soup2.find('p', {"id":"author"})
    ```
    
    > <p id="author">박경리</p>
    > 
    - 책 제목과 작가를 포함한 요소를 각각 추출한 후에 텍스트만 뽑는 코드
    
    ```python
    from bs4 import BeautifulSoup
    
    soup2 = BeautifulSoup(html2, "lxml")
    
    book_titles = soup2.find_all('p', {"id":"book_title"})
    authors = soup2.find_all('p', {"id":"author"})
    
    for book_title, author in zip(book_titles, authors):
        print(book_title.get_text() + "/" + author.get_text())
    ```
    
    > 토지/박경리
    태백산맥/조정래
    감옥으로부터의 사색/신영복
    > 
    

### get_text( ) 함수

- HTML 소스코드의 요소에서 태그와 속성을 제거하고 텍스트 문자만 반환
- 원하는 HTML 요소를 가져온 후 마지막 단계에서 요소의 텍스트 부분만 추출

```python
'''
<html>
 <body>
  <div>
   <span>
    <a href="http://www.naver.com">
     naver
    </a>
    <a href="https://www.google.com">
     google
    </a>
    <a href="http://www.daum.net/">
     daum
    </a>
   </span>
  </div>
 </body>
</html>
'''

soup.find('a').get_text()
```

> 'naver'
> 

### find( ) + get_text( ) 함수

```python
'''
<html>
 <body>
  <div>
   <span>
    <a href="http://www.naver.com">
     naver
    </a>
    <a href="https://www.google.com">
     google
    </a>
    <a href="http://www.daum.net/">
     daum
    </a>
   </span>
  </div>
 </body>
</html>
'''

site_names = soup.find_all('a')
for site_name in site_names:
    print(site_name.get_text())
```

> naver
google
daum
> 

<aside>
💡 get_text( ) 는 리스트에 적용할 수 없으므로 for 문을 이용하여 적용해야 한다.

</aside>

### BeautifulSoupd으로 필요한 데이터 추출

- 원본

```python
from bs4 import BeautifulSoup

# 테스트용 HTML 코드
html2 = """
<html>
 <head>
  <title>작품과 작가 모음</title>
 </head>
 <body>
  <h1>책 정보</h1>
  <p id="book_title">토지</p>
  <p id="author">박경리</p>
  
  <p id="book_title">태백산맥</p>
  <p id="author">조정래</p>

  <p id="book_title">감옥으로부터의 사색</p>
  <p id="author">신영복</p>
 </body>
</html>
""" 

soup2 = BeautifulSoup(html2, "lxml")
```

```python
soup2.title
```

> <title>작품과 작가 모음</title>
> 

```python
soup2.body
```

> <body>
<h1>책 정보</h1>
<p id="book_title">토지</p>
<p id="author">박경리</p>
<p id="book_title">태백산맥</p>
<p id="author">조정래</p>
<p id="book_title">감옥으로부터의 사색</p>
<p id="author">신영복</p>
</body>
> 

```python
soup2.body.h1
```

> <h1>책 정보</h1>
> 

### select( ) 함수

- CSS 선택자 이용
- 'BeautifulSoup.select( )'의 인자로 '태그 및 속성'을 단계적으로 입력하면 원하는 요소를 찾을 수 있음
- **기본**
    - body 태그 요소 내에 h1 태그 요소를 가지고 오기
    
    ```python
    soup2.select('body h1')
    ```
    
    > [<h1>책 정보</h1>]
    > 
    
    - p태그를 포함한 요소를 모두 가지고 오기
    
    ```python
    soup2.select('body p')
    soup2.select('p') # p태그가 body 태그 안에만 있을 경우 body 태그 생략 가능
    ```
    
    > [<p id="book_title">토지</p>,
     <p id="author">박경리</p>,
     <p id="book_title">태백산맥</p>,
     <p id="author">조정래</p>,
     <p id="book_title">감옥으로부터의 사색</p>,
     <p id="author">신영복</p>]
    > 
    
- **특정 속성값 지정하여 원하는 요소만 추출**
    - 속성이 id인 경우
        
        ```python
        # p 태그 안의 id가 “book_title”인 요소만 가지고 오기(#id명)
        soup2.select('p#book_title')
        ```
        
        > [<p id="book_title">토지</p>,
         <p id="book_title">태백산맥</p>,
         <p id="book_title">감옥으로부터의 사색</p>]
        > 
        
    - 속성이 class인 경우
        
        ```python
        %%writefile C:\JupyterTest\HTML_example_my_site.html
        <!doctype html>
        <html>
          <head>
            <meta charset="utf-8">
            <title>사이트 모음</title>
          </head>
          <body>
            <p id="title"><b>자주 가는 사이트 모음</b></p>
            <p id="contents">이곳은 자주 가는 사이트를 모아둔 곳입니다.</p>
            <a href="http://www.naver.com" class="portal" id="naver">네이버</a> <br>
            <a href="https://www.google.com" class="search" id="google">구글</a> <br>
            <a href="http://www.daum.net" class="portal" id="daum">다음</a> <br>
            <a href="http://www.nl.go.kr" class="government" id="nl">국립중앙도서관</a>
          </body>
        </html>
        
        f = open('C:\JupyterTest\HTML_example_my_site.html', encoding='utf-8')
        
        html3 = f.read()
        f.close()
        
        soup3 = BeautifulSoup(html3, "lxml")
        ```
        
        ```python
        # 태그가 a이면서 class 속성값이 "portal"인 요소만 가져오기
        soup3.select('a.portal')
        ```
        
        > [<a class="portal" href="http://www.naver.com" id="naver">네이버</a>,
         <a class="portal" href="http://www.daum.net" id="daum">다음</a>]
        > 

## 이미지 추출

### 이미지 한개 추출