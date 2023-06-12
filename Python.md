# Python

## **자료형과 기본 문법**

### 자료형 (Data Type)

**가. 일반 자료형 (Scalar 타입, immutable(값 변경 불가)**

> 정수 : 음수, 0, 양수로 구성된 숫자
> 
> 
> 실수 : 소수점을 가진 숫자
> 
> 논리 : True, False (꼭 첫글자는 대문자로)
> 
> 함수 : 기능적인 코드를 표현
> 
> None : null 값 의미
> 

**나. 집합 자료형**

> 문자열(str) : 값 변경 불가(immutable), “ 또는 “” 또는 “”” 으로 표현
> 
> 
> 리스트(list) : 중복 허용, 값 변경 가능(mutable), [] 표현
> 
> 튜플(tuple) : 중복 허용, 값 변경 불가(immutable), () 표현
> 
> 셋(set) : 중복 허용 불가, 반드시 immutable 값만 저장 가능, {} 표현
> 
> 딕셔너리(dict) : {”key”:”value”} 표현
> 

**다. 이스케이프 문자**

| escape 문자 | 의미 |
| --- | --- |
| ‘\n’ | 새로운 라인 추가 |
| ‘\t’ | 탭(tab) 추가 |
| ‘\r’ | 리턴 기능 |
| ‘\b’ | 백스페이스 기능 |
| ‘\’’ | 따옴표 기능 |
| ‘\’’’’ | 쌍따옴표 기능 |
| ‘\\’ | 백슬래쉬 기능 |

```python
# 이스케이프 문자 (escape 문자) => \는 특별한 의미를 갖는다.
print("c:\\temp") # 파일 경로 지정시 주로 사용됨.
print("Hello\nworld") # 엔터 친 효과
print("Hello\tworld") # tab키 친 효과
print("\'") # '
print("\"") # "
```

```python
# row string : 이스케이프 문자를 무시한다. 정규표현식(regular expression):패턴매칭
print(r"c:\\temp") # c:\\temp
print(r"Hello\nworld") # Hello\nworld
print(r"Hello\tworld") # Hello\tworld
print(r"\'") # \'
print(r"\"") # \"
```

### **변수 (Variable)**

1. **목적 : 데이터 저장**
2. **특징 : 모든 변수는 참조형 변수이다.**
3. **기본 문법**
    1. 변수명 = 값
    2. 변수명 = 변수명2 = 변수명3 = 값
    3. 변수명, 변수명2, 변수명3 = 값, 값2, 값3 (반드시 개수 일치)
4. **기본 문법 예제**
    1. 기본
    
    ```python
    
    num = 4
    name = "홍길동"
    address = "서울"
    height = 174.2
    isMarried = True
    email =["aa@daum.net","bb@google.com"]
    info ={
        "핸드폰":["010", "011"],
        "애완동물":["강아지","고양이"]
    }
    ```
    
    ```python
    print(num, id(num)) # 4 140736376194816 (id() : 주소값)
    print(name, id(name)) # 홍길동 1233104217360
    print(address, id(address)) # 서울 1233104335472
    print(height, id(height)) # 174.2 1233104169008
    print(isMarried, id(isMarried)) # True 140736027658064
    print(email, id(email)) # ['aa@daum.net', 'bb@google.com'] 1233104063936
    print(info, id(info)) # {'핸드폰': ['010', '011'], '애완동물': ['강아지', '고양이']} 1233104013952
    ```
    
    <aside>
    💡 변수를 지정하면 각자 주소값도 함께 지정된다. 주소값 확인 id( )
    
    </aside>
    
    b. 동시 할당
    
    ```python
    # 값 하나를 여러 변수에 저장
    n=n1=n2=10
    print(n,n1,n2) # 10 10 10
    ```
    
    ```python
    # 반드시 개수가 일치해야 한다. (중요)
    name, age, address = "홍길동",20,"서울"
    print(name,age,address) # 홍길동 20 서
    ```
    
    ```python
    # dummy variable ==> _(underscore) 이용
    a, b, _ = 10, 20, 30
    print(a, b) # a b
    ```
    
    ```python
    # dict는 변수에 key 값이 저장됨.
    a, b = {"x":"홍길동", "y":"이순신"}
    print(a,b) # x y
    ```
    
5. **변수 타입 체크**
    
    
    | 변수 지정 | 타입 |
    | --- | --- |
    | a=10 | <class 'int'> |
    | b=3.14 | <class 'float'> |
    | c=True | <class 'bool'> |
    | x=None | <class 'NoneType'> |
    | y=lambda : print(”hello word”) | <class 'function'> |
    | d=[10,20,30] | <class 'list'> |
    | e=(10,20,30) | <class 'tuple'> |
    | f={10,20,30} | <class 'set'> |
    | g={”key”:100} | <class 'dict'> |
    
6. **문자열의 종류**
    
    
    | 종류 | 표현 | 타입 | 설명 |
    | --- | --- | --- | --- |
    | unicode | h=”hello” | unicode string <class 'str'> | 전세계 모든 문자를 다루도록 설계된 표준 문자 전산 처리 방식.
    (앞으로의 파이썬에서는 모두 유니코드를 사용해야 함.) |
    | byte | h=b”hello” | byte string <class 'bytes'> | 웹에서 문자를 가져왔을 때(크롤링)의 형식. 우리가 읽을 수 있도록 인코딩 필요함. |
    

### 표준 출력 (print)

1. **기본 문법**
    
    ```python
    print(value, ..., sep=' ', end='\n' )
    ```
    
    <aside>
    💡 value 여러개 입력 가능
    
    sep=’ ‘ : 값들의 구분자와 함께 출력
    
    end=’이스케이프 문자’
    
    </aside>
    
    ```python
    # 위 설정 값 수정도 가능함.
    print(1,2,3,4) # 1 2 3 4
    print(1,2,3,4, sep=',') # 1,2,3,4 <- 구분자인 쉼표와 같이 출력
    print(1,2,3,4, end=" ") 
    # 1 2 3 4 1 2 3 4 <- 값들의 구분을 공백으로. 만약 end='\n'이라면 값들 사이에 엔터가 적용되어 출력
    ```
    

### 표준 입력 (input)

1. **기본 문법**
    
    ```python
    a = input("문자열")
    ```
    
    ```python
    name = input("이름 입력 : ")
    age = input("나이 입력 : ")
    print(name, age) # 홍길동 20 <- 실제로 입력한 값이 출력 됨.
    ```
    
    <aside>
    💡 키보드로 받아들이는 데이터는 모두 문자로 인식한다.
    
    키보드로 받아들이는 데이터로 연산하려면 int( )를 통해 숫자형으로 변환해주어야 한다.
    
    </aside>
    
    ```python
    name = input("이름 입력")
    age = input("나이 입력")
    grade = int(input("학년 입력"))
    print(name, int(age) + 1, grade+1) # int() 사용하여 숫자로 변경
    ```
    

### 객체 안의 함수 정보 보기 (참고)

```python
# 객체 안의 함수 보기
print(dir(str)) # 문자열 객체 (클래스), str

'''
['capitalize', 'casefold', 'center', 'count', 'encode', 
'endswith', 'expandtabs', 'find', 'format', 'format_map',
 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal',
  'isdigit', 'isidentifier', 'islower', 'isnumeric',
   'isprintable', 'isspace', 'istitle', 'isupper',
    'join', 'ljust', 'lower', 'lstrip', 'maketrans', 
    'partition', 'replace', 'rfind', 'rindex', 'rjust',
     'rpartition', 'rsplit', 'rstrip', 'split', 
     'splitlines', 'startswith', 'strip', 'swapcase',
      'title', 'translate', 'upper', 'zfill']
'''

print(dir(list)) # 리스트 객체 (클래스), List
'''
['append', 'clear', 'copy', 'count', 'extend', 'index',
 'insert', 'pop', 'remove', 'reverse', 'sort']
'''

print(dir(tuple)) # 튜플 객체 (클래스), tuple, 수정할 함수가 제공 안됨.
'''
['count', 'index']
'''

print(dir(set)) # 셋 객체 (클래스), set
'''
'add', 'clear', 'copy', 'difference', 'difference_update',
'discard', 'intersection', 'intersection_update',
'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove',
'symmetric_difference', 'symmetric_difference_update',
'union', 'update']
'''

print(dir(dict)) # 딕트(딕셔너리) 객체 (클래스), dict
'''
['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 
'pop', 'popitem', 'setdefault', 'update', 'values']
'''

print(dir(int)) # 인트 객체 (클래스), int
'''
['as_integer_ratio', 'bit_length', 'conjugate',
'denominator', 'from_bytes', 'imag', 'numerator',
 'real', 'to_bytes']
'''

### 빌트인즈 객체 ==> .없이 사용 가능
print(dir(__builtins__))
# print(), dir(), input(), abs() 등이 포함 됨.
'''
['ArithmeticError', 'AssertionError', 'AttributeError',
'BaseException', 'BlockingIOError', 'BrokenPipeError',
'BufferError', 'BytesWarning', 'ChildProcessError',
'ConnectionAbortedError', 'ConnectionError',
'ConnectionRefusedError', 'ConnectionResetError',
'DeprecationWarning', 'EOFError', 'Ellipsis',
'EnvironmentError', 'Exception', 'False',
'FileExistsError', 'FileNotFoundError', 
'FloatingPointError', 'FutureWarning', 
'GeneratorExit', 'IOError', 'ImportError', 
'ImportWarning', 'IndentationError', 'IndexError', 
'InterruptedError', 'IsADirectoryError', 'KeyError', 
'KeyboardInterrupt', 'LookupError', 'MemoryError', 
'ModuleNotFoundError', 'NameError', 'None', 
'NotADirectoryError', 'NotImplemented', 
'NotImplementedError', 'OSError', 'OverflowError', 
'PendingDeprecationWarning', 'PermissionError', 
'ProcessLookupError', 'RecursionError', 'ReferenceError', 
'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 
'StopAsyncIteration', 'StopIteration', 'SyntaxError', 
'SyntaxWarning', 'SystemError', 'SystemExit', 
'TabError', 'TimeoutError', 'True', 'TypeError', 
'UnboundLocalError', 'UnicodeDecodeError', 
'UnicodeEncodeError', 'UnicodeError', 
'UnicodeTranslateError', 'UnicodeWarning', 
'UserWarning', 'ValueError', 'Warning', 'WindowsError', 
'ZeroDivisionError']
'''
```

### 포맷 출력

1. **.format ( ) 방식**
    1. **문자열 데이터  표현**
        
        ```python
        mesg = "이름:{}".format('홍길동')
        print(mesg) # 이름:홍길동 <- { } 안에 format(값)이 출력됨.
        
        mesg = '이름:{0}'.format('홍길동')
        print(mesg) # 이름:홍길동 <- {}안에 format(값,값2, ...)의 순서 지정하여 출력
        
        mesg = '이름:{0}, 나이:{1}'.format('홍길동',20)
        print(mesg) 
        # 이름:홍길동 <- 이름에는 0번째, 나이에는 1번째가 지정되었으므로 format( )안의 여러 값의 순서대로 출력됨.
        ```
        
    2. **수치 데이터 표현**
        
        ```python
        mesg = '{0}'.format(123456789)
        print(mesg) # 123456789
        
        mesg = '{0:f}'.format(123456789) # :f : 실수로 출력하라
        print(mesg) # 123456789.000000
        
        mesg = '{0:.3f},{0:.9f}'.format(123.4567) # .3f : 소수점 세자리의 실수로 출력하라
        print(mesg) # 123.457,123.456700000
        
        mesg = '{0:,}'.format(123456789) # 세자리마다 쉼표를 찍어 출력하라
        print(mesg) # 123,456,789
        ```
        
    3. **key 사용 (중요⭐)**
        
        ```python
        mesg = '이름: {username}, 나이: {age}'.format(username='홍길동', age=20)
        print(mesg) # 이름: 홍길동, 나이: 20
        ```
        
    4. **unpacking - 문자열/리스트**
        
        ```python
        mesg = '{0}:{1}:{2}'.format(*'홍길동') # str unpacking
        print(mesg)  # 홍:길:동
        
        mesg = '{0}:{1}:{2}'.format(*['홍길동', '이순신', '강감찬']) # list unpacking
        print(mesg) # 홍길동:이순신:강감찬
        ```
        
    5. **unpacking - dict**
        
        ```python
        person = {'username': '홍길동', 'age': 20} # unpacking ==> username=홍길동, age=20
        mesg = '이름: {username}, 나이: {age}'.format(**person)
        print(mesg) # 이름: 홍길동, 나이: 20
        ```
        
2. **% 지정 방식**
    
    %d : 정수, %s : 문자열, %c : 문자, %f : 실수
    
    **a.  숫자 바로 대입**
    
    ```python
    print("I eat %d apples." % 3)
    # 'I eat 3 apples.'
    ```
    
    <aside>
    💡 포맽팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다.
    
    </aside>
    
    ```python
    print("Error is %d%." % 98)
    # Error is 98%.
    ```
    
    **b. 문자열 바로 대입**
    
    ```python
    print("I eat %s apples." % "five")
    # 'I eat five apples.'
    ```
    
    **c. 숫자값을 나타내는 변수로 대입**
    
    ```python
    number = 3
    print("I eat %d apples." % number)
    # 'I eat 3 apples.
    ```
    
    **d. 두개 이상의 값 넣기**
    
    ```python
    number = 10
    day = "three"
    print("I ate %d apples. so I was sick for %s days." % (number, day))
    # 'I ate 10 apples. so I was sick for three days.'
    ```
    
3. **포맷 코드와 숫자 함께 사용하기**
    1. **정렬과 공백**
        
        ```python
        print("%10s" % "hi")
        # '        hi'
        # %10s : 전체 길이가 10개인 문자열 공간에서 대입되는 값을 오른쪽으로 정렬하고 그 앞은 공백으로
        ```
        
        ```python
        print("%-10sjane." % 'hi')
        # 'hi        jane.'
        # %-10s : 전체 길이가 10개인 문자열 공간에 대입되는 값을 왼쪽으로 정렬(jane 제외 10 글자)
        ```
        
    2. **소수점 표현하기**
        
        ```python
        print("%0.4f" % 3.42134234)
        # '3.4213'
        ```
        
        ```python
        print("%10.4f" % 3.42134234)
        # '    3.4213'
        # %10.4f : 전체 길이가 10글자(대입 값은 오른쪽 정렬), 소수점 4자리까지 출력
        ```
        
4. **f 문자열 포매팅**
    1. **문자열**
        
        ```python
        name = '홍길동'
        age = 30
        print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
        # '나의 이름은 홍길동입니다. 나이는 30입니다.'
        ```
        
    2. **딕셔너리**
        
        ```python
        d = {'name':'홍길동', 'age':30}
        print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')
        # '나의 이름은 홍길동입니다. 나이는 30입니다.'
        ```
        
        <aside>
        💡 key값을 이용하여 value 값을 대입할 수 있다.
        
        </aside>
        
    3. **정렬**
        
        ```python
        print(f'{"hi":<10}')  # 왼쪽 정렬(문자열 길이 = 10)
        # 'hi        '
        print(f'{"hi":>10}')  # 오른쪽 정렬(문자열 길이 = 10)
        # '        hi'
        print(f'{"hi":^10}')  # 가운데 정렬(문자열 길이 = 10)
        # '    hi    '
        ```
        
        ```python
        print(f'{"hi":=^10}')  # 가운데 정렬하고 '=' 문자로 공백 채우기(문자열 길이 = 10)
        # '====hi===='
        print(f'{"hi":!<10}')  # 왼쪽 정렬하고 '!' 문자로 공백 채우기(문자열 길이 = 10)
        # 'hi!!!!!!!!'
        ```
        

## 연산자

### 산술 연산자

1. **산술 및 대입 연산자**
    
    
    | 종류 | 설명 |
    | --- | --- |
    | + | 더하기 |
    | - | 빼기 |
    | * | 곱하기 |
    | / | 나누기 |
    | % | 나머지 반환 |
    | // | 몫을 반환 |
    | ** | 지수 승 |
    
    ```python
    a = 10
    b = 3
    print(a+b)
    print(a-b)
    print(a*b)
    print("h"*10) # 문자열 x 숫자 => 숫자만큼 문자열이 반복 출력됨.
    print(a/b)    # 3.3333333333333335
    print(a % b)  # 1  ,  Modulus
    print(a//b)   # 3  ,  Floor Division   소수점 버림
    print(a**b)   # square ( 제곱 )
    ```
    
    ```python
    # 몫과 나머지를 한번에 반환 (tuple로 반환)
    a = 10
    b = 3
    result = divmod(10, 3)
    print(result) # (3, 1)
    ```
    
    ```python
    # name, age, address = ("홍길동", 20, "서울") 과 같은 방법
    x, y = divmod(10, 3) # 일반적임
    print(x, y) # 3 1
    ```
    
2. **대입 연산자**
    
    ```python
    n = 10
    n2 = 4
    
    n += n2 # n = n + n2
    print(n,n2) # 14 4
    
    n -= n2 # n = n - n2
    print(n,n2) # 10 4
    
    n *= n2 # n = n * n2
    print(n,n2) # 40 4
    
    n /= n2 # n = n / n2
    print(n,n2) # 10.0 4
    
    n //= n2 # n = n // n2
    print(n,n2) # 2.0 4
    
    n **= n2 # n = n ** n2
    print(n,n2) # 16.0  4
    ```
    
    ```python
    # 대입 연산자 심화
    a = b = c = 1
    name, age, address = "홍길동",20,"서울" # 중요, 개수가 반드시 일치해야 함.
    print(name,age,address)
    print(a,b,c)
    
    # 변수에 값 지정할 때 개수가 달라도 된다. packing
    
    x = [10,20,30] # 변수 x 하나에 리스트 1개 지정 => 개수 일치
    x, y, z = [10,20,30]
    #x, y = [10,20,30] # 에러 : 변수 x, y 두개에 리스트 1개 지정 됨 => 개수 불일치
    
    x, *y = [10,20,30]
    print(x,y) # 10 [20, 30],    *로 unpacking 해주면 x 나머지 값들은 리스트로 묶임
    
    x, *y = (10,20,30)
    print(x,y) # 10 [20, 30],    *로 unpacking 해주면 x 나머지 값들은 리스트로 묶임
    
    x, *y = {10,20,30}
    print(x,y) # 10 [20, 30]
    
    v1, *v2 = [10,20,30] # [10,20,30]의 값의 개수는 list 한개
    print(v1,v2)  # 10 [20, 30]
    
    # dict는 key 값이 저장된다.
    a, *b = {"x":"홍길동", "y":"이순신", "z":"유관순"}
    print(a, b) # x ['y', 'z']
    
    # 제일 앞에 있는 변수에도 * 가능
    *x, y, z = {10,20,30,40,50}
    print(x,y,z) # [40, 10, 50] 20 30
    ```
    

1. **비교 연산자**
    
    
    | 종류 | 설명 |
    | --- | --- |
    | A > B | A가 B보다 크다 |
    | A<B | A가 B보다 작다 |
    | A==B | A와 B가 같다 |
    | A<=B | A가 B와 같거나 작다 |
    | A>=B | A가 B와 같거나 크다 |
    | A!=B | A와 B는 같지 않다 |
2. **논리 연산자**
    
    ```python
    print(True and True)   # True
    print(True and False)  # False
    print(False and True)  # False
    print(False and False) # False
    print(True or True)    # True
    print(True or False)   # True
    print(False or True)   # True
    print(False or False)  # False
    print(not True)        # False
    print(not False)       # True
    ```
    
    ```python
    # False로 처리되는 data (외우기)
    print(not 0)
    print(not "")
    print(not None)
    print(not [])
    print(not {}) # 비어있는 dict
    print(not set()) # 비어있는 set
    
    # => 모두 True로 반환된다.
    ```
    
    <aside>
    💡 False로 처리되는 data (중요⭐)
    
    </aside>
    
3. **멤버쉽 연산자 (in 연산자)**
    
    집합형 데이터 안에 지정된 값이 포함되어 있는지 체크하여 bool 타입으로 반환
    
    ```python
    n = [10,9,8]
    result = 10 in n
    print("10포함 여부: ", result) # 10포함 여부: True
    ```
    
    ```python
    # dict는 key 존재 여부를 확인
    n = {"name":"홍길동","age":20}
    result = "name" in n
    print("name 키포함 여부: ", result) # name 키포함 여부: True
    ```
    

### 데이터 형변환

<aside>
💡 **일반 데이터의 형변환**

| 함수 | 설명 |
| --- | --- |
| int(값) | 정수로 변경 |
| float(값) | 실수로 변경 |
| bool(값) | bool로 변경 |

**집합형 데이터의 형변환**

| 함수 | 설명 |
| --- | --- |
| str(값) | str로 변경 |
| list(값) | list로 변경 |
| tuple(값) | tuple로 변경 |
| set(값) | set로 변경 |
| dict(값) | dict로 변경 |
</aside>

1. **int(정수)로 변환**
    
    ```python
    print( int(3.5) )    # 3
    print( int(-3.5) )   # -3
    print( int(True) )   # 1
    print( int(False) )  # 0
    print( int("123") )  # 123
    ```
    
2. **float(실수)으로 변환**
    
    ```python
    print( float(3) )                     # 3.0
    print( float(-3) )                    # -3.0
    print( float(True) )                  # 1.0
    print( float(False) )                 # 0.0
    print( float("123.34") )              # 123.34
    print( float("123") )                 # 123.0
    ```
    

## 집합형

### 문자열 자료형(str)

- **개요**
    - ‘ ’ 또는 “ “ 똔는 “”” “”” 또는 ‘”” ‘”” 사용
    - 생성된 문자열은 변경이 불가능하다. (immutable)
    - 순서형으로써 문자열 내 순서를 갖는다.
    - 다양한 형태의 함수가 제공된다.
    - 색인 및 슬라이싱 방식으로 특정 문자 및 임의의 문자열을 추출할 수 있다.
- **str 객체 함수 확인**
    
    ```python
    print(dir(str))
    '''
    ['capitalize', 'casefold', 'center', 'count', 'encode', 
    'endswith', 'expandtabs', 'find', 'format', 'format_map',
     'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal',
      'isdigit', 'isidentifier', 'islower', 'isnumeric',
       'isprintable', 'isspace', 'istitle', 'isupper',
        'join', 'ljust', 'lower', 'lstrip', 'maketrans', 
        'partition', 'replace', 'rfind', 'rindex', 'rjust',
         'rpartition', 'rsplit', 'rstrip', 'split', 
         'splitlines', 'startswith', 'strip', 'swapcase',
          'title', 'translate', 'upper', 'zfill']
    '''
    ```
    
    <aside>
    💡 반드시 문자열.함수 형태로 사용해야 한다.
    
    </aside>
    
- **문자열 주요 함수**
    
    ```python
    s = "sequence"
    
    print("1. 문자열 길이:", len(s)) # 8
    print("2. 특정문자 포함횟수:", s.count('e')) # 3
    print("3. 소문자로:", "HeLLo".lower()) # hello
    print("4. 대문자로:", "HeLLo".upper()) # HELLO
    print("5. swap 문자로(대->소,소->대:", "HeLLo".swapcase()) # hEllO
    ```
    
    ```python
    print("6. 공백제거 및 특정문자 제거:\n") # SQL의 Ltrm, Rtrim, trim 기능과 유사
    print("    HeLLo    ".lstrip()) # HeLLo     => lstrip(공백) : 왼쪽 공백 삭제
    print("HHeLLH".lstrip("H")) # eLLH => lstrip("특정문자") : 왼쪽에 위치한 특정문자 삭제
    print(len("    HeLLo    ".lstrip())) # 9 => lstrip으로 왼쪽 공백 삭제 후의 문자열 길이
    print("    HeLLo    ".rstrip()) #     HeLLo => rstrip(공백) : 오른쪽 공백 삭제
    print("HHeLLHH".rstrip("H")) # HHeLL => rstrip("특정문자") : 오른쪽에 위치한 특정 문자 삭제
    print("    HeLLo    ".strip()) # HeLLo => strip(공백) : 양쪽 공백 삭제
    print("HHeLLHH".strip("H")) # eLL => strip("특정문자") : 양쪽에 있는 특정문자 삭제
    print(len("    HeLLo    ".strip())) # 5 # => 양쪽 공백 삭제 후의 문자열 길
    ```
    
    ```python
    print("7. 문자열 변경:", "HeLHO".replace('H', 'A')) # AeLAO
    
    # 구분자 명시하여 문자열 나누기 -> 리스트로 출력
    print("8. 구분자:", "aaa/bbb/ccc".split("/")) # ['aaa', 'bbb', 'ccc'] 
    print("8. 구분자:", "aaa,bbb,ccc".split(",")) # ['aaa', 'bbb', 'ccc']
    ```
    
    ```python
    print('9. 특정 글자 시작 : ', s.startswith('s'), s.startswith('a')) # True False
    print('10. 특정 글자 끝 : ', s.endswith('e'), s.endswith('x')) # True False
    ```
    
    ```python
    print("11. 문자로만 구성?", "대한Heloo".isalpha())  # True
    print("11. 문자로만 구성?", "12".isalpha())   # False
    
    print("11. 숫자로만 구성?", "12".isnumeric())   # True
    ```
    
    ```python
    s = "sequence"
    
    print("12. S.find(sub[, start[, end]]) -> int") # find : 찾고자 하는 문자의 인덱스를 반환
    print("12. 검색위치1:", s.find('e')) # 1
    print("12. 검색위치2:", s.find('e', 2)) # 4
    print("12. 검색위치2:", s.find('x', 2)) # -1, 못찾으면 -1 반환
    print("12. 검색위치3:", s.rfind('e')) # 7, 반환될 index 중 가장 큰 인덱스 값 반환
    ```
    
    ```python
    print("13. join:", ",".join(["A", "B", "C"])) # A,B,C (중요)
    print("13. join:", " 와 ".join(["A", "B", "C"])) # A 와 B 와 C  (중요)
    ```
    
    <aside>
    💡 "구분자".join : 리스트 안의 값들을 문자열로 반환
    
    </aside>
    
    ```python
    # SQL의 Lpad, Rpad와 비슷한 기능
    
    # center : 20 자리수로 표시하고 _로 마킹 (문자열은 가운데 정렬)
    print("14. center:", "Hello".center(20, "_")) # _______Hello________
    
    # rjust: 20 자리수로 표시하고 _로 마킹 (문자열은 오른쪽 정렬)
    print("15. rjust:", "Hello".rjust(20, "_")) # _______________Hello
    
    # ljust: 20 자리수로 표시하고 _로 마킹 (문자열은 왼쪽 정렬)
    print("16. ljust:", "Hello".ljust(20, "_")) # 20 자리수로 표시하고 _로 마킹
    ```
    
    ```python
    print("17. capitalize:", "heLLOX".capitalize()) # 첫글자 대문자
    ```
    
- **문자열 연산하기**
    1. **문자열 더해서 연산하기**
        
        ```python
        head = "Python"
        tail = " is fun!"
        print(head + tail) # 문자열을 공백 없이 합쳐줌
        # 'Python is fun!'
        ```
        
    2. **문자열 곱하기**
        
        ```python
        a = "python"
        print(a * 2 )
        # 'pythonpython'
        ```
        
- **문자열 종류**
    
    > s="hello" ==> unicode string, 일반적으로 사용하는 문자열
    > 
    > 
    > s2=b"hello" ==> byte string, binary 기반, 네트워크 이용한 경우에는 bytees string으로 처리된다.
    > 
    1. **unicode --> bytes ( 암호화 작업 : encode 함수 )**
        
        ```python
        s = "hello" # unicode
        
        s2 = s.encode('utf-8')
        print(s, s2) # hello b'hello'
        print(type(s),type(s2)) # <class 'str'> <class 'bytes'>
        ```
        
    2. **bytes --> unicode ( 복호화 작업 : decode 함수 )**
        
        ```python
        s2 = s.encode('utf-8')
        
        s3 = s2.decode("utf-8")
        print(s2, s3) # b'hello' hello
        print(type(s2),type(s3)) # <class 'bytes'> <class 'str'>
        ```
        
- **문자열 인덱싱 & 슬라이싱**
    1. **인덱싱(indexing)**
        
        ```python
        m = "대한민국"
        
        print("1:", m[0])  #  대
        print("2:", m[-1]) #  국
        print("2:", m[2]) #  민
        print("2:", m[-3]) #  한
        ```
        
    2. **슬라이싱(slicing)**
        
        <aside>
        💡 m[start:end:step]
        
        start : 시작 idx 값, 생략하면 맨처음부터
        end : 끝 inx 값, end값은 포함 안됨, 생랼하면 맨끝까지
        step : 기본값 1
        
        </aside>
        
        ```python
        print("3:", m[0:3]) # 대한민
        print("4:", m[1:]) # 한민국
        print("5:", m[:2]) #  대한
        ```
        
        ```python
        print("6:", m[-3:-1]) # 한민
        print("7:", m[-3:]) #  한민국
        print("7:", m[:-1]) #  대한민
        ```
        
        ```python
        print("8:", m[0:3:2]) #대민
        print("9:", m[:])   #대한민국
        ```
        
        ```python
        print("11:", m[::-1])    # 국민한대
        print("11:", m[::-2])    # 국한
        ```
        

### 리스트(list)

- **개요**
    - 대괄호([ ]) 사용하며 서로 다른 데이터 타입도 저장 가능
    - 순서가 있고 중복 허용 가능
    - 데이터 변경 가능한 mutable한 특징
    - 문자열과 동일한 인덱싱과 슬라이싱 사용 가능
    
- **리스트 생성**
    
    ```python
    string_list = ['abc', 'defghi']
    int_list = [1, 2, 3, 4]
    empty_list = []
    mixed_list = [1, 'abc', True, 2.34, None] # 거의 안씀
    nested_list = [['a', 'b', 'c'], [1, 2, 3]] # 중첩 가능
    ```
    
    ```python
    # 문자열 해체 가능 => 리스트로 반환
    xxx = list('hello') # ['h', 'e', 'l', 'l', 'o']
    
    # 튜플도 리스트 함수로 변환 가
    xxx2 = list((10,20,30)) # [10, 20, 30]
    ```
    
    ```python
    int_list = [1, 2, 3, 4]
    print(int_list*2) # 반복출력
    # [1, 2, 3, 4, 1, 2, 3, 4]
    ```
    
- **리스트 함수 확인**
    
    ```python
    print(dir(list))
    '''
    ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 
    'pop', 'remove', 'reverse', 'sort']
    '''
    ```
    
- **리스트 추가, 삽입, 병합, 삭제**
    1. **리스트 추가(append)**
        
        ```python
        #추가 : 리스트 가장 마지막에 추가된다.
        m = [1,2,3]
        m.append(10)
        m.append([9,8])
        m.append((100,200)) # 튜플도 추가 가능
        print("1. append:",m) #[1, 2, 3, 10, [9, 8], (100, 200)]
        ```
        
    2. **리스트 삽입(insert)**
        
        ```python
        m = [1,2,3]
        m.insert(0,100) # 위치 지정하여 삽입 => 0자리에 100 삽입
        m.insert(0,[4,5,6]) # => 0자리에 리스트 삽입
        print("2. insert:",m) # [[4, 5, 6], 100, 1, 2, 3, 10, [9, 8], (100, 200)]
        ```
        
    3. **리스트 병합(extend 또는 +)**
        
        ```python
        x = [1,2,3]
        x.extend([10])
        x.extend([9,8]) # 리스트와 리스트가 병합되면 값이 리스트 안으로 들어감. (append와 다름)
        x.extend("XYZ") # 문자열 해체되어 리스트 안으로 들어
        # x.extend(100) -> 집합형이 아닌 일반자료형 때문에 병합 불가
        x.extend((7,))  # tuple, tuple도 리스트 안의 값으로 들어감.
        print("3. extend:",x) # [1, 2, 3, 10, 9, 8, 'X', 'Y', 'Z', 7]
        ```
        
        <aside>
        💡 # 병합은 기본적으로 집합형과 집합형을 사용한다.
        # 병합할 대상이 같은 형태여야 함. (집합형과 일반자료형은 병합 불가)
        
        </aside>
        
    4. **리스트 삭제(pop, remove, clear)**
        
        ```python
        kk4 = [1,2,3,4]
        kk4.pop() # pop(-1) 과 동일, 마지막 값이 삭제됨
        kk4.pop(0) # 0자리 값이 삭제됨
        print("9. pop 함수(위치)",kk4) # [2,3]
        ```
        
        ```python
        kk4 = [1,2,3,4]
        kk4.remove(2)  # 값에 의한 삭제
        print("10. remove(값): ", kk4) # [1,3,4]
        ```
        
        ```python
        kk4.clear() # 리스트 전체 삭제
        print("12. clear: " , kk4)
        ```
        
- **리스트 주요 함수**
    
    ```python
    print("4. 리스트 길이:" , len([1,2,3,4])) # 4
    print("5. 포함 갯수:" , [10,2,3,2,9,2].count(2)) # 2의 개수 3
    x3 = [100,200,300]
    print("6. 특정 위치:" , x3.index(200)) # 1
    print("7. 포함 여부1:" , 9 in [9,8,7]) # True
    print("7. 포함 여부2:" , 6 in [9,8,7]) # False
    ```
    
    ```python
    x = [1,2,3]
    x.reverse()
    print("8. 거꾸로(자신이 변경):" , x)  # [3, 2, 1]
    
    y = reversed(x)  # 뒤집힌 새로운 객체 반환
    print("8. 거꾸로(새로운 객체반환):", y, list(y))  
    # y => <list_reverseiterator object at 0x0000029954C4DC10>
    # list(y) => [1, 2, 3]
    ```
    
    <aside>
    💡 x.reverse와 reverse(x)의 차이 주
    
    </aside>
    
    ```python
    # sorted() : 원본은 그대로 유지되고 복사본 생성하여 반환
    #list.sort() : 자기 자신(in-place)을 정렬
    xxx = [88,2,5,3,9,7,10]
    xxx.sort()
    print("13. 오름차순 정렬:",  xxx) # [2, 3, 5, 7, 9, 10, 88]
    xxx.sort(reverse=True)       #역순으로 정렬 [88, 10, 9, 7, 5, 3, 2]
    print("13. 내림차순 정렬:",  xxx) # 원본은 그대
    ```
    
    ```python
    #문자열이 저장된 리스트 정렬
    # 제일 앞에 있는 숫자 기준으로만 정렬 됨.
    yyy = ['123', '9999', '43']
    yyy.sort()
    print("14. 기본 문자열 정렬:",  yyy) # ['123', '43', '9999']
    ```
    
    ```python
    # 리스트 안에 있는 문자열의 길이에 따라 정렬
    # key = 함수명
    zz = ['홍길동','김', '박혁거세']
    zz.sort(key=len)
    zz.sort(key=len, reverse=True)
    print("14. 길이에 따라서  정렬:",  zz)  # ['김', '홍길동', '박혁거세']
    ```
    
- **리스트 인덱싱 & 슬라이싱**
    1. **인덱싱**
        1. **1차원 리스트**
            
            ```python
            arr = [1,2,3,4,5,6,7,8,9,10]
            print("맨 마지막: ", arr[-1])     # 10
            print("맨 마지막에서 두번째 : ", arr[-2])     # 9
            
            print("original: ", arr)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            print("all: ", arr[:])    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            print("reverse: ", arr[::-1])  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
            print("1 부터 끝까지: ", arr[1:])  # [2, 3, 4, 5, 6, 7, 8, 9, 10]
            print("0 부터 5까지: ", arr[:6])   # [1, 2, 3, 4, 5, 6]
            print("2 부터 5까지: ", arr[2:6])  # [3, 4, 5, 6]
            ```
            
        2. **2차원 리스트**
            
            ```python
            arr = [[1,2,3,4,5], [10,20,30,40,50]]
            print("original: ", arr) # [[1, 2, 3, 4, 5], [10, 20, 30, 40, 50]]
            print("all: ", arr[:]) # [[1, 2, 3, 4, 5], [10, 20, 30, 40, 50]]
            print("arr[0]: ", arr[0]) # [1, 2, 3, 4, 5]
            print("arr[1]: ", arr[1]) # [10, 20, 30, 40, 50]
            print("arr[0][:3] ", arr[0][:3] ) # [1, 2, 3]
            ```
            
            ```python
            y = arr[1][-1]
            print(y) # 50 => int로 반환
            ```
            
    2. **슬라이싱**
        
        > 깊은 복사 : 실제값 복사 ⇒ 슬라이싱 [ : ], list.copy( ), list( )
        > 
        > 
        > 얕은 복사 : 주소값 복사 ⇒ n=m
        > 
        
        **a. 얕은 복사 : 주소값 복사, 원본 변경 시 복사본도 영향을 받는다.**
        
        ```python
        n = [1,2,3]
        m=n
        print(n, id(n)) # [1, 2, 3] 3084215230592
        print(m, id(m)) # [1, 2, 3] 3084215230592
        n[0]=100 # 원본 수정
        print(n, m) # [100, 2, 3] [100, 2, 3] => 원본, 복사본 함께 수정됨.
        ```
        
        **b. 깊은 복사 : 실제값 복사, 원본 변경 시 복사본에는 영향주지 않는다.**
        
        ```python
        n = [1,2,3]
        
        # m=n[:] # 슬라이싱
        m=list.copy(n) # list.copy()
        # m=list(n) # list()
        print(n, id(n)) # [1, 2, 3] 1568242331520
        print(m, id(m)) # [1, 2, 3] 1568241909888 => 주소값이 다르다.
        n[0]=100 # 원본 변경
        print(n, m) # [100, 2, 3] [1, 2, 3] => 원본 변경해도 영향받지 않는다.
        ```
        

### 튜플(tuple)

- **개요**
    - 소괄호 (( )) 사용하여 서로 다른 데이터 저장 가능
    - 순서가 있고 중복 허용, 리스트와 유사
    - 리스트와 차이점은 데이터 변경 불가능한 immutable한 특징
    - 따라서 자료 변경을 위해 사용할 만한 메서드를 지원하지 않는다.
        
        (append, insert, remove, pop, sort 함수 지원 안됨)
        
- **튜플 생성**
    
    ```python
    xx = (10,20,30,43)
    xx2 = tuple([9,8,7,7,6,8,9])
    xx3 = (100,)  # 값 하나 가진 튜플 생성
    print(xx, xx2) # (10, 20, 30, 43) (9, 8, 7, 7, 6, 8, 9)
    print(tuple("hello")) # ('h', 'e', 'l', 'l', 'o')
    ```
    
- **튜플 함수 확인**
    
    ```python
    print(dir(tuple))
    '''
    ['count', 'index']
    '''
    ```
    
- **튜플 주요 함수**
    
    ```python
    print("튜플 길이:" , len((1,2,3,4))) # 4
    print("포함 갯수:" , (10,2,3,2,9,2).count(2)) # 3
    x3 = (100,200,300)
    print("포함 갯수:" , x3.count(100)) # 1
    print("특정 위치:" , x3.index(200)) # 1
    print("포함 여부1:" , 9 in (9,8,7)) # True
    print("포함 여부2:" , 6 in (9,8,7)) # False
    ```
    
- **튜플 인덱싱 & 슬라이싱**
    
    ```python
    kk = (1,2,3,4,5)
    print("특정 값:" , kk[0]) # 1
    print("slice:" , kk[0:3]) # (1, 2, 3)
    print("slice:" , kk[:6]) # (1, 2, 3, 4, 5)
    print("slice:" , kk[3:]) # (4, 5)
    print("slice:" , kk[:]) # (1, 2, 3, 4, 5)
    ```
    
    ```python
    kk3 =(1,2,3,(9,8,7))
    print("중첩 :" , kk3) # (1,2,3,(9,8,7))
    print("특정 값 출력1:" , kk3[3][0]) # 9
    print("특정 값 출력2:" , kk3[3][2:]) # (7, )
    print("특정 값 출력3:" , kk3[3][:2]) # (9, 8)
    ```
    

### 셋(set)

- **개요**
    - 중괄호 ({ }) 사용하여 서로 다른 데이터 저장 가능
    - 순서가 없고 중복 불가
    - 저장되는 값은 반드시 immutable만 가능하다. ⇒ 리스트 저장 불가
    - set 함수 지원( union(), intersection(), difference())
- **셋 생성**
    
    ```python
    m = {1,2,3,1}
    m2 = set() # set()
    print(m, m2) # {1,2,3,1}, set()
    print(set("hello")) # {'e', 'o', 'l', 'h'} => 순서 없음
    ```
    
    ```python
    m3 = {10,20,"홍길동",(100,200)}
    print(m3) # {10, 20, '홍길동', (100, 200)}
    #m4 = {10,20,"홍길동",[1,2]}  # mutable 데이터인 리스트 저장 불가
    # print(m4)  # 에러
    #print(m*2) # error , 반복출력 불가
    ```
    
- **셋 함수 확인**
    
    ```python
    print(dir(set))
    '''
    ['add', 'clear', 'copy', 'difference', 'difference_update',
    'discard', 'intersection', 'intersection_update',
    'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove',
    'symmetric_difference', 'symmetric_difference_update',
    'union', 'update']
    '''
    ```
    
- **셋 추가, 병합, 삭제**
    1. **셋 추가 (add)**
        
        ```python
        m = {1,2,3}
        m.add(10)
        m.add("홍길동")
        m.add((9,8))
        print("add:",m) # {1, 2, 3, 10, (9, 8), '홍길동'}
        ```
        
    2. **셋 병합 (update)**
        
        ```python
        m2 = {1,2}
        m2.update({3,4})
        print("update1_set:" , m2) # {1, 2, 3, 4}
        m2.update([5,6,7]) # list와도 병합 가능 (추가는 불가)
        print("update2_list:" , m2) # {1, 2, 3, 4, 5, 6, 7}
        m2.update((9,10))
        print("update3_tuple:" , m2) # {1, 2, 3, 4, 5, 6, 7, 9, 10}
        ```
        
        <aside>
        💡 집합형에 저장된 데이터를 꺼내서 처리하기 때문에 리스트와도 병합이 가능하다.
        
        </aside>
        
    3. **셋 삭제 (discard, remove, pop)**
        
        ```python
        m2 = {1,2,3,4}
        m2.discard(4)  # 값 4를 삭제해라. If the element is not a member, do nothing.
        print(m2) # {1,2,3}
        m2.remove(3)  # 값 3을 삭제해라. If the element is not a member, raise a KeyError.
        print(m2) # {1,2}
        m2.pop()      # 임의의 값을 삭제해라.(순서가 없으므로) Raises KeyError if the set is empty.
        # 리스트에서의 pop 함수에서는 인덱스 지정하여 삭제하였음.
        print(">>>>>>>>>>>>>>>>>", m2)
        ```
        
        <aside>
        💡 리스트에서는 pop함수를 이용하여 마지막 값을 삭제하였지만, 셋은 순서가 없기 때문에 임의의 값이 삭제된다.
        
        </aside>
        
- **셋 주요 함수**
    
    ```python
    print("set 길이:" , len({1,2,3,4,5})) # 5
    x3 = {100,200,300}
    print("포함 여부1:" , 9 in {9,8,7}) # True
    print("포함 여부2:" , 6 in {9,8,7}) # False
    
    x3.clear() 
    print(x3) # set( )
    print()
    ```
    
- **연산자 및 함수**
    1. **union(합집합)**
        - 중복값을 삭제하고 셋을 병합한다.
        
        ```python
        a = {1,2,3,1}
        b = {3,4}
        print("union(합집합):" , a.union(b)) # {1, 2, 3, 4}
        # 중복값 1 하나가 삭제되었으며 3, 4가 추가되었다.
        ```
        
    
    1. **intersection(교집합)**
        - 교집합 중에서도 중복값이 있다면 삭제 후 반환된다.
        
        ```python
        a = {1,2,3,1}
        b = {3,4}
        print("intersection(교집합):" , a.intersection(b)) # {3}
        ```
        
    2. **difference(차집합)**
        - 차집합 중 중복값이 있다면 삭제 후 반환된다.
        
        ```python
        a = {1,2,3,1}
        b = {3,4}
        print("difference: 차집합" , a.difference(b)) # {1, 2}
        ```
        
    
    1. **symmetric_difference(대칭 차집합)**
        - 대칭 차집합 중 중복값이 있다면 삭제 후 반환된다.
        
        ```python
        a = {1,2,3,1}
        b = {3,4}
        print("exclusive difference: 대칭 차집합" ,
              a.symmetric_difference(b)) # {1, 2, 4}
        ```
        
    
    <aside>
    💡 set은 중복값을 삭제할 때 주로 사용함.
    ex) union 실행 시 중복값 삭제 됨. a.union( )
    
    </aside>
    

