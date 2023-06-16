# SQL_Oracle

- **오라클 개요**
    1. 회원가입 : www.oracle.com
    2. 오라클 버전
        
        1)  enterprise 버전 : 현업에서 사용. 서비스를 여러개 생성 가능. 이름을 임의로 지정 가능.
        
        2) express 버전 : 개인용, 교육용. 하나의 서비스만 지원. (서비스 이름 = ex)
        
        * 설치 주의 : 압축 해제 폴더는 한글, 공백 없이 생성하여 설치해야 함.
        
        3) Oracle 홈페이지 다운로드 경로 : Hardware and Software – Hard & software – Oracle DB - Download Oracle Database 19c
        
    3. 오라클 관리자 계정
        
        1) sys
        
        2) system(계정)/oracle(비번) → 주로 사용
        
    4. 오라클 port : 1521
        
        오라클 서비스명 : xe
        
    5. 오라클 실행하기 위해선 작업관리자-서비스에서 OracleXETNSListener,  OracleServiceXE가 실행 중이어야 함.
    6. 오라클 접속 방법
        
        무료 외부 Tool
        
        1) sql*plus
        
        - 오라클 설치시 자동 설치됨.(sqlplus.exe)
        - text 기반이어서 사용에 불편.
        
        2) sqlDeveloper
        
        - 오라클 상위버전에 내장되어 있거나 (11g버전에는 없음) 홈페이지에서 별도 다운로드 받아야 함.
        - GUI 기반
        - 자바언어로 만들어져 있어 JDK 필요 ./ JDK 미포함 버전은 따로 설치 필요.
        - 실행방법 : 명령 프롬포트에 sqlplus system/oracle 입력 엔터
    7. 수업에 사용할 계정
        
        SCOTT/TIGER
        
        오라클에서 제공함. 경로 : C:\oraclexe\app\oracle\product\11.2.0\server\rdbms\admin
        
        관리자 계정으로 실행해야 함.
        
    

## SQL **데이터베이스 개요**

### DB vs DBMS

- **DB :** 많은 사람들이 공유해서 사용할 목적으로 통합 관리되는 정보(데이터)의 집합
- **DBMS :** DB를 효율적으로 저장하고 관리 및 검색할 수 있는 소프트웨어를 설치해서 사용하는 것

### **Data를 관리하는 구조**

- **관계형 DB**
    - 정형 data에 최적 (cf. 비정형 data(소리, 영상, 이미지 등) → NoSQL)
    - 대표적인 관계형 데이터베이스 관리 시스템 : Oracle, MariaDB, Mysql, MSsql
    - 2차원 테이블 형태로 데이터를 관리
        
        ![Untitled](SQL_Oracle%201e0ac134fb854b04a63931f1010100ed/Untitled.png)
        
        - 컬럼 : 열 정보
        - 행 정보 : 레코드
        - null 값이 있을 수 있음.

### **SQL**

- **SQL** : 사용자와 관계형 데이터베이스를 연결시켜 주는 표준 검색 언어
- **종류**
    - **DQL(Data Query Language) :** SELECT문을 사용하여 테이블에 저장된 데이터를 검색할 때 사용
    - **DML(Data Manipulation Language) :** Insert(생성), Update(수정), Delete(삭제), Merge(병합)
    - **TCL(Transaction Control Language) :** 트랜잭션과 관련된 작업을 처리하기 위한 SQL문.
        
        ****트랜잭션 :** insert, delete 등 여러개의 DML문을 반드시 하나처럼 동작하게끔 묶음 처리하는 것)
        
        ** ex. 1,000원이 있는 A 계좌에서 0원이 있는 B계좌로 500원을 이체.
        
        → A 계좌를 1,000원에서 500원으로 update + B 계좌에 500원 insert
        
        = 두개의 작업을 하나의 계좌이체라는 작업으로 묶어서 처리
        
    - **DDL(Data Definition Language) :** 테이블, 뷰, 인덱스, 시퀀스 같은 객체를 생성(CREATE문), 수정(ALTER문), 삭제(DROP문)
        
        **** 오라클 객체**
        
        1) table : data 저장
        
        2) index : table 검색 속도 up (색인표 역할)
        
        3) view : 보안, 복잡한 SQL문 간소화
        
        4) sequence : 특정 컬럼 넘버링
        
        5) synonym : table의 별칭 (보안)
        

## **데이터의 유형(Data Type)**

컬럼에 저장할 수 있는 data의 종류 및 값의 크기

### **수치형**

- **정수 :** number(자릿수)
    
    ex. number(4) : 0~9999
    
- **실수 :** number(전체 자릿수, 소수점 자릿수)
    
    ex. number(3,2) : x.xx
    

### **문자형**

- **char() :** 고정길이(무조건 지정한 크기만큼 생성)
    
    ex. char(2) = 2byte 저장 가능
    
    ** 영문자 1개 = 1byte / 한글 1글자 = 2byte
    
- **varchar2() :** 가변길이(저장할 글자크기만큼만 생성됨)
- **null 값**
    1. 값 없음을 의미
    2. null 값 연산결과는 null 값이 나온다.
        
        null 값을 임의의 값으로 변환하여 연산해야 한다. (함수 nvl(컬럼명, 값))
        
    3. 기본적으로 컬럼은 null 값을 가질 수 있다. 강제적으로 null 값을 허용하지 않게 할 수도 있다. → not null 제약조건
    
    ❗제약조건 타입❗
    
    | 제약조건 타입 | 설명 |
    | --- | --- |
    | primary key | • 레코드를 식별하기 위한 용도. 
    • 내부적으로 unique제약조건과 not null 제약조건을 포함한다.
    • 자동으로 인덱스(index)가 생성됨.
    • 복합컬럼
    ex) 학번, 사번, 주민번호 |
    | unique | • 컬럼에 유일한 값을 저장하기 위한 용도.
    • null 값 포함 가능.
    • 자동으로 인덱스(index)가 생성됨. |
    | not null | • 컬럼에 반드시 값을 저장해야 하는 용도. |
    | check | • 비즈니스 규칙 
    ex) 일반적으로 초등학교는 1~6학년까지 있음. 7학년이라는 값은 저장 불가능 |
    | foreign key | • 하나의 테이블에서 다른 테이블을 참조하기 위해 사용되는 용도(join).
    • ‘참조키’, ‘외래키’ 라고 부름.
    • 테이블당 여러개 지정 가능.
    • foreign key를 가지고 있는 테이블 = slave table / 참조당하는 테이블 = master table
    📌foreign key가 참조할 수 있는 컬럼은 master table의 primary key 값 unique로 되어있는 컬럼의 값 또는 null 값 만 참조 가능하다. |
    1. 컬럼에서 null 조회
        
        is null 연산자 이용 or in not null 연산자 이용
        
    2. 정렬(오름차순, 내림차순)
        
        오라클은 null을 최대값으로 지정함.
        

## **SELECT 문**

### **SELECT의 기능**

: 데이터베이스로부터 데이터를 검색하는 기능

1. **selection :** 행을 선택하기 위해 사용.
2. **projection :** 열을 선택하기 위해 사용.
3. **join :** 여러 테이블이 공통적으로 가진 컬럼을 이용해서 다른 테이블에 저장되어 있는 데이터를 가져오기 위해 사용.

![Untitled](SQL_Oracle%201e0ac134fb854b04a63931f1010100ed/Untitled%201.png)

### **SELECT문_기본**

1. **기본적인 SELECT 문**
    
    ```sql
    SELECT 절
    FROM table;
    ```
    
2. **계정이 소유한 테이블 정보(테이블 목록) 보기**
    
    ```sql
    SELECT * from tab;
    ```
    
3. **특정 테이블(dept)의 컬럼 구조 보기 (describe)**
    
    ```sql
    desc dept;
    ```
    
    ![Untitled](SQL_Oracle%201e0ac134fb854b04a63931f1010100ed/Untitled%202.png)
    
4. **특정 테이블(dept)에 있는 모든 컬럼(*) 보기**
    
    ```sql
    SELECT *
    from dept;
    ```
    
5. **보고싶은 컬럼만 나오도록 컬럼명 명시**
    
    ```sql
    SELECT deptno, loc
    from dept;
    ```
    
