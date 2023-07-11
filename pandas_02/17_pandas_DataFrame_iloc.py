import pandas as pd
import numpy as np

'''
    iloc 인덱서(위치 인덱스)
        라벨(name)이 아닌 위치를 나타내는 정수 인덱스만 받는다.
        위치 정수값은 0부터 시작
        데이터프레임.iloc[행,열]
'''

# 실습 데이터
df = pd.DataFrame(np.arange(10,22).reshape(3,4),
 index=['a','b','c'],
 columns = ["A","B","C","D"])
print(df)
'''
    A   B   C   D
a  10  11  12  13
b  14  15  16  17
c  18  19  20  21
'''

# 1. iloc 인덱싱
print(df.iloc[0,1])
'''
11
'''

# 2. iloc 슬라이싱 적용
print(df.iloc[0:2, 1:2]) # df 반환
'''
    B
a  11
b  15
'''

print(df.iloc[0:2, 1]) # 시리즈 반환
'''
a    11
b    15
Name: B, dtype: int32
'''

# 0행 데이터에서 끝에서 두번째 열부터 끝까지 반환
print(df.iloc[0:1,-2:]) # df
print(df.iloc[0,-2:]) # 시리즈