### 딕트(dict)

- **개요**
    - 중괄호({ }) 내에 {’key’:’value’} 쌍으로 데이터를 관리
    - 순서가 없기 때문에 전체 자료 출력 시 순서 없이 불규칙하게 출력 됨
    - key는 immutable 값이고 value는 mutable 값이다.
- **딕트 생성**
    
    ```python
    m0 = {} # 비어있는 중괄호 = dict
    m1 = dict()
    m2 = {'name':'홍길동1','age':20} # 일반적인 방법
    m3 = dict(name='홍길동2', age=20) # 기억
    print(m0, m1, m2, m3)
    ```
    
- **딕트 함수 확인**
    
    ```python
    print(dir(dict))
    '''
    ['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 
    'pop', 'popitem', 'setdefault', 'update', 'values']
    '''
    ```
    
- **딕트 추가, 변경, 삭제**
    1. **딕트 추가**
        
        ```python
        coffee = {'espresso':'에스프레소', 'latte':'라떼'}
        print(coffee)
        coffee['lungo'] = '룽고'    #요소를 추가
        print("요소추가:", coffee) # {'espresso': '에스프레소', 'latte': '라떼', 'lungo': '룽고'}
        ```
        
    2. **딕트 변경**
        
        ```python
        coffee['latte'] = '라떼2'
        print("요소변경:",coffee)
        ```
        
    3. **딕트 삭제 (del, pop)**
        
        ```python
        del coffee['lungo']        #요소를 삭제
        print("요소삭제1:",coffee)
        
        coffee.pop('latte')        #요소를 삭제
        print("요소삭제2:",coffee)
        
        coffee.clear()            #요소 전체 삭제
        print("요소전체삭제:",coffee)
        ```
        
    4. **딕트 병합/한꺼번에 수정 (update)**
        
        ```python
        x = {'name':'유관순','age':20}
        y = {'address':'seoul'}
        
        x.update(y)
        print("병합1:",x) # {'name': '유관순', 'age': 20, 'address': 'seoul'}
        
        x.update({'name':'aaa2','age':202})
        print("한꺼번에 병합2:",x) # {'name': 'aaa2', 'age': 202, 'address': 'seoul'}
        ```
        
    5. **딕트 정보 얻기**
        1. **길이**
        
        ```python
        coffee = {'espresso': '에스프레소', 'latte': '라떼'}
        print(coffee)
        print(len(coffee))  # 길이 출력, 2
        ```
        
        **b. value 정보 얻기 (key 값을 알고있는 경우)**
        
        ```python
        print(coffee['espresso'])
        # 키를 이용해 값을 조회,  없으면 에러
        # 에스프레소
        
        print(coffee.get('latte'))  # key로 value 얻기
        # 라떼
        
        print(coffee.get('latt2e', 'Not a Coffee'))  
        # 없으면 기본값 출력 , 기본값 지정안하면 None 출력
        # Not a Coffee
        ```
        
        **c. value 정보 얻기 (key 값이 너무 많거나 모르는 경우)**
        
        ```python
        print(coffee.keys(), list(coffee.keys()))
        # key 목록 출력
        # dict_keys(['espresso', 'latte']) ['espresso', 'latte']
        
        keys = list(coffee.keys())
        print(coffee[keys[0]] , coffee['espresso'] , coffee.get(keys[0]))
        ```
        
        **d. value 값만 조회**
        
        ```python
        print(coffee.values(), list(coffee.values()))
        # value 목록 출력
        # dict_values(['에스프레소', '라떼']) ['에스프레소', '라떼']
        ```
        
        **e. key, value 같이 조회**
        
        ```python
        print(coffee.items(), list(coffee.items()))
        # key, value 출력
        # dict_items([('espresso', '에스프레소'), ('latte', '라떼')])
        ```
        