6. **컬럼명에 별칭 부여 =⇒ 컬럼명 as 별칭 (as 생략 가능)**
    
    ```sql
    SELECT deptno as 부서번호
    from dept;
    ```
    
    ** 별칭에 공백이 있으면 안됨.
    
    ```sql
    SELECT deptno as 부서 번호, loc 위치
    from dept;
    ```
    
    ** 별칭에 공백 필요시 “” 활용
    
    (SQL문에서 "" 사용하는 경우는 별칭이 유일. 다른 문자(문자열) 표현은 '' 사용한다.)
    
    ```sql
    SELECT deptno as "부서 번호", loc 위치
    from dept;
    ```
    
7. **연산된 컬럼 보기**
    
    ```sql
    SELECT empno, sal, sal + 100
    from emp;
    ```
    
    ![Untitled](SQL_Oracle%201e0ac134fb854b04a63931f1010100ed/Untitled%203.png)
    
    ** 연산한 컬럼에도 별칭 부여 가능
    
    ```sql
    SELECT empno, sal, sal + 100 as 보너스
    from emp;
    ```
    
    ![Untitled](SQL_Oracle%201e0ac134fb854b04a63931f1010100ed/Untitled%204.png)
    
8. **연결 가능**
    1. **컬럼 || 컬럼**
    
    ```sql
    SELECT ename || sal as 이름과월급
    from emp;
    ```
    
    ![Untitled](SQL_Oracle%201e0ac134fb854b04a63931f1010100ed/Untitled%205.png)
    
    **b.  컬럼 || 값**
    
    ```sql
    SELECT ename || '사원'
    from emp;
    ```
    
    ![Untitled](SQL_Oracle%201e0ac134fb854b04a63931f1010100ed/Untitled%206.png)
    
9. **중복값 제거 (distinct)**
    
    ```sql
    select distinct job
    from emp; 
    ```
    
10. **null 값으로 연산**
    1. null값으로 치환하지 않고 그대로 연산할 경우 → 결과 값도 null 
    
    ```sql
    select empno, sal, comm, (sal*12) + comm
    from emp;
    ```
    
    b.  null 값 치환해서 연산 (nvl)
    
    ```sql
    select empno, sal, comm, (sal*12) + nvl(comm,0)
    from emp;
    ```
    

## **Where**

 ****모든 데이터가 아닌 특정 조건에 일치하는 데이터만 조회

### **비교 연산자**

![Untitled](SQL_Oracle%201e0ac134fb854b04a63931f1010100ed/Untitled%207.png)

1. emp 테이블에서 sal이 800인 사원의 사원번호, 이름, sal은?
    
    ```sql
    select empno, ename, sal
    from emp
    where sal = 800;
    ```
    
2. 이름이 FORD인 사원의 사원번호, 이름, sal은?
    
    ```sql
    select empno, ename, sal
    from emp
    where ename = 'FORD';
    ```
    
    SQL문은 식별자의 대소문자를 구별하지 않지만 값의 대소문자는 구별해야 함.
    Maria DB는 값의 대소문자도 구별하지 않는다.
    
3. 입사일이 2018년 이후인 사원의 사원번호, 이름, 입사일은?
    
    ```sql
    select empno, ename, sal, hiredate
    from emp
    where hiredate > '2017/12/31';
    ```
    

### **범위 지정 between A and B**

반드시 A의 값이 B보다 작아야 한다.

범위는 A와 B를 포함한다.

1. sal이 800이상 2000이하인 사원은?
    
    ```sql
    select empno, ename, sal, hiredate
    from emp
    where sal BETWEEN 800 and 2000;
    ```
    
2. 1980년 입사한 사원은?
    
    ```sql
    select empno, ename, sal, hiredate
    from emp
    where hiredate BETWEEN '80/01/01' and '80/12/31';
    ```
    

### **IN 연산자**

여러 개의 값을 한꺼번에 비교할 때 사용. 내부적으로 or 연산자로 실행 됨. 

1. sal이 800 또는 1500 또는 2000인 사원은?
    
    ```sql
    select empno, ename, sal, hiredate
    from emp
    where sal in (800,1500,2000);
    ```
    
2. 입사일이 80/12/17 또는 80/12/01 인 사원은?
    
    ```sql
    select empno, ename, sal, hiredate
    from emp
    where hiredate in ('80/12/17','80/12/01');
    ```
    

### **Like 연산자**

임의의 문자만 일치하더라도 검색이 가능하게 함.

와일드카드 문자와 함께 사용 됨.

| 와일드 카드 문자 | 설명 |
| --- | --- |
| % | % 위치에 0개 이상의 문자(열)과 대체 |
| _ | _위치에 반드시 한 개 문자와 대체 |

1. A로 시작하는 이름의 사원은?
    
    ```sql
    select empno, ename, sal, hiredate
    from emp
    where ename like 'A%';
    ```
    
2. T가 포함된 이름의 사원은?
    
    ```sql
    select empno, ename, sal, hiredate
    from emp
    where ename like '%T%';
    ```
    
3. 두번째 문자가 L인 이름의 사원은?
    
    ```sql
    select empno, ename, sal, hiredate
    from emp
    where ename like '_L%';
    ```
    

1. 이름이 5글자이고 마지막은 N으로 끝나는 이름의 사원은?
    
    ```sql
    select empno, ename, sal, hiredate
    from emp
    where ename like '____N';
    ```
    

### **null 값 찾기. is null**

1. 커미션이 없는 사원은? = comm이 null 값인 사원은?
    
    ```sql
    select empno, ename, sal, hiredate
    from emp
    where comm is null;
    ```
    
2. 커미션이 있는 사원은?
    
    ```sql
    select empno, ename, sal, hiredate
    from emp
    where comm is not null;
    ```
    

### **논리 연산자**

WHERE절에 명시된 조건이 두 개 이상인 경우

| 연산자 | 설명 |
| --- | --- |
| AND | 두 가지 조건을 모두 만족하는 데이터를 검색 |
| OR | 두 가지 조건 중에서 한 가지만 만족하더라도 검색 |
| NOT | 지정된 조건이 아닌 데이터를 검색 |

![Untitled](SQL_Oracle%201e0ac134fb854b04a63931f1010100ed/Untitled%208.png)

1. 영업사원이면서 sal이 1500이상인 사원은?
    
    ```sql
    select empno, ename, sal, hiredate
    from emp
    where job = 'SALESMAN' and sal >= 1500;
    ```
    
2. 영업사원이거나 sal이 1500이상인 사원은?
    
    ```sql
    select empno, ename, sal, hiredate
    from emp
    where job = 'SALESMAN' or sal >= 1500;
    ```
    
3. FORD가 아닌 사원은?
    
    ```sql
    select empno, ename, sal
    from emp
    where not ename = 'FORD';
    ```
    
4. SMITH와 FORD가 아닌 사원은?
    
    ```sql
    SELECT empno, ename, sal, hiredate
    from EMP
    where NOT ename IN ('SMITH','FORD');
    ```
    
5. 이름이 J로 시작하지 않는 사원은?
    
    ```sql
    SELECT empno, ename, sal, hiredate
    from EMP
    where ename NOT LIKE 'J%';
    ```
    

연산자 중에서도 우선순위가 있다.

![Untitled](SQL_Oracle%201e0ac134fb854b04a63931f1010100ed/Untitled%209.png)

## **ORDER BY (정렬)**

### 기본 특징

- **기본 문법 :** ORDER BY 컬럼명;
- 정렬 방법 : 오름차순(ASC), 내림차순(DESC)
- 수치, 문자, 날짜 데이터 모두 정렬 가능

### order by 컬럼명

- **기본 문법**

```sql
SELECT empno, ename, sal, hiredate
from EMP
order by sal;
```

<aside>
💡 ORDER BY 뒤에는 select 절에서 지정한 컬럼을 사용해야 한다.
Default : 오름차순

</aside>

- **오름차순 명시**

```sql
SELECT empno, ename, sal, hiredate
from EMP
order by sal asc; -- 명시적으로 오름차순 지정. asc
```

- **내림차순 명시**

```sql
SELECT empno, ename, sal, hiredate
from EMP
order by sal DESC; -- 명시적으로 내림차순 지정. DESC
```

### order by 별칭

