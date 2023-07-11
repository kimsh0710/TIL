import pandas as pd
import numpy as np

# 1. 문자열형 인덱스

# 실습 데이터
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

print(s['인천']) # 289045

# 2. 정수형 인덱스
s03 = pd.Series([1,2,3], index=[1,2,3])
print(s03)
'''
1    1
2    2
3    3
dtype: int64
'''

print(s03[1]) # 1

# 3. 리스트 이용
print(s[[0,3,1]])
'''
서울    9904312
대구    2466052
부산    3448737
Name: 인구, dtype: int64
'''