import pandas as pd
import numpy as np

'''
  행/열 합계
     - df.sum() 함수 사용
     - 행과 열의 합계를 구할때는 sum(axis=0/1) - axis는 0이 기본
     - 각 열의 합계를 구할때는 sum(axis=0)
     - 각 행의 합계를 구할때는 sum(axis=1)
'''

# 예제 DF 생성
#4행 8열의 데이터프레임 작성, 난수를 발생시키고
#0-9범위에서 매번 같은 난수 발생되어 반환되도록 설정
np.random.seed(1)
df2=pd.DataFrame(np.random.randint(10,size=(4,8)))
print(df2)
'''
  0  1  2  3  4  5  6  7
0  5  8  9  5  0  0  1  7
1  6  9  2  4  5  2  4  2
2  4  7  7  9  1  7  0  6
3  9  9  7  6  9  1  0  1
'''

# df2의 각 행의 합계를 구함
print(df2.sum(axis=1))
'''
0    35
1    34
2    41
3    42
dtype: int64
'''

# df2의 각 열의 합계를 구함
print(df2.sum(axis=0))
'''
0    24
1    33
2    25
3    24
4    15
5    10
6     5
7    16
dtype: int64
'''

# 각 행의 합계를 표시하는 합계 열을 추가하시오
df2['total']=df2.sum(axis=1)
print(df2)
'''
    0  1  2  3  4  5  6  7  total
0  5  8  9  5  0  0  1  7     35
1  6  9  2  4  5  2  4  2     34
2  4  7  7  9  1  7  0  6     41
3  9  9  7  6  9  1  0  1     42
'''