- **SELECT문에서 컬럼 별칭 지정 후 정렬에 사용**
    
    ```sql
    SELECT empno, ename, sal as salary, hiredate
    from EMP
    order by salary;
    ```
    

### order by 컬럼 순서

- **SELECT 절에서 지정한 컬럼 순서로 정렬 기준 지정**
    
    ```sql
    SELECT empno, ename, sal as salary, hiredate
    from EMP
    order by 3; -- select에서 지정한 컬럼 중 세번째인 sal을 기준으로 정렬
    ```
    

### 다중 정렬

- order by 컬럼명1, 컬럼명2
    
    ⇒ 컬럼명1로 먼저 정렬 후 컬럼명2로 재정렬
    
    ```sql
    SELECT empno, ename, sal as salary, hiredate
    from EMP
    order by salary, hiredate ;
    ```
    
    ```sql
    SELECT empno, ename, sal as salary, hiredate
    from EMP
    order by salary, hiredate DESC; -- hiredate를 내림차순으로 재정렬
    ```
    
    ```sql
    SELECT empno, ename, sal as salary, hiredate
    from EMP
    order by 3, 4 DESC;
    ```
    

### Null 값 정렬

정렬하는 컬럼에 Null 값이 존재하는 경우 → Null 값을 가장 큰 값으로 처리

오름차순일 때에는 가장 아래에, 내림차순일 때에는 가장 위에 위

## **함수**

### **단일행 함수 - 문자열**

모든 행에 각각 적용되어 행의 개수와 동일한 개수를 반환

SELECT, WHERE, ORDER BY절에 사용 가능

![Untitled](SQL_Oracle%201e0ac134fb854b04a63931f1010100ed/Untitled%2010.png)

1. **CONCAT : 문자열 연결**
    
    ```sql
    select concat('ORACLE','SERVER') from dual;
    ```
    
    결과 : ORACLESERVER
    
    CONCAT 함수는 연결 연산자 || 와 같다.  
    
2. **LPAD : 오른쪽 정렬 후 왼쪽에 생긴 빈 공백에 특정 문자를 채운다.**
    
    1) **공백으로 채우기** → 글자수 10 뒤에 채울 문자 지정 X
    
    ```sql
    select lpad('MILLER', 10) from dual;
    ```
    
    결과 :     MILLER
    
    2) *** 로 채우기**
    
    ```sql
    select lpad('MILLER', 10, '*') from dual;
    ```
    
    결과 :****MILLER
    
3. **SUBSTR : 부분열 반환**
    
    1) 전체 문자열 중 8번째 자리 문자로부터 1 글자 반환
    
    ```sql
    select substr('000101-3234232', 8, 1 ) from dual;
    ```
    
    결과 : 3
    
    2) 음수도 적용 가능하다.
    
    ```sql
    select substr('000101-3234232', -7 ) from dual;
    ```
    
    결과 : 3234232
    
    시작 위치 값이 음수이므로 뒤에서부터 7번째 자리부터 마지막 글자까지 반환
    
4. **REPLACE : 문자열 치환**
    
    문자열에서 J를 BL로 치환하라.
    
    ```sql
    select replace('JACK and JUE', 'J', 'BL') from dual;
    ```
    
    결과 : BLACK
    
5. **INSTR : 특정 문자의 위치를 반환**
    
    1) 첫번째 자리부터 L의 시작 위치를 반환하라.
    
    ```sql
    select instr('MILLER' , 'L', 2 ) from dual;
    ```
    
    결과 : 3
    
    2) 첫번째 자리부터 L의 두번째 위치를 반환하라.
    
    ```sql
    select instr('MILLER' , 'L', 1, 2 ) from dual;
    ```
    
    결과 : 4
    
    3) 다섯번째 자리부터 L의 시작 위치를 반환하라.
    
    ```sql
    select instr('MILLER' , 'L', 5 )
    ```
    
    결과 : 0
    
6. **특정 문자 삭제**
    
    1) LTRIM : 왼쪽의 특정 문자 삭제
    
    ```sql
    select LTRIM('MILLERM', 'M') from dual;
    ```
    
    결과 : ILLERM
    
    ```sql
    select LTRIM('MMMMILLERM', 'M') from dual;
    ```
    
    결과 : ILLERM
    
    왼쪽의 특정 문자가 모두 삭제될 때 까지 삭제됨.
    
    2) RTRIM : 오른쪽의 특정 문자 삭제
    
    ```sql
    select RTRIM('MILLERM', 'M') from dual;
    ```
    
    결과 : MILLER
    
7. **공백 문자 삭제**
    
    ```sql
    select LTRIM('     MILLERM      ') from dual; -- 왼쪽 공백 제거/ MILLERM
    select RTRIM('     MILLERM      ') from dual; -- 오른쪽 공백 제거 /MILLERM
    ```
    
8. **왼쪽/오른쪽/양쪽 문자 및 공백 제거**
    
    1) 왼쪽 문자 제거 : TRIM (leading ~ from ~)
    
    ```sql
    select TRIM(leading 1 from 111234561111 ) from dual;
    ```
    
    결과 : 234561111
    
    2) 오른쪽 문자 제거 : TRIM (trailing~ from ~)
    
    ```sql
    select TRIM(trailing 1 from 111234561111 ) from dual;
    ```
    
    결과 : 11123456
    
    3) 양쪽 문자 제거 : TRIM(both~ from ~)
    
    ```sql
    select TRIM(both 1 from 111234561111 ) from dual;
    ```
    
    결과 : 23456
    

### **단일행 함수 - 수치**

![Untitled](SQL_Oracle%201e0ac134fb854b04a63931f1010100ed/Untitled%2011.png)

### **단일행 함수 - 날짜**

![Untitled](SQL_Oracle%201e0ac134fb854b04a63931f1010100ed/Untitled%2012.png)

1. **SYSDATE**
    - SYSDATE : 현재 날
    
    ```sql
    select sysdate, systimestamp from dual;
    -- 23/06/16
    -- 23/06/16 00:05:22.991000000 +09:00
    ```
    
    - SYSDATE에 +1, -1을 하면 일수에 +1, -1 한 날짜가 반환됨.
    
    ```sql
    select sysdate, sysdate + 1, sysdate - 1 from dual;
    ```
    
    결과 : 23/05/26, 23/05/27, 23/05/25
    
2. **month_between : 두 날짜 사이의 개월 수 반환**
    
    ```sql
    select months_between(sysdate+100, sysdate) from dual;
    ```
    
    결과 : 3.25
    
3. **add_months : 특정 개월 수를 더한 날짜 반환**
    
    ```sql
    select add_months(sysdate, 1), add_months(sysdate, -1) from dual;
    ```
    
    결과 : 23/06/26, 23/04/26
    
     
    
4. **next_day : 명시된 날짜로부터 다음 요일에 대한 날짜 반환**
    
    ```sql
    select next_day(sysdate, '화') from dual;
    ```
    
    결과 : 오늘 날짜(23/05/26)로부터 가장 빠른 화요일 → 23/05/30
    
5. **last_day : 월의 마지막 날짜 반환**
    
    ```sql
    select last_day(sysdate) from dual;
    ```
    
    결과 : 23/06/30
    
6. **round : 날짜 반올림**
    
    ```sql
    select round(sysdate, 'YEAR'), round(sysdate, 'MONTH') from dual;
    ```
    
    결과 : year 기준으로 아직 상반기 이므로 상반기 첫째 날인 23/01/01, month를 기준으로 15일이 지났으므로 다음 달 첫째 날인 23/06/01
    
7. **trunc : 날짜 절삭**
    
    ```sql
    select trunc(sysdate, 'YEAR'), trunc(sysdate, 'MONTH') from dual;
    ```
    
    결과 : year 기준으로 올해 첫 날인 23/01/01, month를 기준으로 이 달의 첫째 날인 23/05/01
    

❗RR과 YY 타입 비교❗

오라클에서 년도를 표기하는 방법은 RR형식과 YY형식이 있다.

![Untitled](SQL_Oracle%201e0ac134fb854b04a63931f1010100ed/Untitled%2013.png)

YY형식은 현재년도와 동일하게 처리한다.

![Untitled](SQL_Oracle%201e0ac134fb854b04a63931f1010100ed/Untitled%2014.png)

RR형식은 특정 규칙이 있다.

