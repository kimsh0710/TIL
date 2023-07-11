import pandas as pd
import numpy as np

# 실습 데이터
s1 = pd.Series([1, 1, 2, 1, 2, 2, 2, 1, 1, 3, 3, 4, 5, 5, 7, np.NaN])
print(s1)
'''
0     1.0
1     1.0
2     2.0
3     1.0
4     2.0
5     2.0
6     2.0
7     1.0
8     1.0
9     3.0
10    3.0
11    4.0
12    5.0
13    5.0
14    7.0
15    NaN
dtype: float64
'''

# 시리즈 원소의 개수
print(len(s1)) # 16

print(s1.size) # 16

# 시리즈 형태
print(s1.shape) # (16,)

# 시리즈 원소의 유일한 값
print(s1.unique()) # [ 1.  2.  3.  4.  5.  7. nan]

# nan을 제외한 원소의 개수
print(s1.count()) # 15

# 배열과 시리즈에서의 연산 차이
a = np.array([2,2,2,2,np.NaN]) # array 타입
print(a)
'''
[ 2.  2.  2.  2. nan]
'''
print(a.mean()) # nan <- nan이 포함된 평균을 계산하므로 nan이 반환됨

b=pd.Series(a)
print(b)
'''
0    2.0
1    2.0
2    2.0
3    2.0
4    NaN
dtype: float64
'''
print(b.mean()) # 2.0 <- 배열을 시리즈로 변경하면 nan값 제외하고 계산됨

# 각 원소들에 대해 동일값의 원소끼리 그룹핑하여 개수를 반환(빈도수)
print(s1.value_counts())
'''
1.0    5
2.0    4
3.0    2
5.0    2
4.0    1
7.0    1
Name: count, dtype: int64
'''




