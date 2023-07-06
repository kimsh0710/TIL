# Django

## 개요

### Django란?

- 파이썬으로 만들어진 무료 오픈소스 웹 어플리케이션 프레임워크
- 웹사이트를 쉽고 빠르게 개발할 수 있도록 돕는 구성요소로 이루어짐

### Django의 특징

- **MVC 패턴 기반 MVT(Model-View-Controller)**
    - 장고에서는 View를 Template, Controller를 View라고 부른다.
    - Model : 데이터베이스에 엑세스하는 컴포넌트
    - View : 데이터를 가져오고 변형하는 컴포넌트
    - Template :  데이터를 사용자에게 보여주는 컴포넌트
    
- **객체 관계 매핑(ORM, Object-Realational Mapping)**
    - 데이터베이스 시스템과 모델이라는 파이썬 클래스를 연결하는 다리와 같은 역할
    - SQL 문장을 사용하지 않고도 테이블을 조작할 수 있다.
    
- **우아한 URL 설계**
    - URL을 직관적이고 쉽게 표현
    - 정규표현식을 사용하여 복잡한 URL도 표현
    - 각 URL 형태를 파이썬 함수에 1:1로 연결하도록 설계되어 있어 이해하기 쉬운 코드 작성과 편리한 개발이 가능
    
- **자체 템플릿 시스템**
    - 내부적으로 확장이 가능하고 디자인하기 쉬운 강력한 템플릿 시스템
    - 화면 디자인과 로직에 관한 코딩을 분리하여 독립적으로 프로그래밍 가능
    - HTML과 같은 텍스트형 언어를 쉽게 다룰 수 있음
    
- **캐시 시스템**
    - 동적 페이지 생성을 위한 작업은 서버에 엄청난 부하를 줌 → 장고의 캐시 시스템은 캐시용 메모리, 데이터베이스 내부, 파일 시스템 중 아무 곳에나 저장 가능
    - 캐시 단위를 페이지에서부터 사이트 전체 또는 특정 뷰의 결과, 템플릿의 일부 영역만을 지정하여 저장 가능
    
- **다국어 지원**
    - 소스 코드를 다른 나라에서도 사용할 수 있도록 텍스트 번역, 날짜/시간/숫자 포맷, 타임존 지정 등과 같은 다국어 환경을 제공
    
- **풍부한 개발 환경**
    - 소스 코드를 다른 나라에서도 사용할 수 있도록 텍스트 번역, 날짜/시간/숫자 포맷, 타임존 지정 등과 같은 다국어 환경을 제공
    
- **소스 변경 사항 자동 반영**
    - 장고는 *.py 파일의 변경 여부를 감시하고 있다가 파일이 변경되면 실행 파일에 변경 내역을 바로 반영
    - 테스트용 웹 서버를 실행 중인 상태에서 소스 파일을 수정하더라도 웹 서버를 다시 시작할 필요 없이 자동으로 새로운 파일이 반영됨

### 어플리케이션 개발 방식