ex) 2017 : 현재년도의 뒤 두자리가 00~49, 명시된 년도의 뒤 두자리가 00~49이므로 RR을 현재세기인 2017을 반환한다.

![Untitled](SQL_Oracle%201e0ac134fb854b04a63931f1010100ed/Untitled%2015.png)

### **단일행 함수 - 변환 함수**

![Untitled](SQL_Oracle%201e0ac134fb854b04a63931f1010100ed/Untitled%2016.png)

![Untitled](SQL_Oracle%201e0ac134fb854b04a63931f1010100ed/Untitled%2017.png)

숫자를 날짜로 변경하거나 날짜를 숫자로 변경하는 것은 불가능

- **문자를 숫자로 변환 to_number**
    
    ```sql
    select to_number('100')+100 from dual;
    ```
    
    - ‘1,000’이라는 ‘문자’를 ‘999,999’ 형태로 변환
    
    ```sql
    select to_number('1,000','999,999')+100 from dual;
    ```
    
    결과 : 1100
    
    <aside>
    💡 1,000 처럼 쉼표가 섞여있는 숫자는 숫자로 인식하지 않는다.
    
    따라서 알맞은 형태의 숫자로 변환하는 작업이 필요하다.
    
    </aside>
    
    ```sql
    select to_number('1,000,000,000','999,999,999,999')+100 from dual;
    ```
    
    결과 : 1000000100
    
    <aside>
    💡 자리 수 맞추어 변환해 주어야 함.
    
    </aside>
    
    - 함수 없이 문자에서 숫자로 자동 변환되는 경우도 있음.
    
    ```sql
    SELECT last_name, salary
    FROM employees
    WHERE salary = '17000';
    ```
    
    <aside>
    💡  ‘17000’은 문자이지만 오라클에서는 숫자로 자동 인식하여 처리
    
    </aside>
    
- **숫자를 문자로 변환 to_char**
    
    ```sql
    select to_char(1000) from dual;
    select to_char(1000, 'L999,999') from dual;
    select to_char(1000, '$999,999') from dual;
    select to_char(100000000, '$999,999,999') from dual;
    ```
    
    결과 : 1000 / ￦1,000 / $1,000 / $100,000,000
    
    ![Untitled](SQL_Oracle%201e0ac134fb854b04a63931f1010100ed/Untitled%2018.png)
    
- **문자를 날짜로 변환 to_date**
    - 다음 네가지 날짜 표현식은 오라클이 날짜로 인식한다.
    
    ```sql
    select to_date('2023/05/23') from dual;
    select to_date('20230523') from dual;
    select to_date('2023-05-23') from dual;
    select to_date('2023,05,23') from dual;
    ```
    
    ```sql
    SELECT TO_DATE( '20170802181030' , 'YYYYMMDDHH24MISS' )
    FROM dual;
    ```
    
    <aside>
    💡 임의의 문자열도 날짜로 변환할 수 있다.
    
    </aside>
    
- **날짜를 문자로 변환 to_char**
    
    ```sql
    select sysdate, to_char(sysdate) from dual;
    select sysdate, to_char(sysdate, 'YYYY') from dual; -- 날짜에서 연도만 추출 가능
    select sysdate, to_char(sysdate, 'YYYY:MM:dd') from dual;
    select sysdate, to_char(sysdate, 'YYYY/MM/dd') from dual;
    select sysdate, to_char(sysdate, 'YYYY/MM/dd AM') from dual; -- 오전/오후 표시
    select sysdate, to_char(sysdate, 'YYYY/MM/dd day') from dual; -- 요일 표시
    select sysdate, to_char(sysdate, 'YYYY/MM/DD PM') from dual;
    select sysdate, to_char(sysdate, 'YYYY"년"MM"월"dd"일"') from dual;
    select sysdate, to_char(sysdate, 'YYYY"년"MM"월"dd"일"HH"시"MI"분"SS"초"') from dual;
    select sysdate, to_char(sysdate, 'YYYY/MM/DD (PM) DAY DY HH24:MI:SS') from dual;
    ```
    
    결과
    
    23/05/26
    
    2023
    
    2023:05:26
    
    2023/05/26
    
    2023/05/26 오후
    
    2023/05/26 금요일
    
    2023/05/26 오후
    
    2023년 05월 26일
    
    2023년 05월 26일 04시 46분 04초
    
    2023/05/26 (오후) 금요일 금 16:46:04
    
- **날짜에서 특정 날짜/시간 정보 얻기**
    - sysdate에는 시, 분, 초 데이터 없으므로 systimestamp 이용해야 함.
    
    ```sql
    select sysdate,
    EXTRACT(year from sysdate),
    EXTRACT(month from sysdate),
    EXTRACT(day from sysdate),
    EXTRACT(hour from SYSTIMESTAMP),
    EXTRACT(minute from SYSTIMESTAMP),
    EXTRACT(second from SYSTIMESTAMP)
    from dual;
    ```
    
    결과
    
    23/05/26
    
    2023
    
    5
    
    26
    
    5
    
    2
    
    44
    

### **단일행 함수 - CASE 함수**

- 조건이 반드시 일치하지 않는 경우에 사용되는 SQL문
- 대표적으로 부등, 비교 연산자를 사용하는 형태
- **동등비교**
    
    ```sql
    select empno, ename, sal, job,
    case job when 'ANALYST' then sal**1.1
    when 'CLERK' then sal**1.2
    when 'MANAGER' then sal**1.3
    when 'PRESIDENT' then sal**1.4
    when 'SALESMAN' then sal*1.5
    END "급여"
    from emp;
    ```
    
    ![Untitled](SQL_Oracle%201e0ac134fb854b04a63931f1010100ed/Untitled%2019.png)
    
- **부등비교**
    
    ```sql
    select empno, ename, sal,
    CASE when sal >=0 and sal <=1000 then 'E'
    when sal >1000 and sal <=2000 then 'D'
    when sal >2000 and sal <=3000 then 'C'
    when sal >3000 and sal <=4000 then 'B'
    when sal >4000 and sal <=5000 then 'A'
    END "등급"
    from emp;
    ```
    
    ![Untitled](SQL_Oracle%201e0ac134fb854b04a63931f1010100ed/Untitled%2020.png)
    

### **그룹 함수**

- **개요**
    1. **적용 :** 그룹 함수는 반드시 여러 레코드에 대해 하나의 함수가 적용되어 하나의 결과를 반환한다.
    2. **그룹으로 묶는 방법**
        
        1) 자동(Group by 사용 X) : 전체 레코드가 하나의 그룹으로 묶임
        
        2) Group by 명시 : Group by 컬럼명;
        
- **대표적인 그룹 함수**
    
    ![Untitled](SQL_Oracle%201e0ac134fb854b04a63931f1010100ed/Untitled%2021.png)
    
    ```sql
    select max(sal), min(sal), sum(sal), avg(sal), count(*)
    from emp;
    ```
    
    → emp 테이블 중 sal의 최대값, 최소값, 합계, 평균, 레이블 개수
    
    - **count() : 전체 레코드 개수 / () 안의 *은 count 함수만 가능**
    
    ```sql
    select count(*)
    from emp;
    ```
    
    결과 : emp 전체 레코드 개수 13
    
    <aside>
    💡 count(컬럼) : null을 제외한 레코드 개수
     count( * ) : null을 포함한 레코드 개수
    
    </aside>
    
    - **Group by 절**
        - 특정 컬럼을 기준으로 그룹으로 묶을 때 사용
            
            ex) 학년별, 직급별, 성별 등
            
        - Group by  절 다음에는 컬럼 별칭이나 SELECT의 순서값을 사용할 수 없고 반드시  SELECT절에서 명시한 표현식을 기술해야 한다.
        1. **부서별 sal 최대값 조회하기**
            
            ```sql
            select deptno, max(sal)
            from emp
            group by deptno
            order by 1;
            ```
            
            ![Untitled](SQL_Oracle%201e0ac134fb854b04a63931f1010100ed/Untitled%2022.png)
            
        2. **부서별, job별 sal 최대값 조회하기(다중 그룹핑)**
            
            ```sql
            select deptno, job, max(sal)
            from emp
            group by deptno, job
            order by 1;
            ```
            
            ![Untitled](SQL_Oracle%201e0ac134fb854b04a63931f1010100ed/Untitled%2023.png)
            
        
    - **Having 절**
        - GROUP BY절에 의해서 생성된 결과 중에서 조건과 일치하는 데이터를 추출할 때 사용 (Group by 필터링)
        - Having절이 있는 SELECT문 처리 순서
            
            ```sql
            select deptno, max(sal) -- 5) 결과 값의 럼은 필터링된 deptno와 그에 대한 sal 최대값만
            from emp -- 1) 12개의 레이블 가진 emp 테이블로부터
            WHERE sal < 5000 -- 2) sal이 5000보다 작은 레이블만 가져와라 -> 11개 레이블
            group by deptno  -- 3) 11개의 레코드를 deptno를 기준으로 그룹핑하라
            having DEPTNO = 10; -- 4) 그 중 deptno가 10인 그룹만 가져와라
            ```
            
        - Where 절에는 그룹함수를 사용할 수 없다. (where 절이 먼저 처리되므로)
        
        1. 부서별로 sal이 5000이하인 사원의 sal의 최대값을 조회하라. 단 레코드 값의 개수가 2 이상인 그룹만 가져와라.
            
            ```sql
            select deptno, max(sal)
            from emp
            WHERE sal < 5000
            group by deptno
            having count(*) > 2;
            ```
            
            ![Untitled](SQL_Oracle%201e0ac134fb854b04a63931f1010100ed/Untitled%2024.png)
            
    