### 데이터 형 변환

> 집합형 데이터의 형변환

str(값) : str로 변경
> 
> 
> list(값) : list로 변경
> tuple(값) : tuple로 변경
> set(값) : set로 변경
> dict(값) : dict로 변경
> 

- **list → tuple, set**
    
    ```python
    a = [10,20,30,30]
    a2 = tuple(a)
    a3 = set(a)
    print(a) # [10, 20, 30, 30]
    print(a2) # (10, 20, 30, 30)
    print(a3) # {10, 20, 30} # 셋의 주요한 용도 : 중복 제거
    ```
    
- **set → list, tuple**
    
    ```python
    a = {10,20,30,30}
    a2 = list(a)
    a3 = tuple(a)
    print(a) # {10, 20, 30}
    print(a2) # [10, 20, 30]
    print(a3) # (10, 20, 30)
    ```
    
    <aside>
    💡 중복값 있던 set는 list와 tuple 변환 시에도 중복값 사라짐
    
    </aside>
    
- **tuple → list, set**
    
    ```python
    a = (10,20,30,30)
    a2 = list(a)
    a3 = set(a)
    print(a) # (10, 20, 30, 30)
    print(a2) # [10, 20, 30, 30]
    print(a3) # {10, 20, 30}
    ```
    
- **dict → list, set, tuple (key만 추출되어 저장 됨)**
    
    ```python
    a = {"name":"홍길동","age":100}
    a2 = list(a)
    a3 = set(a)
    a4 = tuple(a)
    print(a)
    print(a2) # ['name', 'age']
    print(a3) # {'name', 'age'}
    print(a4) # ('name', 'age')
    ```
    
