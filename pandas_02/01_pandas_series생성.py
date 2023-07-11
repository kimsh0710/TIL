import pandas as pd
import numpy as np

# 1. Series 생성하기

# 1) pd.Series(집합적 자료형)
# 시리즈 생성시 반드시 집합적 자료형을 이용해야 함

# pd.Series(리스트)
s = pd.Series([1,2,3])
print(s)

# pd.Series(튜플)
s = pd.Series((1.0,2.0,3.0))
print(s)

# 리스트내에 서로 다른 type의 data가 있으면 형변환 일어남- 문자열로 변환됨
s_1 = pd.Series(['a',1,3.0]) #dtype: object
print(s_1)

# 범위를 시리즈의 value 생성하는 데 사용하기 - range/np.arange 함수 사용
s = pd.Series(range(10,14)) # index 인수는 생략됨
print(s)

print(np.arange(20)) # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]

s3 = pd.Series(np.arange(20))
print(s3)

# 2) 결측값 포함해서 Series 만들기
s=pd.Series([1,2,3,np.nan,6,8])
print(s)

# 3) 인덱스 명시해서 Series 만들기

# 숫자 인덱스
s=pd.Series([10,20,30],index=[1,2,3])
print(s)

# 문자 인덱스
s= pd.Series([95,100,88], index = ['홍길동','이몽룡','성춘향'])
print(s)

# 범위(range) 인덱스
s00 = pd.Series([1,2,3]) # index가 없는 Series
print(s00.index) # RangeIndex(start=0, stop=3, step=1)

s = pd.Series([9904312,3448737,289045,2466052],
 index=["서울","부산","인천","대구"]) # Index(['서울', '부산', '인천', '대구'], dtype='object')
print(s.index)

# 4) 인덱스에 이름 붙이기
s.index.name = '광역시'
print(s)

# 5) 시리즈 값에 이름 붙이기
s.name = '인구'
print(s)

