# **Git / GitHub**

## Git 이란?
 * 분산버전관리시스템(DVCS)
 * 로컬에서의 버전 기록, 관리
 * 원격 저장소를 활용하여 협업

 ## Git 버전 관리 기초
 1. 작업하고
 2. 변경된 파일을 모아 (add)
 3. 버전으로 남긴다. (commit)
---
 ## Git에서의 버전 관리 실습
 1. VSC - Terminal - git bash
 2. git 저장소 초기화
    ```git
    git init
    ```
3. 텍스트 파일 생성
    ``` git
    touch a.txt
    ```
4. 텍스트 파일에 내용 입력 후 저장
5. 현재 git 저장소의 상태 확인
    
    ```git
    git status
    ```
    `*`변경된 파일, 스테이징된 파일 등의 정보 확인 가능

6. 현재 디렉토리의 변경된 파일을 스테이징 영역에 추가
    ```git
    # 한개 파일만
    git add a.txt
    ```
    ```git
    # 디렉토리의 모든 파일
    git add .
    ```
    ```git
    # 여러개의 파일
    git add a.txt b.txt c.txt
7. 스테이징 영역의 파일을 커밋하여 버전 기록
    ```git
    git commit -m '커밋이름'
8. 현재까지 커밋된 히스토리 확인
    ```git
    git log
    ```