import pandas as pd
import numpy as np

'''
  np.square 함수는 행/열 별 각 원소에 대해 제곱승 연산을 진행하므로
  행적용이나 열적용 모두 동일한 결과가 나타남
'''
# 실습 데이터
df3 = pd.DataFrame({
 'a':[1,3,4,3,4],
 'b':[2,3,1,4,5],
 'c':[1,5,2,4,4]
})
print(df3)
'''
   a  b  c
0  1  2  1
1  3  3  5
2  4  1  2
3  3  4  4
4  4  5  4
'''

print(df3.apply(np.square,0))
'''
    a   b   c
0   1   4   1
1   9   9  25
2  16   1   4
3   9  16  16
4  16  25  16
'''

print(df3.apply(np.square,1))
'''
    a   b   c
0   1   4   1
1   9   9  25
2  16   1   4
3   9  16  16
4  16  25  16
'''