- **MVT 코딩 순서**
    - 프로젝트 뼈대 만들기 : 프로젝트 및 앱 개발에  필요한 디렉토리와 파일 생성
    - 모델 코딩하기 : 테이블 관련 사항을 개발(model.py, [admin.py](http://admin.py) 파일)
    - URLconf 코딩하기 : URL 및 뷰 매핑 관계를 정의(urls.py 파일)
    - 템플릿 코딩하기 : 화면 UI 개발 (templates/ 디렉토리 하위의 *.html 파일들)
    - 뷰 코딩하기 : 어플리케이션 로직 개발 (views.py 파일)

## 설문 어플리케이션

### 어플리케이션 설계

- index.html : 최근에 실시하고 있는 질문의 리스트를 보여줌.
- detail.html : 하나의 질문에 대해 투표할 수 있도록 답변 항목을 폼으로 보여줌
- result.html : 질문에 따른 투표 결과를 보여줌

![Untitled](Django%203e0e4d0a282a45eda547baf9e46a739c/Untitled.png)

### **테이블 설계**

- **Question 테이블 설계**
    
    
    | 컬럼명 | 타입 | 제약 조건 | 설명 |
    | --- | --- | --- | --- |
    | id | integer | NotNull, PK
    AutoIncrement | Primary Key |
    | question_text | varchar(200) | NotNull | 질문 문장 |
    | pub_date | datetime | NotNull | 질문 생성 시각 |
- **Choice 테이블 설계**
    
    
    | 컬럼명 | 타입 | 제약 조건 | 설명 |
    | --- | --- | --- | --- |
    | id | integer | NotNull, PK
    AutoIncrement | Primary Key |
    | choice_text | varchar(200) | NotNull | 답변 항목 문구 |
    | votes | integer | NotNull | 투표 카운트 |
    | question | integer | NotNull, FK(Question id),
    Index | Foreign Key |

### 프로젝트 뼈대 만들기

- **프로젝트 뼈대 & 디렉토리 항목**
    
    ![Untitled](Django%203e0e4d0a282a45eda547baf9e46a739c/Untitled%201.png)
    
    ![Untitled](Django%203e0e4d0a282a45eda547baf9e46a739c/Untitled%202.png)
    
    ![Untitled](Django%203e0e4d0a282a45eda547baf9e46a739c/Untitled%203.png)
    
- **프로젝트 뼈대 만들기 순서**
    1. django-admin startproject mysite : mysite 프로젝트 생성
    2. python [manage.py](http://manage.py) startapp polls : polls라는 어플리케이션 생성
    3. notepad [setting.py](http://setting.py) : 설정 파일을 확인 및 수정
    4. python [manage.py](http://manage.py) migrate : 데이터베이스에 기본 테이블 생성
    5. python [manage.py](http://manage.py) runserver : 현재까지 작업을 개발용 웹 서버로 확인
    
- **프로젝트 생성**
    - 최상위 디렉토리 밑에 생성
        
        ```powershell
        (base) **C:\MyTest>**django-admin startproject mysite
        ```
        
    - mystie → projectsite로 이름 변경
        
        ```powershell
        (base) **C:\MyTest>**move mysite projectsite
        ```
        
- **어플리케이션 생성**
    - 프로젝트 루트를 projectsite 디렉토리로 이동
        
        ```powershell
        (base) **C:\MyTest> cd \**
        (base) **C:\MyTest> cd projectsite**
        ```
        
    - 어플리케이션 생성
        
        ```powershell
        **(base) C:\MyTest\projectsite>**python manage.py startapp polls
        ```
        
    - 확인
        
        ```powershell
        (base) C:\MyTest\projectsite>cd polls
        (base) **C:\MyTest\projectsite\polls>**dir
        ```
        
- **프로젝트 설정 파일 변경**
    - 프로젝트에 필요한 설정 값들을 [settings.py](http://settings.py) 파일에 지정
    - 루트 디렉토리를 포함한 각종 디렉토리 위치, 로그 형식, 어플리케이션 이름 등이 지정되어 있음.
    - [setting.py](http://setting.py) 파일 수정
        
        ```powershell
        (base) C:\MyTest>\projectstie>notepad setting.py
        ```
        
        <aside>
        💡 notepad [setting.py](http://setting.py) 입력해서 수정해도 되고 파일탐색기를 통해 직접 파일을 열어 수정해도 됨.
        
        </aside>
        
    - 수정 내용
        - ALLOWED_HOSTS 항목을 적절하게 지정
            
            ALLOWED_HOSTS = ['192.168.35.61', 'localhost', '127.0.0.1’]
            (초기값은 빈 리스트로 모든 사람이 접근 가능)
            
        - 어플리케이션들은 모두 설정 파일에 등록
            
            INSTALLED_APPS =[ ~, 'polls.apps.PollsConfig’, ]
            
        - 프로젝트에 사용할 데이터베이스 엔진
            
            디폴트로 SQLite3 데이터베이스 엔진을 사용하도록 설정되어 있음.
            
        - 타임존 지정
            
            TIME_ZONE = 'Asia/Seoul’
            
            UTC로 디폴트 설정 되어 있음
            
- **기본 테이블 생성**
    - 데이터베이스에 변경사항이 있을 때 반영해주는 명령 실행
        
        ```powershell
        (base) **C:\MyTest\projectsite>**python manage.py migrate
        ```
        
- **작업 확인하기**
    - 확인을 위해서 웹 서버를 실행하고, 그 웹 서버에 접속
    
    ```powershell
    (base) **C:\MyTest\projectsite>**python manage.py runserver 127.0.0.1:8000
    (base) C:\MyTest\projectsite>python manage.py runserver
    (base) C:\MyTest\projectsite>python manage.py runserver 0:8000
    ```
    
    - 웹 브라우저 열고 IP 주소 입력
- **Admin 사이트 접속**
    - 주소 검색창에 IP 주소/admin 입력
    [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
    - username, password 생성 (superuser 생성)
        
        ```powershell
        (base) **C:\MyTest\projectsite>**python manage.py createsuperuser
        ```
        
    - 다시 admin 사이트 접속해서 로그인
    
- **테이블 작성 작업**
    - 새롭게 만들 테이블에 대한 데이터의 입력, 변경, 삭제 등의 작업
    
- **골격 생성**
    
    ```powershell
    (base) C:\MyTest>tree /F projectsite
    ```
    

### Model 코딩

- Model 코딩 : 데이터베이스에 테이블을 생성하는 작업

```powershell
>notepad models.py // 테이블을 정의함
>notepad admins.py // 정의된 테이블이 Admin 화면에 보이게 함
>python manage.py makemigrations // 데이터베이스에 변경이 필요
한 사항을 추출함
>python manage.py migrate // 데이터베이스에 변경사항을 반영함
>python manage.py runserver // 현재까지 작업을 개발용 웹 서버로
확인함
```

- **테이블 정의**
    - polls 어플리케이션은 Question과 Choice 두 개의 테이블이 필요
        
        
        | 컬럼명 | 타입 | 제약 조건 | 설명 |
        | --- | --- | --- | --- |
        | id | integer | NotNull, PK
        AutoIncrement | Primary Key |
        | question_text | varchar(200) | NotNull | 질문 문장 |
        | pub_date | datetime | NotNull | 질문 생성 시각 |
        
        | 컬럼명 | 타입 | 제약 조건 | 설명 |
        | --- | --- | --- | --- |
        | id | integer | NotNull, PK
        AutoIncrement | Primary Key |
        | choice_text | varchar(200) | NotNull | 답변 항목 문구 |
        | votes | integer | NotNull | 투표 카운트 |
        | question | integer | NotNull, FK(Question id),
        Index | Foreign Key |
    - 테이블은 [models.py](http://models.py) 파일에 정의
        
        ```python
        from django.db import models
        
        # Create your models here.
        
        class Question(models.Model):
            question_text = models.CharField(max_length=200)
            pub_date = models.DateTimeField('date published')
        
            def __str__(self):
                return self.question_text
        
        class Choice(models.Model):
            question = models.ForeignKey(Question, on_delete=models.CASCADE)
            choice_text = models.CharField(max_length=200)
            votes = models.IntegerField(default=0)
        
            def __str__(self):
                return self.choice_text
        ```
        
- **admin 사이트에 테이블 반영**
    - [admin.py](http://admin.py) 파일에 테이블 등록
        
        ```python
        from django.contrib import admin
        
        # Register your models here.
        
        from polls.models import Question, Choice
        
        admin.site.register(Question)
        admin.site.register(Choice)
        ```
        
        <aside>
        💡 [models.py](http://models.py/) 모듈에서 정의한 Question, Choice 클래스를 임포트 하고, admin.site.register() 함수를 사용하여 임포트 한 클래스를 Admin 사이트에 등록
        
        </aside>
        
- **데이터베이스 변경사항 반영**
    - 테이블의 신규 생성, 테이블의 정의 변경 등 데이터베이스에 변경이 필요한 사항이 있으면, 이를 데이터베이스에 실제로 반영해주는 작업
        
        ```powershell
        (base) C:\MyTest\projectsite>python manage.py makemigrations
        ```
        
        <aside>
        💡 polls/migrations 디렉토리 하위에 마이그레이션 파일들이 생김
        
        </aside>
        
    - migrate 명령으로 데이터베이스에 테이블을 생성
        
        ```powershell
        (base) C:\MyTest\projectsite>python manage.py migrate
        ```
        
- **작업 확인**
    - runserver 용으로 별도의 cmd창을 열어 사용
        
        ```powershell
        (base) C:\MyTest\projectsite>python manage.py runserver 127.0.0.1:8000
        (base) C:\MyTest\projectsite>python manage.py runserver
        (base) C:\MyTest\projectsite>python manage.py runserver 0:8000
        ```
        
    - Admin 사이트에 접속

### View 및 Template

- **처리 흐름 설계**
    - 사용자에게 보여지는 페이지가 3개이므로, 3개의 템플릿 파일이 필요
        
        ![Untitled](Django%203e0e4d0a282a45eda547baf9e46a739c/Untitled%204.png)
        
    - URL/뷰 매핑을 URLconf 라고 하며 [urls.py](http://urls.py/) 파일에 작성
        
        ![Untitled](Django%203e0e4d0a282a45eda547baf9e46a739c/Untitled%205.png)
        
    - URLconf를 먼저 코딩한 후에 뷰, 템플릿 또는 템플릿, 뷰 순서로 코딩하는 것이 일반적
    
- **URLconf 코딩**
    - [urls.py](http://urls.py/)(C:\MyTest\projectsite\mysite) 파일에 코딩
        
        ```python
        """mysite URL Configuration
        
        The `urlpatterns` list routes URLs to views. For more information please see:
            https://docs.djangoproject.com/en/2.0/topics/http/urls/
        Examples:
        Function views
            1. Add an import:  from my_app import views
            2. Add a URL to urlpatterns:  path('', views.home, name='home')
        Class-based views
            1. Add an import:  from other_app.views import Home
            2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
        Including another URLconf
            1. Import the include() function: from django.urls import include, path
            2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
        """
        from django.contrib import admin
        from django.urls import path, **include**
        
        urlpatterns = [
            path('admin/', admin.site.urls),
        
            **# 수정
            path('polls/', include('polls.urls')),**
        ]
        ```
        
    - [urls.py](http://urls.py/)(C:\MyTest\projectsite\mysite\polls) 파일에 코딩
        
        ```python
        from django.urls import path
        from polls import views
        
        app_name = 'polls'
        urlpatterns = [
            path('', views.index, name='index'),      # /polls/
            path('<int:question_id>/', views.detail, name='detail'),       # /polls/5/
            path('<int:question_id>/results/', views.results, name='results'),     # /polls/5/results/
            path('<int:question_id>/vote/', views.vote, name='vote'),      # /polls/5/vote/
        ]
        ```
        
- **뷰 함수 index() 및 템플릿 작성**
    
    ![Untitled](Django%203e0e4d0a282a45eda547baf9e46a739c/Untitled%206.png)
    
    - 위 내용을 구현하기 위한 템플릿 파일 index.html 작성
        
        ```html
        {% if latest_question_list %}
            <ul>
            {% for question in latest_question_list %}
                <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
            {% endfor %}
            </ul>
        {% else %}
            <p>No polls are available.</p>
        {% endif %}
        ```
        
    - pollls\views.py에 index() 함수 작성
        
        ```python
        from django.shortcuts import get_object_or_404, render
        from django.http import HttpResponseRedirect
        from django.urls import reverse
        
        from polls.models import Choice, Question
        
        def index(request):
            latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
            context = {'latest_question_list': latest_question_list}
            return render(request, 'polls/index.html', context)
        ```
        
    
- **뷰 함수 detail() 및 템플릿 작성**
    
    ![Untitled](Django%203e0e4d0a282a45eda547baf9e46a739c/Untitled%207.png)
    
    - 3개의 질문(index.html) 중 하나를 선택했을 때 질문에 대한 답변 항목을 보여주는 화면을 구현하기 위한 템플릿 파일 detail.html 작성
        
        ```html
        <h1>{{ question.question_text }}</h1>
        
        {% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}
        
        <form action="{% url 'polls:vote' question.id %}" method="post">
        {% csrf_token %}
        {% for choice in question.choice_set.all %}
            <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}" />
            <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br />
        {% endfor %}
        <input type="submit" value="Vote" />
        </form>
        ```
        
    - pollls\views.py에 detail() 함수 작성
        
        ```python
        def detail(request, question_id):
            question = get_object_or_404(Question, pk=question_id)
            return render(request, 'polls/detail.html', {'question': question})
        ```
        
- **뷰 함수 vote() 및 리다이렉션 작성**
    - vote() 뷰 함수의 호출과 연계된 URL은 detail.html 템플릿 파일에서
    받음
    - views.py파일을 열고 vote() 뷰 함수의 내용 입력
        
        ```python
        def vote(request, question_id):
            question = get_object_or_404(Question, pk=question_id)
            try:
                selected_choice = question.choice_set.get(pk=request.POST['choice'])
            except (KeyError, Choice.DoesNotExist):
                # Redisplay the question voting form.
                return render(request, 'polls/detail.html', {
                    'question': question,
                    'error_message': "You didn't select a choice.",
                })
            else:
                selected_choice.votes += 1
                selected_choice.save()
                # Always return an HttpResponseRedirect after successfully dealing
                # with POST data. This prevents data from being posted twice if a
                # user hits the Back button.
                return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        ```
        
- **뷰 함수 results() 및 리다이렉션 작성**
    - results()뷰 함수의 호출과 연계된 URL은 votes() 뷰 함수의 리다이렉트 결과
    - 데이터를 처리한 후에 그 결과를 보여주는 페이지로 리다이렉트 시켜주기 위해 votes() 뷰 함수에 실행
    - [views.py](http://views.py/) 파일을 열고 results() 뷰 함수의 내용을 추가
        
        ```python
        def results(request, question_id):
            question = get_object_or_404(Question, pk=question_id)
            return render(request, 'polls/results.html', {'question': question})
        ```
        
    - 템플릿 파일 results.html 작성
        
        ```html
        <h1>{{ question.question_text }}</h1>
        
        <ul>
        {% for choice in question.choice_set.all %}
            <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
        {% endfor %}
        </ul>
        
        <a href="{% url 'polls:detail' question.id %}">Vote again?</a>
        ```
        
- **작업 확인하기**
    
    ```powershell
    (base) C:\MyTest\projectsite>python manage.py runserver 127.0.0.1:8000
    (base) C:\MyTest\projectsite>python manage.py runserver
    (base) C:\MyTest\projectsite>python manage.py runserver 0:8000
    ```
    
    - 웹브라우저에서 [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
        - Questions 데이터 입력
        - Choices 데이터 입력
    - 잘 적용되었는지 확인
        
        [http://127.0.0.1:8000/polls](http://127.0.0.1:8000/polls)