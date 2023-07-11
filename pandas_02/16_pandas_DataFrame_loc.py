import pandas as pd
import numpy as np

'''
    loc 인덱서 : 행 우선 인덱서
        df[열이름값] # 기본 인덱싱, 열우선
        df.loc[행인덱싱 값] #행우선 인덱서
        df.loc[행인덱싱 값,열인덱싱 값]
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

# 1. loc 인덱싱 - 행 추출
print(df.loc['a']) # 시리즈로 반환
'''
A    10
B    11
C    12
D    13
Name: a, dtype: int32
'''

# 2. loc 인덱싱 - 열 추출
#print(df.loc['A']) # 에러, loc 인덱싱에서는 단독 열 추출 불가

# loc 여러 행 추출
print(df.loc[['a','b']])
print(df.loc['a':'b'])
'''
    A   B   C   D
a  10  11  12  13
b  14  15  16  17
'''

# 3. boolean으로 loc 인데싱
# A열의 값이 15보다 큰 행을 추출
print(df.loc[df.A>15])
'''
    A   B   C   D
c  18  19  20  21
'''

# boolean 시리즈를 반환하는 함수 작성
def sel_row(df):
    return df.A>15

# 함수 결과값을 전달받아 인덱스로 사용
print(df.loc[sel_row(df)])
'''
    A   B   C   D
c  18  19  20  21
'''

# 4. loc 슬라이싱 - 행 추출
# 실습 데이터
df2 = pd.DataFrame(np.arange(10,26).reshape(4,4),
 columns=['a','b','c','d'])
print(df2)
'''
    a   b   c   d
0  10  11  12  13
1  14  15  16  17
2  18  19  20  21
3  22  23  24  25
'''

print(df2.loc[1:2])
'''
    a   b   c   d
1  14  15  16  17
2  18  19  20  21
'''

# 5. loc 슬라이싱 - 행열 추출
# 0행 a열의 값 추출
print(df2.loc[0,'a'])
'''
10
'''

# a행 A열의 값 추출
print(df.loc['a','A'])

# 5. loc인덱싱을 사용한 원소값 변경
df.loc['a','A'] = 50
print(df)
'''
    A   B   C   D
a  50  11  12  13
b  14  15  16  17
c  18  19  20  21
'''

# 6. 반환되는 type 주의
# a,b행+A열 추출
df.loc[['a','b']]['A'] # 시리즈
df.loc[['a','b'],'A'] # 시리즈
df.loc[['a', 'b'], ['A']] # df 반환

# a행의 모든 열 추출
df.loc['a'] # 시리즈
df.loc[['a']] # df
df.loc['a', :] # 시리즈
df.loc[['a'],:] # df

# a행의 B,C열 추출
df.loc['a',['b','c']] # 시리즈
df.loc['a', 'b':'c'] # 시리즈
df.loc[['a'],'b':'c'] # df

# B행부터 모든행의 A열을 추출
df.loc['b':,'A'] # 시리즈 반환
df.loc['b':]['A'] #시리즈 반환
df.loc['b':,'A':'A'] # 시리즈 반환
df.loc['b':][['A']] # df반환
df.loc['b':,['A']] # df반환