- **str → list, tuple, set**
    
    ```python
    print( list("홍길동길")) # ['홍', '길', '동', '길']
    print( tuple("홍길동길")) # ('홍', '길', '동', '길')
    print( set("홍길동길")) # {'길', '홍', '동'}
    ```
    

## 제어문

### if 문

- **단일 if 문**
    
    ```python
    print("1")
    if 3==3:
        print("2")
        print("3")
        print("4")
    print("5")
    ```
    
    ```python
    if 3 == 3: print("True")
    ```
    
    <aside>
    💡 조건식에는 True / False, 비교연산자, 논리연산자, 멤버쉽 연산자, True/False가 아닌 임의의 값으로 사용가능 (“ “, None, {}, [] 등)
    
    </aside>
    
- **if ~ else 문**
    
    ```python
    n = int(input("정수입력"))
    if n%2==0:
        print("짝수")
    else:
        print("홀수")
    print("end")
    ```
    
    ```python
    # in 리스트 활용
    
    pocket = ['paper','card','tel']
    if 'tel' in pocket:
        print("tel")
    else:
        print("None")
    ```
    
- **다중 if 문**
    1. **다중 if ~ else 문 (elif)**
        
        ```python
        n = int(input("점수입력"))
        if n>90:
            print("A 학점")
        elif n>80:
                print("B 학점")
        elif n>70:
                print("C 학점")
        else:
            print("F 학점")
        print("end")
        ```
        
    
    1. **중첩 가능**
        
        ```python
        num = 85
        if num >= 90:
            print("우수")
        else:
            if num >= 70:
                print("보통")
            else:
                print("저조")
        ```
        
