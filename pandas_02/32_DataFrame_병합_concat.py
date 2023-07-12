import pandas as pd
import numpy as np

'''
  concat 명령을 사용한 데이터 연결
    pd.concat(objs, # Series, DataFrame, Panel object 
     axis=0, # 0: 위+아래로 합치기, 1: 왼쪽+오른쪽으로 합치기 
     join='outer', # 'outer': 합집합(union), 'inner': 교집합(intersection) 
     ignore_index=False, # False: 기존 index 유지, True: 기존 index 무시 
     keys=None, # 계층적 index 사용하려면 keys 튜플 입력)
     
    concat 명령을 사용하면 기준열 없이 데이터를 연결한다.
    기본은 위 아래로 데이터 행 결합(row bind) axis 속성을 1로 설정하면 열 결합(column bind)을 수행한다
    단순히 두 시리즈나 데이터프레임을 연결하기 때문에 인덱스 값이 중복될 수 있다.
'''

#두 시리즈 데이터 연결
s1=pd.Series([0,1],index=['A','B'])
s2=pd.Series([2,3,4],index=['A','B','C'])

print(s1)
print(s2)
'''
A    0
B    1
dtype: int64

A    2
B    3
C    4
dtype: int64
'''

# 두 시리즈 연결
print(pd.concat([s1,s2]))
'''
A    0
B    1
A    2
B    3
C    4
dtype: int64
'''

# DataFrame concat 연결

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
 'B': ['B0', 'B1', 'B2', 'B3'],
 'C': ['C0', 'C1', 'C2', 'C3'],
 'D': ['D0', 'D1', 'D2', 'D3']},
 index=[0, 1, 2, 3])
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
 'B': ['B4', 'B5', 'B6', 'B7'],
 'E': ['C4', 'C5', 'C6', 'C7'],
 'F': ['D4', 'D5', 'D6', 'D7']},
 index=[0, 1, 2, 3])
df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
 'B': ['B8', 'B9', 'B10', 'B11'],
 'C': ['C8', 'C9', 'C10', 'C11'],
 'O': ['D8', 'D9', 'D10', 'D11']},
 index=[1,2,3,4])

print(df1)
print(df2)
print(df3)
'''
    A   B   C   D
0  A0  B0  C0  D0
1  A1  B1  C1  D1
2  A2  B2  C2  D2
3  A3  B3  C3  D3

    A   B   E   F
0  A4  B4  C4  D4
1  A5  B5  C5  D5
2  A6  B6  C6  D6
3  A7  B7  C7  D7

     A    B    C    O
1   A8   B8   C8   D8
2   A9   B9   C9   D9
3  A10  B10  C10  D10
4  A11  B11  C11  D11
'''

# concat() : 위 아래로 단순 병합
result = pd.concat([df1, df2, df3])
print(result) # default : outer 조인
'''
     A    B    C    D    E    F    O
0   A0   B0   C0   D0  NaN  NaN  NaN
1   A1   B1   C1   D1  NaN  NaN  NaN
2   A2   B2   C2   D2  NaN  NaN  NaN
3   A3   B3   C3   D3  NaN  NaN  NaN
0   A4   B4  NaN  NaN   C4   D4  NaN
1   A5   B5  NaN  NaN   C5   D5  NaN
2   A6   B6  NaN  NaN   C6   D6  NaN
3   A7   B7  NaN  NaN   C7   D7  NaN
1   A8   B8   C8  NaN  NaN  NaN   D8
2   A9   B9   C9  NaN  NaN  NaN   D9
3  A10  B10  C10  NaN  NaN  NaN  D10
4  A11  B11  C11  NaN  NaN  NaN  D11
'''

