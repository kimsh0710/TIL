import pandas as pd
import numpy as np

# 1. 리스트로 데이터프레임 만들기
df = pd.DataFrame([['a','b','c'],['a','a','g'],['a','a']])
print(df)
'''
   0  1     2
0  a  b     c
1  a  a     g
2  a  a  None
'''

# 2. 딕셔너리로 데이터프레임 만들기
# 열 데이터를 dict로 작성한는 것이 일반적
# 열방향 인덱스(dict의 key), 행방향 인덱스(자동생성 숫자)

df1 = pd.DataFrame(
    {
        'A':[90,80,70],
        'B':[85,98,75],
        'C':[88,99,77],
        'D':[87,89,86],
    }, index=[1,2,3] # 행 인덱스
)

print(df1)
'''
    A   B   C   D
1  90  85  88  87
2  80  98  99  89
3  70  75  77  86
'''

data = {
    "2015": [9904312, 3448737, 2890451, 2466052],
    "2010": [9631482, 3393191, 2632035, 2000002],
    "2005": [9762546, 3512547, 2517680, 2456016],
    "2000": [9853972, 3655437, 2466338, 2473990],
    "지역": ["수도권", "경상권", "수도권", "경상권"],
    "2010-2015 증가율":[0.0283, 0.0163, 0.0982,0.0141]
}

df3 = pd.DataFrame(data)
print(df3)
'''
      2015     2010     2005     2000   지역  2010-2015 증가율
0  9904312  9631482  9762546  9853972  수도권         0.0283
1  3448737  3393191  3512547  3655437  경상권         0.0163
2  2890451  2632035  2517680  2466338  수도권         0.0982
3  2466052  2000002  2456016  2473990  경상권         0.0141
'''

columns = ['지역', '2000', '2005', '2010', '2015', '2010-2015 증가율']
index = ['서울', '부산', '인천', '대구']
df3 = pd.DataFrame(data, index=index, columns=columns)
print(df3)
'''
     지역     2000     2005     2010     2015  2010-2015 증가율
서울  수도권  9853972  9762546  9631482  9904312         0.0283
부산  경상권  3655437  3512547  3393191  3448737         0.0163
인천  수도권  2466338  2517680  2632035  2890451         0.0982
대구  경상권  2473990  2456016  2000002  2466052         0.0141
'''

# 3. 시리즈로 데이터프레임 만들기
a = pd.Series([100,200,300], ['a','b','c'])
b = pd.Series([101,201,301], ['a','b','k'])
c = pd.Series([110,210,310], ['a','b','c'])

df4 = pd.DataFrame([a,b,c], index=[100,200,300])
print(df4)
'''
         a      b      c      k
100  100.0  200.0  300.0    NaN
200  101.0  201.0    NaN  301.0
300  110.0  210.0  310.0    NaN
'''

# 4. csv 데이터로부터 데이터프레임 만들기
train_data = pd.read_csv(r"C:\DataEngineer26-main\12_머신러닝딥러닝\train.csv")
print(train_data.head())
'''
     PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S
'''
# 인덱스, 컬럼 지정해서 csv 불러오기
train_data = pd.read_csv(r"C:\DataEngineer26-main\12_머신러닝딥러닝\train.csv",
                         index_col='PassengerId',
                         usecols=['PassengerId', 'Survived', 'Name', 'Sex', 'Age'])
print(train_data.columns)
'''
Index(['Survived', 'Name', 'Sex', 'Age'], dtype='object')
'''

print(train_data.head())
'''
             Survived  ...   Age
PassengerId            ...      
1                   0  ...  22.0
2                   1  ...  38.0
3                   1  ...  26.0
4                   1  ...  35.0
5                   0  ...  35.0
'''