- **3항 연산자**
    
    > 변수 = 참값 if 조건식 else 거짓값
    > 
    
    1. **3항 연산자**
        
        ```python
        jumsu = int(input('점수-->'))
        
        res = '합격' if jumsu >= 60 else '불합격'
        print(res)
        
        res = [2,3,4] if jumsu >= 60 else [-1,2] 
        # 참, 거짓값으로 집합형도 가능
        ```
        
    
    1. **중첩 3항 연산자**
        
        ```python
        n = 4
        m = "Hello" if n > 10 else "Goodbye" if n > 5 else "Good day"
        print(m) # Good day
        ```
        
    

### for 문

> 반복문

for  변수 in 집합형:
       문장

집합형 : 리스트, 문자열, range(n) ⇒ 개수만큼 반복된다.
> 

- **for 문 생성**
    
    ```python
    for n in [1,2,3]:
        print("hello", n) # hello 1 hello 2 hello 3
    
    for n in "abcde" :
        print("world", n) # world a world b ... world e
    
    for _ in "abcde" :
        print("world") # world world world world world
    
    for _ in range(3) : # 0~2 총 세번
        print("happy") # happy happy happy
    ```
    
    <aside>
    💡 일반적으로는 range(n)을 입력하여 n번 반복하게 함.
    
    </aside>
    
