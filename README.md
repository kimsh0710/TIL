# **Git / GitHub**

## Git 개요
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
    `-> 변경된 파일, 스테이징된 파일 등의 정보 확인 가능`
    
    `-> untracked file : 한번도 버전 관리되지 않은 파일 -> staging area에만 있는 상태`


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
    ```
    `-> change not staged for commit : 변경 사항 있었지만 스테이징 되지 않음 -> stage area에만 있는 상태`
7. 스테이징 영역의 파일을 커밋하여 버전 기록
    ```git
    git commit -m '커밋이름'
    ```
    `-> nothing to commit, working tree clean : commit까지 했지만 변경 사항 없음 -> staging, repository area 둘 다 존재 X`

8. 현재까지 커밋된 히스토리 확인
    ```git
    git log
    ```

---
## GitHub로 push 실습
1. GitHub에서 repository 생성
2. 생성한 repository url 주소를 origin에 지정
    ```git
    git remote add origin https://github.com/kimsh0710/TIL.git
    ```
    `-> origin : GitHub 기본 원격저장소`

3. 원격저장소로 push
    ```git
    git push origin main
    ```
4. GitHub에 저장되었는지 확인


---
## 이 외 참고할 명령어
1. 원격저장소 목록 확인
    ```git
    git remote -v
    ```

2. 지정한 원격저장소(origin) 삭제
    ```git
    git remote rm origin
    ```

3. add 실행 취소 하고 싶을 때
    ```git
    restore
    ```
---
## 이슈 해결
❗이슈 : Git Repository에 있었던 프로젝트를 다 지워버리고 새로운 프로젝트를 push하려고 할 때

    
    ! [rejected] master -> master (fetch first) error: failed to push some refs to 'https://github.com/xxx/test.git'
    

💡해결

    
    git push origin +master  



❗이슈 : 로컬폴더 01.SQL를 git init한 상태에서 01.SQL의 하위 폴더인 Oracle폴더의 하위 폴더인 Oracle_workshop폴더를 add 하고 싶을 때 


💡해결

    
    git add Oracle/Oracle_workshop

    


