import pandas as pd
import numpy as np

'''
   데이터 프레임 병합
     pandas는 두개 이상의 데이터 프레임을 하나로 합치는
     병합(merge)이나 연결(concate)을 지원한다.
   merge 명령을 사용한 데이터 프레임 병합
     merge :
     두개의 데이터 프레임의 공통 열 이나 인덱스를 기준으로
     두개의 데이터프레임을 합친다.
     이때 기준이되는 열 데이터를 key라고 부른다.
   형식
     df.merge(df1) : 두 df를 병합시켜 준다.
     기본은 inner join : 양쪽에 동일하게 존재하는 키만 표시
     key : 기준열을 의미
     실제 데이터 필드거나 행 인덱스 일 수 있다.
     병합방식
     inner join : 양쪽 df에서 모두 키가 존재하는 data만표시
     outer join : 한쪽에만 키가 존재하면 data를 표시
     병합방식을 설정 : how=inner(생략가능), how=outer
'''

#예시 df 생성 - 고객 정보를 담고 있는 df

df1 =pd.DataFrame({
 '고객번호' : [1001,1002,1003,1004,1005,1006,1007],
 '이름' : ['둘리','도우너','또치','길동','희동','마이콜','영희']
 },
 columns=['고객번호','이름'])
print(df1)
'''
   고객번호   이름
0  1001   둘리
1  1002  도우너
2  1003   또치
3  1004   길동
4  1005   희동
5  1006  마이콜
6  1007   영희
'''

#예제 df 생성 - 예금 정보 df
df2 = pd.DataFrame({
 '고객번호':[1001,1001,1005,1006,1008,1001],
 '금액' : [10000,20000,15000,5000,100000,30000]
},columns=['고객번호','금액'])
print(df2)
'''
   고객번호      금액
0  1001   10000
1  1001   20000
2  1005   15000
3  1006    5000
4  1008  100000
5  1001   30000
'''

'''
   merge 명령으로 두 df를 병합하는 문법
     모든 인수 생략(병합 df를 제외한) 공통 이름을 갖고 있는 열
     '고객번호'가 키가 됨
     양쪽에 모두 존재하는 키의 data만 보여주는 inner join 방식을 사용
'''

# 두 df의 공통열(같은 이름을 갖는 컬럼) : 고객번호
print(df1.merge(df2)) #key= 생랼하면 공통열을 기준으로 inner join 실행
'''
   고객번호   이름     금액
0  1001   둘리  10000
1  1001   둘리  20000
2  1001   둘리  30000
3  1005   희동  15000
4  1006  마이콜   5000
'''

'''
   outer join 방식은 키 값이 한쪽에만 있어도 데이터를 보여 줌
     pd.merge(df1,df2, how = 'outer')
     어느 한 df에 데이터가 존재하지 않으면 NaN으로 표시됨
     
     how = inner/outer/left/right
     how=left : 왼쪽 df에 있는 모든 키의 데이터는 표시
     how=right : 오른쪽 df 에 있는 모든 키의 데이터는 표시
'''
# outer join : 키 값이 한쪽에만 있어도 데이터를 출력
print(pd.merge(df1,df2,how='outer')) # 공통열인 고객번호를 기준열로 병합 진행
'''
   고객번호   이름        금액
0  1001   둘리   10000.0
1  1001   둘리   20000.0
2  1001   둘리   30000.0
3  1002  도우너       NaN
4  1003   또치       NaN
5  1004   길동       NaN
6  1005   희동   15000.0
7  1006  마이콜    5000.0
8  1007   영희       NaN
9  1008  NaN  100000.0
'''

print(pd.merge(df1,df2,how='left'))
'''
   고객번호   이름       금액
0  1001   둘리  10000.0
1  1001   둘리  20000.0
2  1001   둘리  30000.0
3  1002  도우너      NaN
4  1003   또치      NaN
5  1004   길동      NaN
6  1005   희동  15000.0
7  1006  마이콜   5000.0
8  1007   영희      NaN
'''