- **특정문장을 반복 처리하는 기본 코드**
    
    ```python
    for _ in range(3):
        print("happy")
    # happy happy ****happy
    ```
    
- **집합형에 저장된 데이터 열기**
    
    ```python
    for n in [1,2,3]:
        print(n) # 1 2 3
    
    for n in (10,20,30):
        print(n, end=" ") # 10 20 30
    
    for n in {100,200,300,300}:
        print(n, end=" ") # 100 200 300 300
    
    for s in "abcde":
        print(s) #  a b c d e
    ```
    
    - **반복할 때 idx 값 얻기 (enumerate)**
        
        ```python
        for idx, n in enumerate([10,20,30]):
            print(idx, n)
        '''
          0 10
        	1 20
        	2 30
        '''
        
        for idx, s in enumerate("abcde"):
            print(idx, s)
        '''
        0 a
        1 b
        ...
        4 e
        '''
        ```
        
        ```python
        # idx 값을 1부터 시작하고 싶을 때
        
        for idx, n in enumerate([10,20,30], 1):
            print(idx, n)
        '''
        1 10
        2 20
        3 30
        '''
        ```
        
- **dict 반복**
    1. **key와 value 값 모두 가져오기**
        
        ```python
        soft = {'java':'웹용', 'python':'만능언어', 'oracle':'db처리'}
        for key, value in soft.items():
            print(key + ':  ' + value)
        '''
        java: 웹용
        python: 만능언어
        oracle: db처리
        '''
        ```
        
    2. **key 값만 가져오기**
        
        ```python
        soft = {'java':'웹용', 'python':'만능언어', 'oracle':'db처리'}
        for key in soft.keys():
            print(key)
        '''
        java
        python
        oracle
        '''
        ```
        
    3. **value 값만 가져오기**
        
        ```python
        soft = {'java':'웹용', 'python':'만능언어', 'oracle':'db처리'}
        for value in soft.values():
            print(value, end=" ")
        '''
        웹용 만능언어 db처리
        '''
        ```
        

### range 함수

> range(stop) → range object
range(start, stop, step) → range object
⇒ start 포함, stop 미포함 (슬라이싱과 동일)
⇒ 기본값은 0 부터
> 

```python
print(list(range(10))) # 0부터 9까지
print(list(range(1,5))) # 1부터 4까지
print(list(range(1,10,2))) # 1부터 9까지 2만큼 step
```

### break, continue

> break : 반복문 빠져나올 때
continue : 특정 회차에서 일부분의 문장을 skip할 때
> 

- **break**
    
    ```python
    # break, continue, else 문
    datas = [1, 2, 3, 4, 5]
    print("-------------------------------------")
    
    for i in datas:
        if i == 4: break
        print(i, end=' ') # 1 2 3
    ```
    
    <aside>
    💡 i가 4일 경우 반복문을 종료한다.
    ⇒ 1, 2, 3 값만 출력됨.
    
    </aside>
    
- continue
    
    ```python
    datas = [1, 2, 3, 4, 5]
    print("-------------------------------------")
    
    for i in datas:
        if i == 3: continue
        print(i, end=' ') # 1 2 4 5
    ```
    
    <aside>
    💡 i가 3일 경우는 문장을 skip한다.
    ⇒ 3을 제외한 나머지 값들만 출력됨.
    
    </aside>
    
- **반복문 + else**
    
    ```python
    datas = [1, 2, 3, 4, 5]
    print("-------------------------------------")
    
    for i in datas:
        if i == 6: continue
        if i == 7: break
        print(i, end=' ')
    else:   # 정상적인 반복문 종료시 실행됨
        print("정상종료")
    print("end")
    ```
    
    <aside>
    💡 continue와 break의 조건문이 모두 해당하지 않으므로
    문장 리스트 요소 모두 적용되어 출력된다.
    
    </aside>
    

### list conprehension

> list conprehension
⇒ list로 부터 가공하여 새로운 list를 반환하는 기능
> 

- **변수 = [ 표현식 for 변수 in 집합형 ]**
    
    ```python
    x = [ n+1 for n in [1, 2, 3] ]
    aaa = [ n>2 for n in [1, 2, 3] ]
    x = [ n.upper() for n in ["A","b","C"] ]
    print(x) # [ 2, 3, 4 ]
    print(aaa) # [False, False, True]
    print(x) # [ "A", "B", "C" ]
    ```
    
    ```python
    ## list conprehension 없이 만들 떄
    m = ["A","b","C"]
    k = []
    for m2 in m:
        m3 = m2.upper()
        k.append(m3)
    print(k)
    ```
    
- **변수 = [ 표현식 for 변수 in 집합형 if 조건식 ]**
    
    ```python
    # 짝수만 출력
    x = [n for n in range(1,11) if n%2==0]
    print(x)
    ```
    
- **변수 = [ 참 if 조건식 else 거짓 표현 for 변수 in 집합형 ]**
    
    ```python
    # 짝수면 0으로 홀수면 1로 반환
    x = [0 if n%2==0 else 1 for n in range(1,11)]
    print(x)
    ```
    

### dict conprehension

> dict conprehension
⇒ dict로부터 가공하여 새로운 dict를 반환하는 기능
> 

- **변수 = { k : v for k, v dict.item( ) }**
    
    ```python
    x = {"대한민국":"서울", "미국":"워싱턴","중국":"베이징"}
    
    x2 = { v:k for k,v in x.items()}
    x2 = { k:len(v) for k,v in x.items()}
    print(x2)
    ```
    
- **변수 = { k : v for k, v dict.item( ) if 조건 }**
    
    ```python
    # 국가명이 2글자인 경우에만 출력
    x = {"대한민국":"서울", "미국":"워싱턴","중국":"베이징"}
    x2 = { k:v for k,v in x.items() if len(k)==2}
    print(x2)
    ```
    
- **변수 = { 참 표현식 if 조건 else 거짓 표현식 for k, v 변수.item( ) }**
    
    ```python
    # 국가명 중에서 대한민국은 korea로 표시
    x = {"대한민국":"서울", "미국":"워싱턴","중국":"베이징"}
    x2 = { "korea" if k=="대한민국" else k for k,v in x.items() }
    print(x2)
    ```
    

### generator comprehension

- 문법 : 변수 = ( 표현식 for 변수 in 집합형 )
- 한번에 실행되지 않고 단계적으로 실행 됨.
    
    → next( ) 함수 이용해서 단계적으로 값을 얻는다.
    

```python
list_x = [ n for n in [1, 2, 3] ]
generator_x = ( n for n in [1, 2, 3] )

print("list comprehension:", list_x) # [1, 2, 3]
print("generator comprehension:", generator_x) 
# <generator object <genexpr> at 0x000001CB28CD7B30>
```

```python
# next() 함수로 호출할 때마다 단계적으로 출력 됨.
print(next(generator_x)) #1
print(next(generator_x)) #2
print(next(generator_x)) #3
```

```python
# 위의 단계적인 next() 함수 한번에 표현
generator_x = (n for n in [1,2,3])
print(list(generator_x))
```

<aside>
💡 next 후 다시 집합형 데이터 가져와서 작업해야 한다.
그렇지 않으면, 집합형 데이터를 모두 소진하여 작업하여도 
비어있는 집합형이 출력된다.

</aside>

## while 문

### 기본 while 문

> 문법 :

초기값
while 조건식 :
          문장
          증감식
> 

```python
n=1
while n<6:
    print("hello")
    n+=1
print("End")
```

### while문 무한루프

> 문법 :

while True :
          문장1
          문장2
          if 조건식 : break
> 

```python
while True:
    name = input("이름 입력하시오. 중지하려면 Q 입력")
    print("입력한 이름:", name)
    if name == "Q" : break

print("종료")
```

## 함수

### 함수 개요 및 특징

- **문법**
    
    def 함수명( 파라미터, … ) :
    
    실행코드
    
    return 반환값
    
- **특징**
    - 반드시 호출해야 수행되고 수행 후에는 호출된 곳으로 돌아온다.
    - 호출시 인자값 전달이 가능하고 반환시 리턴값을 받을 수 있다.
    - 파이썬 함수는 일급객체 특성을 갖는다.
    - 함수 수행을 끝마칠 목적으로 return 키워드를 사용할 수 있다.
    - 함수 호출시 인자 개수는 일치시키거나 default 파라미터 및 packing/unpacking 을 사용할 수 있다.

### 함수 유형

- **파라미터 없고 리턴값도 없음**
    
    ```python
    def fun():
        print("fun") # 여기서는 fun() 함수가 실행되지 않는다. 반드시 함수를 호출해야 함.
    
    fun() # 함수를 호출해야 실행 됨.
    print("end")
    ```
    
- **파라미터 있고 리턴값 없음**
    
    ```python
    def fun2(n, n2):
        print("fun", n, n2)
    
    fun2(10, "홍길동") # fun 10 홍길동
    fun2([1,2,3],{"a":20}) # fum [1,2,3] {"a":20}
    ```
    
    <aside>
    💡 함수를 호출할 때에는 파라미터와 인자 개수가 일치해야 한다.
    
    </aside>
    
