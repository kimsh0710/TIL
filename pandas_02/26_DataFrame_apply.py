import pandas as pd
import numpy as np

'''
  열 또는 행에 동일한 연산 반복 적용할 때 : apply() 함수
    apply() 함수는 DataFrame의 행이나 열에 복잡한 연산을 vectorizing할 수 있게 해주는 함수로 매우 많이 활
    용되는 함수임
    동일한 연산(함수화 되어있어야함)을 모든열에 혹은 모든 행에 반복 적용하고자 할때 사용
    apply(반복적용할 함수, axis=0/1)
    0 : 열마다 반복
    1 : 행마다 반복
    생략시 기본값 : 0
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

# np.sum() : 전달된 첫번째 인수 데이터들의 합산 결과를 반환하는 함수
print(np.sum([1,2,3])) # 6

# df3의 각 열에 대해서 np.sum() 함수를 반복 적용
print(df3.apply(np.sum,0))
'''
a    15
b    15
c    16
dtype: int64
'''

# titanic df의 alive, sex, class 열에 대해서 value_counts() 함수를 적용하여 결과를
# 확인하시오.apply() 함수 사용할 것

import seaborn as sns
titanic = sns.load_dataset('titanic')

print(titanic[['alive','sex', 'class']].apply(pd.value_counts,0))
'''
        alive    sex  class
First     NaN    NaN  216.0
Second    NaN    NaN  184.0
Third     NaN    NaN  491.0
female    NaN  314.0    NaN
male      NaN  577.0    NaN
no      549.0    NaN    NaN
yes     342.0    NaN    NaN
'''

'''
    데이터프레임의 기본 집계함수(sum, min, max, mean 등)들은 행/열 단위 벡터화 연산을 수행함
    apply() 함수를 사용할 필요가 없음
    일반적으로 apply() 함수 사용은 복잡한 연산을 해결하기 위한 lambda 함수나 사용자 정의 함수를 각 열 
    또는 행에 일괄 적용시키기 위해 사용
'''

# lambda 함수를 apply()에 사용하는 예제
print((lambda x : x.max()-x.min())(df3['a']))
'''
3
'''

print(df3.apply(lambda x : x.max()-x.min(),0))
'''
a    3
b    4
c    4
dtype: int64
'''