print(pd.merge(df1,df2,how='right'))
'''
   고객번호   이름      금액
0  1001   둘리   10000
1  1001   둘리   20000
2  1005   희동   15000
3  1006  마이콜    5000
4  1008  NaN  100000
5  1001   둘리   30000
'''

'''
   동일한 키 값이 있는 경우
   키값이 같은 데이터가 여러개 있는 경우에는 있을 수 있는 모든 경우의 수를 따져서 조합을 만들어 낸다.
'''

#예제 df 생성
#열: 품종, 꽃잎길이
df1 = pd.DataFrame({
 '품종':['setosa','setosa','virginica','virginica'],
 '꽃잎길이':[1.4,1.3,1.5,1.3]
}, columns=['품종','꽃잎길이'])

print(df1)
'''
          품종  꽃잎길이
0     setosa   1.4
1     setosa   1.3
2  virginica   1.5
3  virginica   1.3
'''

#열 : 품종, 꽃잎너비
df2 = pd.DataFrame({
 '품종': ['setosa','virginica','virginica','ersicolor'],
 '꽃잎너비':[0.4,0.3,0.5,0.3]
},columns=['품종','꽃잎너비'])

print(df2)
'''
          품종  꽃잎너비
0     setosa   0.4
1  virginica   0.3
2  virginica   0.5
3  ersicolor   0.3
'''

'''
  df1과 df2 를 병합
   - 위 데이터에서 키 값 setosa에 대해
   - df1에는 1.4와 1.3 2개의 데이터가 있고
   - df2에는 0.4라는 1개의 데이터가 있으므로
   - 병합 데이터에는 setosa가 (1.4,0.4)(1.3,0.4)의 2 경우가 표현된다.
   - 키값 virginica의 경우에는 df1에 2개 df2에 2개의 데이터가 있으므로
   - 2개와 2개의 조합에 의해 4개의 데이터가 표현된다
'''

print(pd.merge(df1,df2))
'''
          품종  꽃잎길이  꽃잎너비
0     setosa   1.4   0.4        <- 동일한 key값 setosa를 기준으로 꽃잎너비가 두번 중복되어 병합됨.
1     setosa   1.3   0.4
2  virginica   1.5   0.3
3  virginica   1.5   0.5
4  virginica   1.3   0.3
5  virginica   1.3   0.5
'''

'''
   key
    두 데이터 프레임에서 이름이 같은 열은 모두 키가 될 수 있다.
    이름이 같아도 키가되면 안되는 열이 있으면 on 인수로 기준열을 명시해야 한다.
    
   기준열을 직접 지정 : on=기준열 이름
    반환 결과에 동일 필드명이 있을경우에는 필드명_x, 필드명_y로 필드명을 변경해서 표현한다.
'''

# 예제 df
df1 = pd.DataFrame({
 '고객명':['춘향','춘향','몽룡'],
 '날짜' : ['2018-01-01','2018-01-02','2018-01-01'],
 '데이터':[20000,30000,100000]
})
print(df1)
'''
 고객명          날짜     데이터
0  춘향  2018-01-01   20000
1  춘향  2018-01-02   30000
2  몽룡  2018-01-01  100000
'''

df2 = pd.DataFrame({
 '고객명':['춘향','몽룡'],
 '데이터':['여자','남자']
})
print(df2)
'''
  고객명 데이터
0  춘향  여자
1  몽룡  남자
'''

# 기준열을 직접 지정
# 반환 결과에 동일 필드명이 있을 경우 필드명_x, 필드명_y로 표현되어짐
print(pd.merge(df1,df2, on='고객명')) # inner
'''
  고객명          날짜   데이터_x 데이터_y
0  춘향  2018-01-01   20000    여자
1  춘향  2018-01-02   30000    여자
2  몽룡  2018-01-01  100000    남자
'''

print(df1.merge(df2, on='고객명',how='outer')) # outer
'''
 고객명          날짜   데이터_x 데이터_y
0  춘향  2018-01-01   20000    여자
1  춘향  2018-01-02   30000    여자
2  몽룡  2018-01-01  100000    남자
'''