- **파라미터 없고 리턴값 있음**
    
    ```python
    def fun3() :
        print("fun3")
        return 100
    
    result=fun3() # 리턴값을 저장해야하기 때문에 앞에 변수 필요
    print(result) 
    '''
    fun3
    100
    '''
    ```
    
    <aside>
    💡 리턴값을 저장해야하기 때문에 함수를 변수에 지정해야 한다.
    
    </aside>
    
    ```python
    def fun4() :
        print("fun4")
        return 100, 200 # 튜플 한개로 반환 됨.
    
    result=fun4() # 리턴값을 저장해야하기 때문에 앞에 변수 필요
    print(result)
    '''
    fun4
    (100, 200)
    '''
    ```
    
    <aside>
    💡 리턴값이 여러개일 경우 튜플 하나로 묶여서 반환 됨.
    
    </aside>
    
- **파라미터 있고 리턴값 있음**
    
    ```python
    def fun5(n, n2) :
        print("fun5")
        return n+n2
    
    result=fun5(10,20)
    print(result)
    '''
    fun5
    30
    '''
    ```
    

### default 파라미터

> def 함수명( n = 기본값, n2 = 기본값) :
      pass
> 

```python
def fun(n=10, n2=20):
    print(n, n2)

fun()
fun(100) # n은 100으로, n2는 파라미터에서 지정한 값 20으로 출력됨.
fun(100, 200) # 인자 두개를 지정했을 경우 파라미터에서 지정한 default 값 무시하고 출력 됨.
```

### packing 파라미터

> def 함수형( n, *n ) :
      pass

*n은 튜플로 출력됨.
> 

```python
# 변수 선언
n, *n2 = 1,2,3,4,5
print(n, n2) # 1 [2,3,4,5]

def fun(n, *n2):
    print(n, n2)

fun(10,20) # 10 (20, )
fun(10,20,30) # 10 (20,30)
fun(10) # 10 ()
```

```python
def fun2(n, x, *n2):
    print(n, x, n2)

fun2(10,20,30,40) # 10 20 (30,40)
```

```python
def fun3(n=10, x=20, *n2):
    print(n, x, n2)

fun3() # 인자 값 없으면 default 값으로 출력 # 10 20 ()
fun3(1,2,3,4,5) # 인자 값 입력해주면 입력한 인자 값으로 출력
# 1 2 (3,4,5)
```

### named 파라미터

> def fun( age, username ) :
      pass

fun( 10, ‘홍길동’ ) # 일반적인 방법
fun( age=10, username=’홍길동’ ) # 변수명 명시하여 인자값 지정
> 

1. **기본**
    
    ```python
    def fun(age, username) :
        print(age, username)
    
    fun(10, "홍길동") # 10 홍길동
    fun(age=10, username="홍길동") # 10 홍길동
    fun(username="홍길동", age=10) # 변수명 명시하면 인자 순서 바뀌어도 됨.
    # 10 홍길동
    ```
    
    <aside>
    💡 파라미터에 변수명 명시했어도 출력할 때에는 인자값을 우선시 함.
    
    </aside>
    
2. ****n**
    
    ```python
    def fun2(**n): # dict로 출력됨
        print(n)
    ```
    
    ```python
    fun2(age=10) # {'age': 10}
    fun2(age=10, username='홍길동')
    # {'age': 10, 'username': '홍길동'}
    fun2(age=10, username='홍길동',address="서울")
    # {'age': 10, 'username': '홍길동', 'address': '서울'}
    ```
    
    <aside>
    💡 인자값이 몇개든 dict로 출력됨.
    
    </aside>
    

1. **혼합**
    
    ```python
    def fun3(n, n2, *n3, **n4): # 순서 중요
        print(n,n2,n3,n4)
    
    fun3(10,20,30, age=10, username='홍길동')
    # 10 20 (30, ) {age:10, 'username':'홍길동'}
    fun3(10,20,30,40,50, age=10, username='홍길동')
    # 10 20 (30,40,50) {age:10, 'username':'홍길동'}
    ```
    

### 변수 scope

> python의 변수는 함수 scope를 따른다.
⇒ 함수 안에서 선언된 변수는 함수 안에서만 사용 가능하다.
> 

```python
n=10 # 함수 밖에서 선언된 함수 = 전역 변수 ( global variable)

def fun():
    n2=20 # 함수 안에서 선언된 함수 = 지역 변수( Local variable )
    print("n:", n)
    print("n2:", n2)

fun() # 함수 안, 밖에서 선언된 함수 모두 사용 가능하다.

print("n:", n)
print("n2:", n2) # 함수 안에서 선언된 함수는 함수 밖에서 사용 불가
```

### 일급객체

- **특징**
    - 함수를 변수에 저장할 수 있다.
    - 함수를 호출할 때 인자로 전달할 수 있다.
    - 함수를 함수의 리턴값으로 사용할 수 있다.
    
- **함수는 데이터이기 때문에 변수에 저장 가능하다.**
    
    ```python
    def fun() :
        print("fun")
    
    print(fun) # () 없이 함수명만 불렀을 경우-> 주소값이 출력됨
    n=fun # 함수 객체를 참조하는 변수(n) 생성 (함수를 변수에 저장)
    n() # n 실행 -> fun()이 실행 됨
    ```
    
    <aside>
    💡 함수 객체를 참조하는 변수 n을 생성하여 n을 실행하면 함수가 실행 됨.
    
    </aside>
    
- **함수는 데이터이기 때문에 함수 호출시 인자값으로 사용 가능하다.**
    
    ```python
    def x():
        print("x")
    
    def y(n):
        n()
    
    y(x) # y를 호출했으나 실제 반응은 x함수이다. => 트리거
    ```
    
    <aside>
    💡 콜백함수(callback) 구현이 가능하다.
    
    콜백함수는 사용자가 호출한 함수가 아니고 특정 시점에 시스템이 호출하는 함수를 의미한다.
    
    콜백함수를 구현하는 방법은 직접 함수명을 알려줘야 한다.
    
    </aside>
    
- **함수는 데이터이기 때문에 함수 호출시 리턴값으로 사용 가능하다.**
    
    ```python
    def k():
        print("k")
    
    def k2() :
        return k
    
    result = k2()
    result()
    ```
    
    <aside>
    💡 대신 함수를 변수에 지정을 해야 리턴값으로 사용 가능하다.
    
    </aside>
    

### lambda 표현식

- **특징**
    - def 함수명 ( ) 문법을 이용한 함수 작성의 또 다른 표현식
    - 반드시 단일 문장인 경우에만 lambda 표현식이 가능하다.
    - 익명함수이기 때문에 변수에 저장해서 호출해야 한다. (일급객체)
    
- **파라미터 없고 리턴값 없음**
    1. **일반 함수에서는**
        
        ```python
        def fun():
            print("fun")
        
        fun()
        ```
        
    
    1. **lambda 표현식**
        
        ```python
        fun = lambda : print("lambda fun")
        
        fun()
        ```
        
- **파라미터 있고 리턴값 없음**
    1. **일반 함수에서는**
        
        ```python
        def fun2(n, n2):
        	print("fun", n, n2)
        fun2(n,n2)
        ```
        
    2. **lambda 표현식**
        - 기본
        
        ```python
        fun2 = lambda n, n2 : print("lambda fun2", n, n2)
        fun2(10,20)
        ```
        
        - default 파라미터도 가능
        
        ```python
        fun2 = lambda n=20, n2='홍길동' : print("lambda fun2", n, n2)
        fun2()
        ```
        
        - packing 파라미터도 가능
        
        ```python
        fun2 = lambda n=10, n2=20, *n3 : print("lambda fun2", n, n2, n3)
        fun2(10,20) # lambda fun2 10 20
        fun2() # lambda fun2 10 20
        fun2(10,23,4,4,5,6,5) # lambda fun2 10 23 (4,4,5,6,5)
        ```
        
        ```python
        fun2=lambda n=10,n2=20, *n3, **n4:print("lambda fun2",n, n2, n3, n4)
        fun2(10,20) # lambda fun2 10 20 () {}
        fun2() # lambda fun2 10 20 () {}
        fun2(10,23,4,4,5,6,5, age=20, addr='서울')
        # lambda fun2 10 23 (4,4,5,6,5), {'age':20, 'addr':'서울'}
        ```
        
- **파라미터 없고 리턴값 있음**
    1. **일반 함수에서는**
        
        ```python
        def fun3 :
        	return 100
        
        result = fun3()
        print(result) # 100
        ```
        
    2. **lambda 표현식**
        
        ```python
        fun3=lambda : 100 # 리턴값 = 100
        result = fun3()
        print("lambda fun3", result)
        ```
        
- **파라미터 있고 리턴값 있음**
    1. **일반 함수에서는**
        
        ```python
        def fun4(n, n2):
        	return n+n2
        ```
        
    2. **lambda 표현식**
        
        ```python
        fun4 = lambda n, n2 : n+n2
        result = fun4(10,20)
        print(result)
        ```
        

### generater 함수

- **특징**
    - 함수 내의 문장을 단계적으로 실행 가능
    - yield 키워드 이용하여 generator 함수로 생성
    - next( ) 함수 이용
    
- **일반 함수에서**
    
    ```python
    def fun():
        print("1")
        print("2")
        print("3")
    
    f=fun() # 함수를 변수에 저장
    print(f, type(f)) # 변수에 저장한 함수 호출 => <class 'NoneType'> = 리턴값 없음
    ```
    
- **generator 함수**
    
    ```python
    def fun2():
        print("10")
        yield
        print("20")
        yield
        print("30")
        yield
    
    f2=fun2() # 함수를 변수에 저장
    print(f2, type(f2)) # 문장에 대한 값이 호출되진 않음(next() 필요) & type이 <class 'generator'>로 바뀜
    next(f2, type(f2)) # 10
    next(f2, type(f2)) # 20
    next(f2, type(f2)) # 30
    ```
    

### 내장함수

- **내장함수(built-in) 확인**
    
    ```python
    print(dir(__builtins__))
    '''
    'abs', 'all', 'any', 'ascii', 'bin', 'bool',
    'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod',
    'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir',
    'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format',
    'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id',
    'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list',
    'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open',
    'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round',
    'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super',
    'tuple', 'type', 'vars', 'zip'
    '''
    ```
    
- **주요 내장함수**
    
    ```python
    print("1. 합계:", sum([1,2,3,4]))
    print("2. 평균:", sum([1,2,3,4])/len([1,2,3,4]))
    print("3. 리스트 최대값, 최소값:", max([1,2,3,4]), min([1,2,3,4]))
    print("4. 딕셔너리 최대값", max({10:'aaa',4:'bbb',100:'ccc'})) #100
    print("5. 딕셔너리 최소값", min({10:'aaa',4:'bbb',100:'ccc'})) #4
    print("6. 절대값:", abs(-100))
    print("7. 아스키코드값:", chr(65), chr(97))
    print("7. 아스키코드값:", ord('A'), ord('a'))
    print("8. 몫과 나머지:", divmod(10,3))
    print("9. 반올림:",  round(4.67))  # 소수점 0 자리 반올림, 즉 정수 반올림
    print("10. 반올림:",  round(4.67, 1)) # 소수점 1자리 반올림
    ```
    
