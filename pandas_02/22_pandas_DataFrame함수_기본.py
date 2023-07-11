import pandas as pd
import numpy as np

'''
  df의 기본 함수
mean(axis=0/1)
min(axis=0/1)
max(axis=0/1)

'''

np.random.seed(1)
df2=pd.DataFrame(np.random.randint(10,size=(4,8)))
df2['total']=df2.sum(axis=1)
print(df2)
'''
    0  1  2  3  4  5  6  7  total
0  5  8  9  5  0  0  1  7     35
1  6  9  2  4  5  2  4  2     34
2  4  7  7  9  1  7  0  6     41
3  9  9  7  6  9  1  0  1     42
'''

# 각 열의 평균
print(df2.mean(axis=0))
'''
0         6.00
1         8.25
2         6.25
3         6.00
4         3.75
5         2.50
6         1.25
7         4.00
total    38.00
dtype: float64
'''

# 각 행의 평균
print(df2.mean(axis=1))
'''
0    7.777778
1    7.555556
2    9.111111
3    9.333333
dtype: float64
'''

# 각 열의 최소값
print(df2.min(axis=0))
'''
0         4
1         7
2         2
3         4
4         0
5         0
6         0
7         1
total    34
dtype: int64
'''

# 각 행의 최소값
print(df2.min(axis=1))
'''
0    0
1    2
2    0
3    0
dtype: int64
'''

# 각 열의 최대값
print(df2.max(axis=0))
'''
0         9
1         9
2         9
3         9
4         9
5         7
6         4
7         7
total    42
dtype: int64
'''

# 각 행의 최대값
print(df2.max(axis=1))
'''
0    35
1    34
2    41
3    42
dtype: int64
'''

# 각 열의 최대값을 구해서 max_data라는 행을 추가
df2.loc['max_data'] = df2.max(axis=0)
print(df2)

# total 열 제외하고 행추가 하고 싶은 경우
df2.loc['max_data'] = df2[[0,1,2,3,4,5,6,7]].max(axis=0)
print(df2)
'''
          0  1  2  3  4  5  6  7  total
0         5  8  9  5  0  0  1  7   35.0
1         6  9  2  4  5  2  4  2   34.0
2         4  7  7  9  1  7  0  6   41.0
3         9  9  7  6  9  1  0  1   42.0
max_data  9  9  9  9  9  7  4  7    NaN
'''