## **조인**

여러 테이블을 연결해서 필요한 데이터를 조회하는 방법

### 종류

![Untitled](SQL_Oracle%201e0ac134fb854b04a63931f1010100ed/Untitled%2025.png)

![Untitled](SQL_Oracle%201e0ac134fb854b04a63931f1010100ed/Untitled%2026.png)

### **Equi 조인**

- **natural join**
    - 같은 이름을 가진 공통 컬럼을 자동으로 찾아 같은 레코드 값만 조회
    - **inner 조인** : 조인할 때 일치하는 레코드 값만 조회하는 방식
    - **Equi 조인 :** 동등연산자로 조인 (동일한 컬럼 기준으로 조인)
        
        ```sql
        select *
        from emp natural join dept;
        ```
        
    - **필터링**
        
        ```sql
        select *
        from emp natural join dept -- from 절에 조인조건 명시
        where deptno = 30; -- where 절에서 검색조건(필터링) 명시
        ```
        
        → emp와 dept 테이블의 공통 컬럼, 공통 레코드 값 중 deptno가 30인 레코드만 조회 됨.
        
    - **테이블 별칭**
        
        ```sql
        select *
        from emp e natural join dept d;
        ```
        
        <aside>
        💡   from 절에서 테이블 별칭 지정할 수 있음. (as 사용 불가)
        
        </aside>
        
    - **보고싶은 컬럼만 출력되도록 select 절에서 컬럼 지정**
        
        ```sql
        select empno, ename, sal, dname, loc, deptno
        from emp natural join dept;
        ```
        
        ```sql
        select emp.empno, emp.ename, emp.sal, dept.dname, dept.loc, deptno
        from emp natural join dept;
        ```
        
        <aside>
        💡 컬럼 앞에 테이블명 명시 가능하나 공통컬럼은 테이블 명시 불가
        
        </aside>
        
        ```sql
        select e.empno, e.ename, e.sal, d.dname, d.loc, deptno
        from emp e natural join dept d;
        ```
        
        <aside>
        💡 from 절에서 지정한 별칭은 select 절 컬럼명 앞에 명시해 주어야 함.
        공통컬럼은 별칭 명시 불가
        
        </aside>
        
- **join ~ using (공통 컬럼)**
    - **inner 조인** : 조인할 때 일치하는 레코드 값만 조회하는 방식
    - **Equi 조인 :** 동등연산자로 조인 (동일한 컬럼 기준으로 조인)
    
    - **using( 공통컬럼명 )**
        
        ```sql
        select empno, ename, sal, dname, loc, deptno
        from emp join dept using(deptno); -- emp와 dept를 조인할 때 deptno 컬럼을 이용하라.
        ```
        
    
    - **SELECT절 컬럼명 앞에 테이블 명시**
        
        ```sql
        select emp.empno, emp.ename, emp.sal, dept.dname, dept.loc, deptno
        from emp join dept using(deptno);
        ```
        
        <aside>
        💡 → natural join과 마찬가지로 테이블 별칭 지정 가능하나 공통 컬럼에는 지정 불가
        
        </aside>
        
        ```sql
        select e.empno, e.ename, e.sal, d.dname, d.loc, deptno
        from emp e join dept d using(deptno);
        ```
        
        <aside>
        💡 from 절에서 지정한 별칭은 select 절 컬럼명 앞에 명시해 주어야 함. 
        공통컬럼은 테이블 별칭 명시 불가
        
        </aside>
        
    - **검색 조건 추가**
        
        ```sql
        select e.empno, e.ename, e.sal, d.dname, d.loc, deptno
        from emp e join dept d using(deptno) -- 조인조건
        where deptno = 30; -- 검색조건
        ```
        
        → emp와 dept 테이블의 공통 컬럼, 공통 레코드 값 중 deptno가 30인 레코드만 조회 됨.
        
- **join ~ on 조건식**
    - **inner 조인** : 조인할 때 일치하는 레코드 값만 조회하는 방식
    - **Equi 조인 :** 동등연산자로 조인 (동일한 컬럼 기준으로 조인)
    
    - **on 절 뒤에 테이블 명시하여 공통 컬럼 지정**
        
        ```sql
        select empno, ename, sal, dname, loc, emp.deptno
        from emp join dept on emp.deptno = dept.deptno;
        ```
        
        <aside>
        💡 주의 : on 절에 지정한 공통컬럼을 select 절에서 지정할 때 반드시 테이블명을 명시해야 함.
        
        </aside>
        
    
    - **SELECT절 컬럼명 앞에 테이블 명시**
        
        ```sql
        select emp.empno, emp.ename, emp.sal, dept.dname, dept.loc, emp.deptno
        from emp join dept on emp.deptno = dept.deptno;
        ```
        
        <aside>
        💡 다른 join과 다르게 공통 컬럼에도 테이블 명시 가능
        
        </aside>
        
    - **테이블 별칭**
        
        ```sql
        select e.empno, e.ename, e.sal, d.dname, d.loc, e.deptno
        from emp e join dept d on e.deptno = d.deptno;
        ```
        
        <aside>
        💡 테이블 별칭 주려면 컬럼명 앞에도 별칭을 명시해야 함.
        
        </aside>
        
    - **검색조건 지정**
        
        ```sql
        select e.empno, e.ename, e.sal, d.dname, d.loc, e.deptno
        from emp e join dept d on e.deptno = d.deptno -- 조인조건
        where d.DEPTNO = 10; -- 검색조건
        ```
        
        → emp와 dept 테이블의 dept 컬럼에서의 공통 레코드 중 deptno가 10인 레이블만 조회
        

### **Non-Equi 조인**

- 이전까지는 모두 동등연산자(=)로 조인하였지만 (Equi 조인)
- 부등 연산자로 조인하려면 반드시 join ~ on을 사용해야 한다. (Non-Equi 조인)
    
    ```sql
    select *
    from emp join SALGRADE on sal BETWEEN losal and hisal;
    ```
    

- **보고싶은 컬럼만 출력하도록 컬럼 지정**
    
    ```sql
    select empno, ename, sal, grade
    from emp join SALGRADE on sal BETWEEN losal and hisal;
    ```
    
- **테이블 별칭**
    
    ```sql
    select e.empno, e.ename, e.sal, s.grade
    from emp e join salgrade s on e.sal between s.losal and s.hisal;
    ```
    
    <aside>
    💡 컬럼명 앞에도 테이블 별칭 명시해야 함.
    
    </aside>
    

### **3개 테이블 join**

- **join ~ using 으로 조인**
    
    ```sql
    select *
    from emp join dept using(deptno)
    join salgrade on sal BETWEEN losal AND hisal;
    ```
    
    <aside>
    💡 deptno을 공통 컬럼으로 emp와 dept 테이블을 먼저 조인한 후, 
    salgrade와 한번 더 조인한다.
    단, sal이 losal과 hisal 사이 값을 갖는 레코드만 출력한다.
    
    </aside>
    
    - **보고싶은 컬럼만 나오도록 컬럼 지정**
        
        ```sql
        select empno, ename, dname, loc, sal, grade
        from emp join dept using(deptno)
        join salgrade on sal BETWEEN losal AND hisal;
        ```
        
    