- **zip 함수**
    
    ```python
    x=['name',"age", "address"]
    y=["홍길동", 20, "서울"]
    
    print("12. zip:",list(zip(x,y))) 
    #[('name', '홍길동'), ('age', 20), ('address', '서울')]
    
    print("13. zip:",dict(zip(x,y)))
    # {'name': '홍길동', 'age': 20, 'address': '서울'}
    ```
    
- **all, any**
    - 전부 또는 일부가 맞으면 True / False
    
    ```python
    b_list = [True, 1, False]
    print(all(b_list)) # False #iterable data들 중 모두 참이면 참
    print(all([1,1,0])) # False #iterable data들 중 모두 참이면 참
    print(any(b_list)) # True
    ```
    
    ```python
    b_list =[1, 3, 2, 5, 7, 6]
    print("b_list 값이 모두 10 미만인가?")
    
    x = [n < 10 for n in b_list] # list comprehension
    print(x)
    print(all(x),all(n<10 for n in b_list))
    
    print("b_list 값 중 3 미만이 있나?")
    print(any([n<3 for n in b_list]))
    ```
    
- **filter 함수**
    - 내장된 함수에서 반환된 값이 참인 경우에만 반환
    - filter(function or None, iterable) = filter(함수, 집합형)
    
    ```python
    b_list =[1, 3, 2, 5, 7, 6]
    
    def fun(n): # filter에서 fun 사용했기 때문에 값 들어갈 파라미터 필요
        return n%2 == 0
    
    result = filter(fun, b_list) # def 함수에서 반환된 값이 참인 경우(짝수인 경우)에만 반환
    print(list(result))
    
    ## lambda 표현식 이용
    def fun(n): # filter에서 fun 사용했기 때문에 값 들어갈 파라미터 필요
        return n%2 == 0
    
    fun = lambda  n : n%2 == 0
    result = filter(fun, b_list)
    result = filter(lambda  n : n%2 == 0, b_list) # 가장 일반적
    print(list(result))
    ```
    
- **join 함수**
    - 리스트에 있는 문자열들을 구분자와 함께 합쳐준다.
    
    ```python
    xxx = list(result)
    print(xxx) 
    # ['a', 'b', 'd', 'e', 'A', 'b', 'C', 'd', 'e', 'D', 'g', 'd', 'd']
    
    print("".join(xxx))
    # abdeAbCdeDgdd
    ```
    
- **map 함수**
    - 내장된 함수에서 다른 함수적용(가공) 후 반환
    - map(함수, 집합형)
    
    ```python
    xxx = ["Abc","EbAeEG"]
    
    def fun(n):
        return n.upper() # n.uuper() => 내장된 함수
    
    result = map(fun, xxx)
    print(list(result))
    
    #lambda
    result = map(lambda n : n.upper(), xxx)
    result = map(str.upper, xxx) # 문자열에 있는 함수는 앞에 str. 붙여주어야 함.
    print(list(result))
    ```
    

### 내장함수-랜덤함수

- **random.randint(a, b)**
    - a <= N <= b
    
    ```python
    import random # 랜덤함수 사용할 때 필수
    
    n = random.randint(1, 7) 
    # random 안에 있는 randint 함수 실행 / 1 이상 7 이하 중 랜덤값
    print("1. randint:", n)
    ```
    
- **random.random()**
    - 0~1 사이의 랜덤 실수
    
    ```python
    n = random.random()
    print("2. random:", n)
    ```
    
- **random.randrange(a, b)**
    - a <= N < b
    
    ```python
    n = random.randrange(1,7)
    print("3. randrange:", n)
    ```
    
- **random.shuffle(x)**
    - 리스트 요소 섞기
    
    ```python
    x = ['a','b','c']
    random.shuffle(x)
    print("4. shuffle:", x)
    ```
    
- **random.choice(x)**
    - 리스트 요소 중 한개만 랜덤으로 뽑아 반환
    
    ```python
    x = ['a','b','c']
    print("5. choice:", random.choice(x))
    ```
    

## Class

### 개요

- 현실 세계의 객체(object)를 OPP기반으로 표현한 형태이다.
- 객체의 구성요소인 속성과 동작은 변수와 메서드로 표현한다.
- 클래스를 사용하기 위해서는 반드시 객체 생성이 필요하다.
- 클래스의 이름은 반드시 첫글자를 대문자 형태로 지정한다.

- **문법**
    
    > class명(첫글자 대문자) :
                생성자 # 기능 처리 역할
                변수 # 데이터 저장 역할
                메서드 # 기능 처리 역
    
    변수명 = 클래스명( ) # 객체 생성, 클래스를 메모리에 올리는 작업
    > 

### 생성자

- **개요**
    - 문법
    
    ```python
    def __init__(self):
    			pass
    ```
    
    - 생성자도 호출해야 출력된다 ⇒ 호출방법 : 클래스명( )
    - 객체 생성 ⇒ 생성자 자동 호출
    - 생성자 역할 : 객체 생성시 실제 인스턴스가 필요한 데이터, 인스턴스 변수 초기화
    
- **예제**
    
    ```python
    class Cat:
        def __init__(self, n, a):
            print("__init__ 생성자")
            self.username = n
            self.age = a
    
    c = Cat("야옹이", 2) # 첫번째 고양이 생성
    print(id(c)) # 변수 c가 참고하는 주소 : 2530208282992
    print(c.username, c.age)
    
    c2 = Cat("나비", 1) # 두번째 고양이 생성
    print(id(c2)) # 변수 c가 참고하는 주소 : 2148561456480
    print(c2.username, c2.age)
    ```
    

### 메서드

- **개요**
    - **문법**
        
        ```python
        class 클래스명:
        
             #생성자 ==> 인스턴스 변수값 초기화 담당
             def __init__(self):
             self.변수명 = n # 인스턴스 변수 ==> 값 저장 담당
        
             # method ==> 일반적인 기능 처리 담당
             def 메서드명(self):
                 pass
        ```
        
    - 클래스의 구성요소로서 기능 처리를 담당하는 함수
    - 반드시 self로 지정된 파라미터를 설정해야 한다.
    - 메서드는 반드시 객체 생성 후에 변수명.메서드 형식으로 사용할 수 있다.
    - 메서드명은 소문자로 지정하고 _(언더바) 사용 가능하다.
    
- **예제**
    
    ```python
    ## class 생성 ##
    class Cat:
    
        # 생성자
        def __init__(self, n, a):
            # 인스턴스 변수
            self.username = n
            self.age = a
    
        # method (age 수정)
        def setage(self, n):
            self.age = n
    
    		# method2 (age값 반환)
        def getage(self):
            return self.age
    
    ## 실제 고양이(인스턴스) 생성 ##
    c = Cat("야옹이", 2)
    print(c.username, c.age) # 야옹이 2
    print(c.username, c.getage()) # 야옹이 2
    
    c2 = Cat("나비", 1)
    print(c2.username, c2.age) # 나비 1
    print(c2.username, c2.getage()) # 나비 1
    ```
    

### 상속 전

- **Cat 클래스 생성**
    
    ```python
    class Cat:
    
        def __init__(self,n,a):
            self.username = n
            self.age = a
    
        def info(self):
            return self.username, self.age #튜플로 리턴
    ```
    
- **Dog 클래스 생성**
    
    ```python
    class Dog:
    
        def __init__(self, n, a, g):
            self.username = n
            self.age = a
            self.gender = g
    
        def info(self):
            return self.username, self.age, self.gender  # 튜플로 리턴
    ```
    
- **호출**
    
    ```python
    c = Cat("야옹이", 2)
    d = Dog("망치", 1, "수컷")
    
    print("고양이: ", c.info()) # 고양이:  ('야옹이', 2)
    print("강아지: ", d.info()) # 강아지:  ('망치', 1, '수컷')
    ```
    
    <aside>
    💡 변수.info( ) 함수를 이용하면 튜플로 반환된다.
    
    </aside>
    

### 상속 후

- 공통적인 속성 및 동작 추출하여 큰 개념의 Pet 클래스를 작성한다.

- 부모 클래스 Pet 작성 (공통 속성 : 인스턴스 변수 username, age)
    
    ```python
    class Pet: # 자동으로 (Object)가 지정된다.
        def __init__(self,n,a):
            self.username = n
            self.age = a
    ```
    
- 자식 클래스 Cat 작성
    
    ```python
    class Cat(Pet): # Cat is a Pet, 부모 클래스 명시 (상속관계)
    
        def __init__(self,n,a):
            # 부모 클래스의 속성 및 메소드를 자동으로 불러와 자식 클래스에서도 사용이 가능하도록
            super().__init__(n,a) # super() : 부모 호출
    
        # 추가 메서드 지정 가능
        def info(self):
            return self.username, self.age #튜플로 리턴
    ```
    
- 자식 클래스 Dog 작성
    
    ```python
    class Dog(Pet):
    
        def __init__(self,n,a,g):
            super().__init__(n,a)
            self.gender = g
    
        def info(self):
            return self.username, self.age, self.gender  # 튜플로 리턴
    ```
    
- 호출
    
    ```python
    c = Cat("야옹이", 2)
    d = Dog("망치", 1, "수컷")
    
    print("고양이: ", c.info()) # 고양이:  ('야옹이', 2)
    print("강아지: ", d.info()) # 강아지:  ('망치', 1, '수컷')
    ```
    

### 클래스 변수 및 메서드

```python
class Person:

    # 클래스 변수, 단 한번 생성 ==> 목적: 여러 인스턴스가 공유 가능
		address = "서울" 

    def __init__(self,n,a):
        # 인스턴스 변수, 객체 생성시 마다 매번 생성
        self.username = n
        self.age = a

    def info(self):
        return self.username, self.age, Person.address

		@classmethod # 메서드가 클래스 메서드임을 표시
		def get_address(cls):
		    return Person.address
```

```python
Person.address = "제주" # 한번에 모든 인스턴스 address가 변경 된다.
print(Person.address)

p = Person("홍길동",20)
p2 = Person("이순신",44)

print("p1", p.info(),Person.get_address())
print("p2", p2.info(), Person.get_address())
```