# 인덱스가 중복되므로 멀티인덱스를 생성할 수도 있음
result=pd.concat([df1, df2, df3],keys=['x','y','z'])
print(result)
'''
       A    B    C    D    E    F    O
x 0   A0   B0   C0   D0  NaN  NaN  NaN
  1   A1   B1   C1   D1  NaN  NaN  NaN
  2   A2   B2   C2   D2  NaN  NaN  NaN
  3   A3   B3   C3   D3  NaN  NaN  NaN
y 0   A4   B4  NaN  NaN   C4   D4  NaN
  1   A5   B5  NaN  NaN   C5   D5  NaN
  2   A6   B6  NaN  NaN   C6   D6  NaN
  3   A7   B7  NaN  NaN   C7   D7  NaN
z 1   A8   B8   C8  NaN  NaN  NaN   D8
  2   A9   B9   C9  NaN  NaN  NaN   D9
  3  A10  B10  C10  NaN  NaN  NaN  D10
  4  A11  B11  C11  NaN  NaN  NaN  D11
'''
print(result.loc['x'].loc[0,'A'])
# A0

# 3개의 데이터프레임에서 공통적으로 나타나는 열만 표현(inner)
result = pd.concat([df1, df2, df3], join='inner',keys=['x','y','z'])
print(result)
'''
       A    B
x 0   A0   B0
  1   A1   B1
  2   A2   B2
  3   A3   B3
y 0   A4   B4
  1   A5   B5
  2   A6   B6
  3   A7   B7
z 1   A8   B8
  2   A9   B9
  3  A10  B10
  4  A11  B11
'''

result = pd.concat([df1, df2, df3], join='inner',ignore_index=True)
print(result)
'''
      A    B
0    A0   B0
1    A1   B1
2    A2   B2
3    A3   B3
4    A4   B4
5    A5   B5
6    A6   B6
7    A7   B7
8    A8   B8
9    A9   B9
10  A10  B10
11  A11  B11
'''

'''
   concate를 이용한 열 병합
    - axis=1 설정
    - pd.concat([df1,df2],axis=1,join='inner/outer')
    - 데이터프레임들의 열을 결합한다
    - 모든행을 표시하고 해당 행의 데이터가 없는 열의 원소는 NaN으로 표시된다 : 기본설정(join='outer')
    - 병합하는 데이터프레임에 중복되는 인덱스의 행만 표시한다 : join='inner'
'''

# 예제 df 생성
df1=pd.DataFrame(
 np.arange(6).reshape(3,2),
 index=['a','b','c'],
 columns=['데이터1','데이터2']
)
df2=pd.DataFrame(
 5+np.arange(4).reshape(2,2),
 index=['a','c'],
 columns=['데이터2','데이터4']
)
print(df1)
print(df2)
'''
   데이터1  데이터2
a     0     1
b     2     3
c     4     5

   데이터2  데이터4
a     5     6
c     7     8
'''

# 열방향 결합
# join 방식 생략 : outer
print(pd.concat([df1, df2],axis=1))
'''
   데이터1  데이터2  데이터2  데이터4
a     0     1   5.0   6.0
b     2     3   NaN   NaN
c     4     5   7.0   8.0
'''

# 행방향 결합(axis=0 생략 가능)
print(pd.concat([df1, df2],axis=0))
'''
   데이터1  데이터2  데이터4
a   0.0     1   NaN
b   2.0     3   NaN
c   4.0     5   NaN
a   NaN     5   6.0
c   NaN     7   8.0
'''

test = pd.concat([df1,df2], axis=1, join='inner')
print(test)
'''
   데이터1  데이터2  데이터2  데이터4
a     0     1     5     6
c     4     5     7     8
'''
print(test.데이터2)
'''
   데이터2  데이터2
a     1     5
c     5     7
'''

test = pd.concat([df1,df2], axis=1, join='inner',keys=['x','y'])
print(test)
'''
     x         y     
  데이터1 데이터2 데이터2 데이터4
a    0    1    5    6
c    4    5    7    8
'''
print(test.x.데이터1)
'''
a    0
c    4
Name: 데이터1, dtype: int32
'''

#df의 concat을 활용한 행 추가
df1=pd.DataFrame(
 np.arange(6).reshape(3,2),
 index=['a','b','c'],
 columns=['데이터1','데이터2']
)
print(df1)
'''
   데이터1  데이터2
a     0     1
b     2     3
c     4     5
'''

df2 = pd.DataFrame([[5,4]], index=['d'], columns=['데이터1','데이터2'])
print(df2)
'''
   데이터1  데이터2
d     5     4
'''

print(pd.concat([df1,df2]))
'''
   데이터1  데이터2
a     0     1
b     2     3
c     4     5
d     5     4
'''