- **join ~ on 조건식**
    
    ```sql
    select empno, ename, dname, loc, sal, grade
    from emp join dept on emp.deptno = dept.DEPTNO 
             join salgrade on sal BETWEEN losal AND hisal;
    ```
    

### **self join**

- **inner 조인** : 조인할 때 일치하는 레코드 값만 조회하는 방식
- **용도 :** 담당 관리자가 있는 사원의 리스트인 emp 테이블에서 담당 관리자의 이름을 사번을 통해 알고 싶을 때 (모두 한 테이블 안에서 조회 가능할 때)
    
    ```sql
    select *
    from emp e join emp m on e.mgr = m.empno;
    ```
    
    → emp 테이블(별칭 e) join emp 테이블(별칭 m) & 담당 관리자 컬럼(mgr)의 값과 사번 컬럼(empno)의 값이 같은 레이블 조회
    
- **outer join**
    - 일치하는 레코드 뿐만 아니라 일치하지 않는 레코드까지 포함하여 반환
    
    - **left outer join :** 왼쪽에 있는 컬럼의 모든 레코드를 반환.
        
        ```sql
        select e.empno, e.ename, e.sal, d.dname, d.loc, deptno   
        from emp e left outer join dept d using(deptno);
        ```
        
        <aside>
        💡 공통 레코드가 없는 오른쪽 테이블에는 null 값이 반환 됨.
        
        </aside>
        
    - **right outer join :** 오른쪽에 있는 컬럼의 모든 레코드를 반환.
        
        ```sql
        select e.empno, e.ename, e.sal, d.dname, d.loc, deptno
        from emp e right outer join dept d using(deptno);
        ```
        
        <aside>
        💡 공통 레코드가 없는 왼쪽 테이블에는 null 값이 반환 됨.
        
        </aside>
        
    - **full outer join :** 양쪽 테이블의 모든 레코드를 반환.
        
        ```sql
        select e.empno, e.ename, e.sal, d.dname, d.loc, deptno
        from emp e full outer join dept d using(deptno);
        ```
        
    

## **서브쿼리**

### 개요

- **개념 :** 하나의 SELECT 만으로 원하는 데이터를 조회할 수 없을 때 사용
- 용도 : Smith 사원의 sal 보다 많은 사원 조회할 때
    
    → 먼저 Smith 사원의 sal을 조회한 후, 그 보다 많은 sal의 사원을 조회해야 함.
    

### **종류**

![Untitled](SQL_Oracle%201e0ac134fb854b04a63931f1010100ed/Untitled%2027.png)

### **단일행 서브쿼리**

- **where 절 서브쿼리**
    
    ```sql
    select empno, ename, job, sal
    from emp
    where sal > ( select sal
    							from emp
    							where ename ='WARD');
    ```
    
    → ename이 ‘WARD’인 사원의 sal 보다 큰 sal인 사원의 empno, ename, job, sal을 조회하라.
    

- **그룹함수 이용**
    
    ```sql
    select empno, ename, job, sal
    from emp
    where sal > ( select avg(sal)
    							from emp );
    ```
    
    → 평균 sal 보다 큰 sal인 사원의 empno, ename, job, sal을 조회하라.
    

### **복수행 서브쿼리**

- **IN 연산자 이용**
    
    ```sql
    select empno, ename, job, sal
    from emp
    where sal IN ( select MIN(sal)
    							from emp
    							Group by job );
    ```
    
    → 업무별 최소 급여를 받는 사원 조회 (업무별 최소 급여는 값이 여러개임)
    
- **ALL 연산자 이용**
    
    ```sql
    select empno, ename, job, sal
    from emp
    where sal < ALL ( select sal
    						from emp
    						where job = 'MANAGER');
    ```
    
    → 업무가 MANAGER인 사원의 최소 급여보다 적은 급여를 받는 사원 조회
    
    <aside>
    💡  < ALL : “<”를 모두 만족할 레코드만 반환 
    ⇒ 서브쿼리의 실행 결과 중 최소값보다 작은 값을 가진 레코드 반환
    
    </aside>
    
    ```sql
    select empno, ename, job, sal
    from emp
    where sal > ALL ( select sal
    						from emp
    						where job = 'MANAGER');
    ```
    
    → 업무가 MANAGER인 사원의 최대 급여보다 많은 급여를 받는 사원 조회
    
    <aside>
    💡  >ALL : “>”를 모두 만족할 레코드 반환 
    ⇒ 서브쿼리의 실행 결과 중 최대값보다 큰 값을 가진 레코드 반환
    
    </aside>
    
- **ANY 연산자 이용**
    
    ```sql
    select empno, ename, job, sal
    from emp
    where sal < ANY ( select sal
    									from emp
    									where job = 'MANAGER');
    ```
    
    → 업무가 MANAGER인 사원의 최대 급여보다 적은 급여를 받는 사원 조회
    
    <aside>
    💡 <ANY : “<”를 적어도 하나만 만족하는 레코드 반환 
    ⇒ 서브쿼리의 실행 결과 중 최대값보다 작은 값을 가진 레코드 반환
    
    </aside>
    
    ```sql
    select empno, ename, job, sal
    from emp
    where sal > ANY ( select sal
    						from emp
    						where job = 'MANAGER');
    ```
    
    → 업무가 MANAGER인 사원의 최소 급여보다 많은 급여를 받는 사원 조회
    
    <aside>
    💡 >ANY : “>”를 적어도 하나만 만족하는 레코드 반환 
    ⇒ 서브쿼리의 실행 결과 중 최소값보다 작은 값을 가진 레코드 반환
    
    </aside>
    

### EXISTS

서브쿼리 실행 후 반환되는 레코드 유무에 따라 메인쿼리의 실행 여부가 결정 됨.

```sql
select *
from emp
where EXISTS (select empno
							from emp
							where comm is not null );
```

→ 서브쿼리의 결과 값이 존재하는 경우 ⇒ 메인쿼리 실행 (where 절 조건과 상관 없음)

```sql
select *
from emp
where EXISTS ( select empno
from emp
where ename is null );
```

→ 서브쿼리의 결과 값이 존재하지 않는 경우 ⇒ 결과값 없음

## **DML**

### 개요

- **개념 :** Data Manipulation Language
데이터베이스의 테이블에 새로운 **데이터를 저장(INSERT)**하거나 **삭제(DELETE)** 또는 **수정(UPDATAE)** 및 **병합(MERGE)**할 때 사용하는 데이터 조작어
- **특징**
    - 실제 물리적인 파일에는 반영되지 않는다. only 메모리에만 저장됨.
    - 메모리에 반영된 모든 DML문이 모두 성공하면 트랜잭션으로 실제 물리적 파일에 반영해야 한다. ⇒ commit (실제 물리적 파일에서 실패 시 수정하는 것 쉽지 않음.)
    - DML문 중 하나라도 실패 시 이전 commit 실행 전까지의 DML문을  모두 취소하려면 ⇒ rollback
    - Maria DB)  내부적으로 자동 commit 이므로 물리적 파일에 바로 반영 됨. but 자동 commit 비활성화 가능

### **INSERT : 새로운 레코드 생성**

- **단일 생성 :** 하나의 레코드 생성
    
    ⭐특징⭐
    
    저장되는 데이터의 타입은 컬럼 데이터와 같아야 한다.
    
    입력되는 데이터의 크기는 지정된 컬럼의 크기보다 작아야 한다.
    
    Primary Key 또는 Unique로 지정된 컬럼은 기존의 동일한 값을 저장할 수 없다.
    
    into 절에서 생략된 컬럼에는 자동으로 null 값이 저장된다. ⇒ not null 제약 조건이 아닌 컬럼만 into 절에서 생략 가능
    
    - **컬럼명 명시**
        
        ```sql
        insert into dept(deptno, dname, loc )
        values ( 50, '개발', '서울');
        ```
        
        → dept 테이블의 컬럼 deptno에는 50이, dname에는 ‘개발’이,  loc에는 ‘서울’이 저장됨.
        
        ```sql
        insert into dept(deptno, dname )
        values ( 60, '개발');
        ```
        
        <aside>
        💡 dept 테이블에는 이미 loc 컬럼이 있는 상태에서 loc 컬럼을 제외한 나머지 컬럼에만 레이블 값이 부여되었다.
        ⇒ loc 컬럼의 레이블에는 자동으로 null 값이 저장됨.
        
        </aside>
        
    - **컬럼명 생략**
        
        ```sql
        insert into dept
        values ( 51, '개발', '서울');
        ```
        
        → 모든 컬럼명이 생략되는 경우도 있음.
        
