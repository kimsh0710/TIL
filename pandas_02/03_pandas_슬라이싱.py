import pandas as pd
import numpy as np

# 1. 문자 인덱스 슬라이싱

s = pd.Series([9904312,3448737,289045,2466052],
 index=["서울","부산","인천","대구"]) # Index(['서울', '부산', '인천', '대구'], dtype='object')
s.index.name = '광역시'
s.name = '인구'
print(s)
'''
광역시
서울    9904312
부산    3448737
인천     289045
대구    2466052
Name: 인구, dtype: int64
'''

print(s[[1,2]])
print(s[['부산','인천']])
print(s[1:3])
'''
광역시
부산    3448737
인천     289045
Name: 인구, dtype: int64
'''

print(s["부산":"대구"])
'''
광역시
부산    3448737
인천     289045
대구    2466052
Name: 인구, dtype: int64
'''

# 2. 정수형 인덱스 슬라이싱
s_01 = pd.Series([100,200,300,400], index=[1,2,3,4])
print(s_01)
'''
1    100
2    200
3    300
4    400
dtype: int64
'''
print(s_01[2:4])
'''
3    300
4    400
dtype: int64
'''

# 시리즈의 인덱스를 명시할때는 가급적이면 문자형으로 명시하는 것이 좋다