'''
   같은 이름의 열이 없는 경우
    키가 되는 기준열이 두 데이터 프레임에서 다르게 나타나면
    left_on, right_on 인수를 사용해서 기준열을 명시해야 함
'''

df1=pd.DataFrame({
 '이름' :['영희','철수','철수'],
 '성적' :[90,80,80]
})
df2 = pd.DataFrame({
 '성명' :['영희','영희','철수'],
 '성적2':[100,80,90]
})

print(df1)
print(df2)
'''
   이름  성적 <- 같은 이름의 컬럼이 없음
0  영희  90
1  철수  80
2  철수  80

   성명  성적2 <- 같은 이름의 컬럼이 없음
0  영희  100
1  영희   80
2  철수   90
'''

# 양쪽 df의 기준이 되는 열의 이름이 다름
print(pd.merge(df1,df2, left_on='이름', right_on='성명'))
# 출력 결과는 양쪽 필드명이 다르기 때문에 기준열로 설정한 두 필드 모두 반환
'''
   이름  성적  성명  성적2
0  영희  90  영희  100
1  영희  90  영희   80
2  철수  80  철수   90
3  철수  80  철수   90
'''

'''
   일반 데이터 열이 아닌 인덱스를 기준으로 merge 할 수 도 있음
     인덱스를 기준열로 사용하려면
     left_index = True 또는
     right_index = True 설정을 하게 됨
'''

df1 = pd.DataFrame({
 '도시': ['서울','서울','서울','부산','부산'],
 '연도': [2000,2005,2010,2000,2005],
 '인구':[9853972,9762546,9631482,3655437,3512547]
})
df2=pd.DataFrame(
 np.arange(12).reshape((6,2)),
 index=[['부산','부산','서울','서울','서울','서울'],
 [2000,2005,2000,2005,2010,2015]],
 columns=['데이터1','데이터2']
)
print(df1)
print(df2)
'''
   도시    연도       인구
0  서울  2000  9853972
1  서울  2005  9762546
2  서울  2010  9631482
3  부산  2000  3655437
4  부산  2005  3512547

         데이터1  데이터2
부산 2000     0     1
    2005     2     3
서울 2000     4     5
    2005     6     7
    2010     8     9
    2015    10    11
'''

print(pd.merge(df1,df2,left_on=['도시','연도'],right_index=True))
'''
   * df1의 도시, 연도 컬럼과 df2의 인덱스를 기준으로 병합됨.
   도시    연도       인구  데이터1  데이터2
0  서울  2000  9853972     4     5
1  서울  2005  9762546     6     7
2  서울  2010  9631482     8     9
3  부산  2000  3655437     0     1
4  부산  2005  3512547     2     3
'''

# 양쪽 데이터프레임에 key가 모두 인덱스 인 경우

df1 = pd.DataFrame(
[[1.,2.],[3.,4.],[5.,6.]],
index=['a','c','e'],
columns=['서울','부산'])
df1
df2=pd.DataFrame(
[[7.,8.],[9.,10.],[11.,12.],[13.,14.]],
 index=['b','c','d','e'],
columns=['대구','광주'])

print(df1)
print(df2)
'''
    서울   부산
a   1.0  2.0
c   3.0  4.0
e   5.0  6.0

    대구    광주
b    7.0   8.0
c    9.0  10.0
d   11.0  12.0
e   13.0  14.0
'''

print(pd.merge(df1, df2, left_index=True, right_index=True, how='outer'))
'''
    서울   부산    대구    광주
a  1.0  2.0   NaN   NaN
b  NaN  NaN   7.0   8.0
c  3.0  4.0   9.0  10.0
d  NaN  NaN  11.0  12.0
e  5.0  6.0  13.0  14.0
'''

# merge 명령어 대신 join 메서드 사용 가능
print(df1.join(df2,how='outer'))
'''
    서울   부산    대구    광주
a  1.0  2.0   NaN   NaN
b  NaN  NaN   7.0   8.0
c  3.0  4.0   9.0  10.0
d  NaN  NaN  11.0  12.0
e  5.0  6.0  13.0  14.0
'''