- **멀티 생성 (CTAS) :** 기존 테이블을 이용하여 새로운 테이블 생성
    
    ⭐특징⭐
    
    CTAS는 not null을 제외한 제약조건이 복사되지 않음.
    
    creat는 DDL 문이고 DDL은 자동으로 commit 됨.
    
    - **레코드까지 포함하여 생성**
        
        ```sql
        create table copy_dept
        as
        select * from dept;
        ```
        
    - **기존 테이블의 구조만 복사하여 생성**
        
        ```sql
        create table copy_dept2
        as
        select * from dept
        where 1=2;
        ```
        
        → where 절의 조건을 FALSE로 지정하여 레코드 값은 복사되지 않도록 함.
        
    - **insert ~ select 문을 이용하여 하나의 insert 이용하여 멀티 레코드 생성**
        
        ```sql
        insert into copy_dept2
        select deptno, dname, loc
        from dept;
        ```
        

### **UPDATE : 테이블에 저장된 데이터를 수정**

- **특정 레코드만 수정**
    
    ```sql
    update dept
    set dname ='인사', loc='제주'
    where deptno = 50;
    ```
    
     → deptno가 50인 레코드의 dname은 인사로 loc는 제주로 수정됨.
    
- **모든 레코드 수정**
    
    ```sql
    update dept
    set dname ='인사', loc='제주';
    ```
    
    → dname의 모든 레코드는 인사로, loc의 모든 레코드는 제주로 수정됨.
    
- **update + sub query**
    
    다른 테이블에 저장된 데이터를 사용하여 특정 컬럼값 변경이 가능하다.
    
    ```sql
    update dept
    set dname = (select dname from dept where deptno=10),
    loc = (select loc from dept where deptno=20)
    where deptno = 50;
    ```
    
    → deptno가 50인 레코드만 수정
     수정 내용 : dname의 레코드 값은 deptno가 10인 dname과 같도록 수정 & loc의 레코드 값은 deptno가 20인 loc와 같도록 수정
    

### **DELETE : 테이블에 저장된 데이터를 삭제**

- **특정 레코드만 삭제**
    
    ```sql
    delete from dept
    where deptno = 50;
    ```
    
    → deptno 가 50인 레코드 값들을 삭제
    
    <aside>
    💡 만약 deptno = 50의 레코드를 참조하는 다른 테이블이 있다면 삭제 불가
    (무결성 제약조건에 위배)
    
    </aside>
    
- **모든 레코드 삭제**
    
    ```sql
    delete from emp;
    ```
    
- **delete + subquery**
    
    ```sql
    delete from dept
    where deptno in (select deptno from dept where dname = '개발');
    commit;
    ```
    
    → dname이 개발인 레코드 값을 가진 deptno와 같은 값의 레코드 행 삭제
    

## **DDL**

### 개요

- **개념 :** 데이터베이스의 구조를 생성하거나 수정 및 삭제하는데
사용되는 SQL문
- **특징**
    - 자동으로 commit 되어 데이터베이스 실제 물리 파일에 저장된다.
    - 오라클 객체를 생성하거나 수정 및 삭제하기 위해 사용된다.
- **오라클 객체**
    
    ![Untitled](SQL_Oracle%201e0ac134fb854b04a63931f1010100ed/Untitled%2028.png)
    
- **DDL문 종류**
    
    ![Untitled](SQL_Oracle%201e0ac134fb854b04a63931f1010100ed/Untitled%2029.png)
    

### CREATE : **테이블 생성**

- 무결성 보장이 안됨.

```sql
create table dept_2
( deptno number(2), -- 0~99까지 저장 가능
dname varchar2(10), -- 영문 10글자, 한글 5글자 저장 가능
loc varchar2(10));
```

![Untitled](SQL_Oracle%201e0ac134fb854b04a63931f1010100ed/Untitled%2030.png)

- **default 값 지정**
    
    ```sql
    create table dept_3
    ( deptno number(2),
    dname varchar2(10),
    loc varchar2(10) default '서울');
    ```
    
    ```sql
    insert into dept_3(deptno,dname)
    values ( 1, '개발'); -- loc 컬럼, 값 지정 안해도 default 값이 '서울'이 저장됨.
    select * from dept_3;
    ```
    
    → 테이블 생성 후 레이블 값 insert 할 때, values에 값을 입력하지 않아도 테이블 생성 시 default 값 지정했다면 레이블에 default 값이 들어간다.
    
    ![Untitled](SQL_Oracle%201e0ac134fb854b04a63931f1010100ed/Untitled%2031.png)
    
    ```sql
    create table dept_3_1
    ( deptno number(2),
    dname varchar2(10),
    loc varchar2(10) default '서울',
    writeday date default sysdate);
    ```
    
    ![Untitled](SQL_Oracle%201e0ac134fb854b04a63931f1010100ed/Untitled%2032.png)
    
