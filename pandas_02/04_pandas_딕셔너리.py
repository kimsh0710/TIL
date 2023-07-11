import pandas as pd
import numpy as np

# 1. in 연산자/ for 반복문 사용

s = pd.Series([9904312,3448737,289045,2466052],
 index=["서울","부산","인천","대구"]) # Index(['서울', '부산', '인천', '대구'], dtype='object')
s.index.name = '광역시'
s.name = '인구'
s['서울'] = 10000000

print(s)
'''
광역시
서울    10000000
부산     3448737
인천      289045
대구     2466052
Name: 인구, dtype: int64
'''

# 인덱스가 서울인 원소가 시리즈에 있는지 확인( in)
print('서울' in s) # True
print('대전' in s) # False
print('대전' not in s) # True

# 딕셔너리의 items() 함수 시리즈에 사용 가능
print(s.items()) # zip 객체 <zip object at 0x000001EF7DCA4240>
print(list(s.items())) # [('서울', 10000000), ('부산', 3448737), ('인천', 289045), ('대구', 2466052)]

# 시리즈 각 원소 출력
for k, v in s.items() :
 print('%s=%d' % (k,v))

'''
서울=10000000
부산=3448737
인천=289045
대구=2466052
'''

# 2. 딕셔너리로 시리즈 만들기

scores = {'홍길동':96, '이몽룡':100, '성춘향':88}
s=pd.Series(scores)
print(s)
'''
홍길동     96
이몽룡    100
성춘향     88
dtype: int64
'''

city = {'서울':9631482,'부산':3393191,'인천':2632035,'대전':1490158}
s=pd.Series(city)
print(s)
'''
서울    9631482
부산    3393191
인천    2632035
대전    1490158
dtype: int64
'''

city = {'서울':9631482,'부산':3393191,'인천':2632035,'대전':1490158}
s=pd.Series(city,index=city.keys())
print(s)
'''
서울    9631482
부산    3393191
인천    2632035
대전    1490158
dtype: int64
'''

s=pd.Series(city, index=['부산','인천','서울','대전'])
print(s)
'''
부산    3393191
인천    2632035
서울    9631482
대전    1490158
dtype: int64
'''


