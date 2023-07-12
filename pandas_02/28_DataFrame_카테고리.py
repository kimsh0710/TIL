import pandas as pd
import numpy as np

'''
    데이터값을 카테고리 값으로 변환

        값의 크기를 기준으로하여 카테고리 값으로 변환하고 싶을때
        cut(data,bins,labels)
        data : 구간 나눌 실제 값,
        bins : 구간 경계값
        labels: 카테고리값
        qcut(data,구간수,labels)
'''

#구간을 나눌 실제 값 : 관측 데이터
ages=[0,0.5,4,6,4,5,2,10,21,23,37,15,38,31,61,20,41,31,100]

# data : 구간 나눌 실제 값
data = ages

# bins : 구간 경계값
# 구간 최소값 < 구간 <= 구간 최대값
bins = [0,4,18,25,35,60,100] # 영유아 : 0살 < 영유아 <=4

# label: 카테고리값(각 구간의 이름)
# 순서는 구간(bins)의 순서와 동일해야 함
labels = ['영유아','미성년자','청년','중년','장년','노년']

print(len(data)) #19
cats = pd.cut(data,bins,labels=labels)
print(cats)
'''
[NaN, '영유아', '영유아', '미성년자', '영유아', ..., '노년', '청년', '장년', '중년', '노년']
Length: 19
Categories (6, object): ['영유아' < '미성년자' < '청년' < '중년' < '장년' < '노년']
'''
print(type(cats)) # <class 'pandas.core.arrays.categorical.Categorical'>

cat_list = list(cats) # 리스트로 변환
print(cat_list)
'''
[nan, '영유아', '영유아', '미성년자', '영유아', '미성년자', '영유아', '미성년자', '청년', '청년', '장년', '미성년자', '장년', '중년', '노년', '청년', '장년', '중년', '노년']
'''

test = pd.DataFrame({'나이':ages, '연령대':cat_list}) # ages와 cat_list를 df로
print(test.head())
'''
    나이   연령대
0  0.0   NaN
1  0.5   영유아
2  4.0   영유아
3  6.0  미성년자
4  4.0   영유아
'''

print(test['연령대'].value_counts())
'''
연령대
영유아     4
미성년자    4
청년      3
장년      3
중년      2
노년      2
Name: count, dtype: int64
'''

'''
    Categorical 클래스 객체
        카테고리명 속성 : Categorical.categories
        카테고리명 저장
        코드 속성 : Categorical.codes
        인코딩한 카테고리 값을 정수로 갖는다.
'''

# cats 변수내의 범주 index를 저장
print(cats.categories)
'''
Index(['영유아', '미성년자', '청년', '중년', '장년', '노년'], dtype='object')
'''

# 코드 속성 확인 -> 인코딩한 카테고리 값을 정수로 갖는다.
# 정수값이 -1이면 NaN값
print(cats.codes)
'''
[-1  0  0  1  0  1  0  1  2  2  4  1  4  3  5  2  4  3  5]
'''

'''
    구간 경계선을 지정하지 않고 데이터 개수가 같도록 지정한 수의 구간으로 분할하기 : qcut()
        형식 : pd.qcut(data,구간수,labels=[d1,d2....])
        
         - 예)1000개의 데이터를 4구간으로 나누려고 한다면
         - qcut 명령어를 사용 한 구간마다 250개씩 나누게 된다.
         - 예외)같은 숫자인 경우에는 같은 구간으로 처리한다.
'''

# 랜덤정수 20개를 생성하고 생성된 정수를 4개의 구간으로 나누시오.
# 각 구간의 label은 Q1,Q2,Q3,Q4 로 설정하시오.
# 랜덤정수 생성 : 범위 0-19, size =20
# seed 설정해서 재 실행해도 랜덤정수가 변하지 않도록 생성

# 랜덤 정수 생성
np.random.seed(2)
data = np.random.randint(20,size=20)
print(data)
'''
[ 8 15 13  8 11 18 11  8  7  2 17 11 15  5  7  3  6  4 10 11]
'''

# 4구간으로 나누기
qcat = pd.qcut(data,4,labels=['Q1','Q2','Q3','Q4'])
print(qcat)
'''
['Q2', 'Q4', 'Q4', 'Q2', 'Q3', ..., 'Q1', 'Q1', 'Q1', 'Q3', 'Q3']
Length: 20
Categories (4, object): ['Q1' < 'Q2' < 'Q3' < 'Q4']
'''

print(pd.value_counts(qcat))
'''
Q1    5
Q2    5
Q3    5
Q4    5
Name: count, dtype: int64
'''

# df로 만들기
df0 = pd.DataFrame(data, columns=['관측수'])
df0['범주'] = qcat
print(df0)
'''
    관측수  범주
0     8  Q2
1    15  Q4
2    13  Q4
3     8  Q2
4    11  Q3
5    18  Q4
6    11  Q3
7     8  Q2
8     7  Q2
9     2  Q1
10   17  Q4
11   11  Q3
12   15  Q4
13    5  Q1
14    7  Q2
15    3  Q1
16    6  Q1
17    4  Q1
18   10  Q3
19   11  Q3
'''