- **제약조건 지정**
    - **primary key**
        1. **컬럼 레벨**
        - **제약조건 이름 지정 방식 (제약조건 삭제, 비활성화 시킬 때 용이)**
            
            create table 테이블명
            
            (컬럼명 데이터형태 constraint 제약조건명 제약조건타입);
            
            ```sql
            create table table1
            ( no number(2) constraint table1_no_pk PRIMARY KEY,
            email varchar2(20));
            ```
            
            <aside>
            💡 이처럼 PK로 지정한 컬럼의 레이블 값으로는 중복 값과 null 값이 없어야 하므로 데이터 입력 시 주의해야 함.
            
            </aside>
            
        - **제약조건 이름 미지정 방식**
            
            ```sql
            create table table1_1
            ( no number(2) PRIMARY KEY,
            email varchar2(20));
            ```
            
            → 제약조건 이름은 자동 부여되나 나중에 비활성화하거나 삭제할 때 컬럼 식별이 어려움
            
        
        **b. 테이블 레벨 (컬럼을 모두 지정하고 나서 나중에 제약조건 지정)**
        
        ```sql
        create table table2
        ( no number(2),
        email varchar2(20),
        constraint table2_no_pk PRIMARY KEY(no)
        );
        ```
        
        → constraint 제약조건명 제약조건타입(지정할 컬럼명)
        
        지정할 컬럼명 명시해 주어야 함.
        
        **c. 복합컬럼 (두 개의 컬럼에 동시에 제약조건 지정)**
        
        ```sql
        create table table2_1
        ( no number(2),
        email varchar2(20),
        address varchar2(20),
        constraint table2_1_no_pk PRIMARY KEY(no, email)
        );
        ```
        
        → 지정할 컬럼명에 두 개의 컬럼명 명시
        
    - **unique**
        1. **컬럼 레벨**
            
            ```sql
            create table table3
            ( no number(2) constraint table3_no_uk UNIQUE,
            email varchar2(20));
            ```
            
            <aside>
            💡 PK와 마찬가지로 UK 제약조건으로 지정한 컬럼의 레이블 값에는 중복값이 없어야 한다. 그러나 null 값은 저장 가능하다.
            
            </aside>
            
        2. **테이블 레벨**
            
            ```sql
            create table table4
            ( no number(2),
            email varchar2(20),
            constraint table4_no_uk UNIQUE(no)
            );
            ```
            
        3. **복합 컬럼**
            
            ```sql
            create table table4_1
            ( no number(2),
            email varchar2(20),
            address varchar2(20),
            constraint table4_1_no_pk UNIQUE(no, email)
            );
            ```
            
    - **not null**
        1. **컬럼 레벨**
            
            ```sql
            create table table7
            ( no number(2) constraint table7_no_nn NOT NULL,
            email varchar2(20));
            ```
            
        2. **테이블 레벨 : 지원 안됨**
    - **check**
        1. **컬럼 레벨**
            
            ```sql
            create table table5
            ( no number(2) constraint table5_no_ck CHECK(no in (10,20)),
            email varchar2(20));
            ```
            
            <aside>
            💡 제약조건타입 check 뒤에 레이블 값 범위 지정해 주어야 함.
            지정한 범위 외 다른 값은 레이블 값으로 저장할 수 없다.
            
            </aside>
            
        2. **테이블 레벨**
            
            ```sql
            create table table6
            ( no number(2),
            email varchar2(20),
            constraint table6_no_ck CHECK(no > =20));
            ```
            
    - **foreign key**
        1. **컬럼 레벨**
        - **master 테이블 생성 (primary key)**
            
            ```sql
            create table master1
            (num number(2) constraint master1_num_pk primary key,
            email varchar2(10));
            ```
            
            ```sql
            insert into master1 ( num, email ) values (1, 'aa1');
            insert into master1 ( num, email ) values (2, 'aa2');
            insert into master1 ( num, email ) values (3, 'aa3');
            ```
            
            → master 테이블에는 PK 지정해 줌.
            
        - **slave 테이블 생성**
            
            ```sql
            create table slave1
            ( no number(2) constraint slave1_no_pk primary key,
            name varchar2(10),
            num number(2) constraint slave1_num_fk REFERENCES master1(num)
            );
            ```
            
            ```sql
            insert into slave1 ( no, name, num ) values (10, 'xxx1', 1 );
            insert into slave1 ( no, name, num ) values (20, 'xxx2', 2 );
            insert into slave1 ( no, name, num ) values (30, 'xxx3', 3 );
            insert into slave1 ( no, name, num ) values (40, 'xxx4', 4 ); -- 에러 (마스터 PK에 해당하지 않는 값)
            insert into slave1 ( no, name, num ) values (50, 'xxx5', null ); -- 마스터 PK 값 외 null 값도 가능
            commit;
            ```
            
            <aside>
            💡 → slave 테이블에는 FK 제약조건을 지정해 준다. 
            (master 테이블에서 참조할 컬럼 명시 필요)
            
            </aside>
            
            <aside>
            💡 ⭐ FK 제약조건을 지정한 컬럼에는 master 테이블 PK 컬럼에 있는 값들만 저장 가능하다. 또는 null 값 저장이 가능하다.
            
            </aside>
            
        
        **b. 테이블 레벨**
        
        - **slave 테이블 작성**
            
            ```sql
            create table slave2
            ( no number(2) constraint slave2_no_pk primary key,
            name varchar2(10),
            num number(2),
            constraint slave2_num_fk FOREIGN KEY (num) REFERENCES master1(num)
            );
            ```
            
            ```sql
            insert into slave2 ( no, name, num ) values (10, 'xxx1', 1 );
            insert into slave2 ( no, name, num ) values (20, 'xxx2', 2 );
            insert into slave2 ( no, name, num ) values (30, 'xxx3', 3 );
            insert into slave2 ( no, name, num ) values (40, 'xxx4', 4 ); -- 에러 (마스터 PK에 해당하지 않는 값)
            insert into slave2 ( no, name, num ) values (50, 'xxx5', null ); -- 마스터 PK 값 외 null 값도 가능
            commit;
            ```
            
        
        ⭐주의⭐
        만약 master 테이블의 PK 컬럼 중 1 값을 가진 레이블 행을 삭제하려면?
        (단, 이 값은 slave 테이블이 참조하고 있다.)
        
        **해결 1) on delete cascade :** master PK 레코드 삭제하기 위해 slave FK 레이블을 먼저 삭제하게 함.
        
        ```sql
        create table slave1
        ( no number(2) constraint slave1_no_pk primary key,
        name varchar2(10),
        num number(2) constraint slave1_num_fk REFERENCES master1(num) ON DELETE CASCADE
        );
        ```
        
        → FK 제약조건 지정 시 뒤에 ON DELETE CASCADE를 명시해줌.
        
        **해결 2) on delete set null :** master PK 레코드 삭제하기 위해 slave FK 레이블 값을 null 값으로 변환한다.
        
        ```sql
        create table slave2
        ( no number(2) constraint slave2_no_pk primary key,
        name varchar2(10),
        num number(2),
        constraint slave2_num_fk FOREIGN KEY (num) REFERENCES master1(num) on delete set null
        );
        ```
        
        → FK 제약조건 지정 시 뒤에 on delete set null 를 명시해줌.
        
        ⭐Foreign Key 특징⭐
        
        1. Master 테이블의 레코드는 마음대로 삭제 불가
            
            (참조하고 있는 slave 테이블 FK 컬럼이 있기 때문)
            
            → 해결 1) on delete cascode : Master PK 레코드 삭제 시 Slave FK의 레코드 먼저 삭제
            
            → 해결 2) on delete set null : Master PK 레코드 삭제 시 Slave FK의 레코드 값을 null로 변환
            
        2. Master의 테이블 삭제(drop) 불가
            
            → 해결) drop table slave cascade constraints : Slave의 FK 제약조건 삭제
            
            ```sql
            drop table master1 CASCADE constraints;
            ```
            
            → Slave가 참조하고 있는 Master 테이블을 명시해야 함.
            
        3. Master의 PK 제약조건 삭제 불가
        

### DELETE : **테이블 절삭 (레코드 삭제하기)**

- **DML로 레코드 삭제 예시**
    
    ```sql
    delete from copy_dept;
    ```
    
    → copy_dept의 7개의 레코드 값이 삭제 됨. (rollback으로 복구 가능)
    
- **DDL로 레코드 삭제 (truncate)**
    
    ```sql
    truncate table copy_dept;
    ```
    
    → copy_dept의 7개의 레코드 값이 삭제 됨. (rollback으로 복구 불가)
    

### ALTER : **DDL 수정 및 삭제**

- **컬럼 추가 (alter table ~ add)**
    
    ```sql
    alter table my_dept
    add ( email varchar2(20), aaddr varchar2(10));
    ```
    
- **데이터 타입 변경 (alter table ~ modify)**
    
    ```sql
    alter table my_dept
    modify ( tel number(10));
    ```
    
    → number()을 varchar2()로 변경하는 것 가능하나 단, 값이 없을 때만 가능
    
    → 데이터 크기를 더 작게 변경 가능하나 단, 값이 없을 때만 가능
    
    number(4) → number(8) : 가능 / number(8) → number(4) : 값이 없을 때만 가능
    
- **컬럼 삭제 (alter table ~ drop)**
    
    ```sql
    alter table my_dept
    drop ( tel );
    ```
    
- **제약조건 추가 (alter table ~ add / alter table ~ modify)**
    
    ```sql
    alter table my_dept
    add constraint my_dept_deptno_pk PRIMARY KEY(deptno);
    ```
    
    ```sql
    alter table my_dept
    add constraint my_dept_dname_uk UNIQUE(dname);
    ```
    
    → 테이블 레벨 문법과 동일
    
    ```sql
    alter table my_dept
    modify ( loc varchar2(13) constraint my_dept_loc_nn not null);
    ```
    
    <aside>
    💡 not null 제약조건은 테이블 레벨 문법이 없음. 
    따라서 add가 아닌 modify를 사용하여 not null 제약조건을 추가해야 함.
    
    </aside>
    
- **제약조건 삭제 (drop constraint)**
    
    ```sql
    alter table my_dept
    drop primary key;
    ```
    
    → PK 제약조건은 테이블 당 한개이므로 제약조건명을 이용하지 않아도 됨.
    
    ```sql
    alter table my_dept
    drop CONSTRAINT MY_DEPT_DNAME_UK;
    ```
    
    → PK 외 다른 제약조건들은 지정했던 제약조건명 이용
    
    ⭐주의⭐ slave에서 master의 PK를 참조하고 있을 때 master PK 제약조건을 삭제하는 법
    
    ```sql
    alter table MASTER1
    drop primary key CASCADE;
    ```
    
    → 참조되고 있는 master 테이블의 PK 제약조건 뒤에 CASCADE 붙여서 PK를 참조하는 모든 FK를 먼저 삭제한다.
    

### 테이블 삭제 (drop table)

```sql
DROP TABLE my_dept CASCADE constraints;
```