import pandas as pd
import numpy as np

'''
    정렬함수 -데이터 정렬 시 사용
        - sort_index(ascending=True/False) : 인덱스를 기준으로 정렬
        - ascending 생략하면 오름차순 정렬
        - sort_value(ascending=True/False) : 데이터 값을 기준으로 정렬
'''

# 1. 시리즈 정렬
# 실습 데이터
np.random.seed(1) #항상 같은 값이 나오게 설정
s2=pd.Series(np.random.randint(6,size=100)) # 0~5의 정수 내에서 100개의 난수 추출
print(s2.head())
'''
0    5
1    3
2    4
3    0
4    1
dtype: int32
'''

# s2 시리즈에 대해 value_counts()
print(s2.value_counts()) # 반환결과는 빈도값을 기준으로 내림차순 정렬
'''
1    22
0    18
4    17
5    16
3    14
2    13
Name: count, dtype: int64
'''

# 인덱스 기준 정렬(오름차순)
print(s2.value_counts().sort_index())
'''
0    18
1    22
2    13
3    14
4    17
5    16
Name: count, dtype: int64
'''

# 인덱스 기준 정렬(내림차순)
print(s2.value_counts().sort_index(ascending=False))
'''
5    16
4    17
3    14
2    13
1    22
0    18
Name: count, dtype: int64
'''

'''
    데이터 프레임 정렬
        - df.sort_values() : 특정열 값 기준 정렬
        - 데이터프레임은 2차원 배열과 동일하기 때문에 정렬시 기준열을 줘야 한다. by 인수 사용 
        : 생략 불가
        - by = 기준열, by=[기준열1,기준열2]
            오름차순/내림차순 : ascending = True/False (생략하면 오름차순)
        - df.sort_index() : DF의 INDEX 기준 정렬
            오름차순/내림차순 : ascending = True/False (생략하면 오름차순)
'''

np.random.seed(3) # 시드값 고정되어서 동일한 값의 난수가 발생
df1 = pd.DataFrame(np.random.randint(5,size=(4,4))) #기본 정수
print(df1)
'''
   0  1  2  3
0  2  0  1  3
1  0  0  0  3
2  2  3  1  1
3  2  0  4  4
'''

# 특정열(0)의 값을 기준으로 정렬
print(df1.sort_values(by=0) )
'''
   0  1  2  3
1  0  0  0  3
0  2  0  1  3
2  2  3  1  1
3  2  0  4  4
'''

print(df1.sort_values(by=0,ascending=False))
'''
   0  1  2  3
0  2  0  1  3
2  2  3  1  1
3  2  0  4  4
1  0  0  0  3
'''

# 특정열(0과 2)를 기준으로 정렬
print(df1.sort_values(by=[0,2],ascending=False))
'''
   0  1  2  3
3  2  0  4  4
0  2  0  1  3
2  2  3  1  1
1  0  0  0  3
'''

# 예제 DataFrame
df = pd.DataFrame({'num_legs': [2, 4, 4, 6],
 'num_wings': [2, 0, 0, 0]},
 index=['falcon', 'dog', 'cat', 'ant'])
print(df)
'''
        num_legs  num_wings
falcon         2          2
dog            4          0
cat            4          0
ant            6          0
'''

# 인덱스 기준 오름차순 정렬
print(df.sort_index())
'''
        num_legs  num_wings
ant            6          0
cat            4          0
dog            4          0
falcon         2          2
'''

