import pandas as pd
import numpy as np

np.random.seed(0)
df2 = pd.DataFrame({
 'key1':['A', 'A','B','B', 'A'],
 'key2':['one','two','one','two','one'],
 'data1':[1,2,3,4,5],
 'data2':[10,20,30,40,50]
})

print(df2)
'''
  key1 key2  data1  data2
0    A  one      1     10
1    A  two      2     20
2    B  one      3     30
3    B  two      4     40
4    A  one      5     50
'''

# key1을 기준으로 group
groups = df2.groupby(df2.key1)
print(groups)
'''
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000023608A72640>
'''

# groups 속성을 확인하려면 그룹핑된 요약을 볼 수 있음
print(groups.groups)
'''
{'A': [0, 1, 4], 'B': [2, 3]} 
 -> 딕셔너리로 반환, {그룹명:그룹에 포함된 행인덱스}
'''

print(groups.groups.keys())
'''
dict_keys(['A', 'B'])
'''

print(groups.groups['A'])
'''
Index([0, 1, 4], dtype='int64')
'''

print(pd.DataFrame(groups))
'''
   0                                                  1
0  A    key1 key2  data1  data2
0    A  one      1  ...
1  B    key1 key2  data1  data2
2    B  one      3  ...
'''

print(pd.DataFrame(groups).loc[0].values)
'''
['A'   key1 key2  data1  data2
     0    A  one      1     10
     1    A  two      2     20
     4    A  one      5     50]
'''

print(pd.DataFrame(groups).loc[1].values[1])
'''
  key1 key2  data1  data2
2    B  one      3     30
3    B  two      4     40
'''

# groups 객체에 연산 메서드를 적용시켜 요약 결과를 확인
print(groups.sum())
'''
           key2  data1  data2
key1                         
A     onetwoone      8     80
B        onetwo      7     70
'''

# data1 선택 후 계산
print(groups['data1'].sum())
'''
key1
A    8
B    7
Name: data1, dtype: int64
'''

# 전체 데이터 계산 후 data1 선택
print(groups.sum()['data1'])
'''
key1
A    8
B    7
Name: data1, dtype: int64
'''

# 위 연산을 df로 반환하도록
print(groups[['data1']].sum())
'''
      data1
key1       
A         8
B         7
'''

# 그룹함수 예제

# apply( ) / agg( )

import seaborn as sns
iris = sns.load_dataset("iris")

print((iris))
'''
     sepal_length  sepal_width  petal_length  petal_width    species
0             5.1          3.5           1.4          0.2     setosa
1             4.9          3.0           1.4          0.2     setosa
2             4.7          3.2           1.3          0.2     setosa
3             4.6          3.1           1.5          0.2     setosa
4             5.0          3.6           1.4          0.2     setosa
..            ...          ...           ...          ...        ...
145           6.7          3.0           5.2          2.3  virginica
146           6.3          2.5           5.0          1.9  virginica
147           6.5          3.0           5.2          2.0  virginica
148           6.2          3.4           5.4          2.3  virginica
149           5.9          3.0           5.1          1.8  virginica

[150 rows x 5 columns]
'''

# iris 품종별로 그룹
i_group = iris.groupby(iris.species)
print(i_group)
'''
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x00000161C5061640>
'''
print(i_group.groups)
'''
{'setosa': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ... 47, 48, 49],
 'versicolor': [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,... 97, 98, 99],
  'virginica': [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110,... 147, 148, 149]}
'''
print(i_group.mean())
'''
            sepal_length  sepal_width  petal_length  petal_width
species                                                         
setosa             5.006        3.428         1.462        0.246
versicolor         5.936        2.770         4.260        1.326
virginica          6.588        2.974         5.552        2.026
'''

print(pd.DataFrame(i_group))
'''
            0                                                  1
0      setosa      sepal_length  sepal_width  petal_length  p...
1  versicolor      sepal_length  sepal_width  petal_length  p...
2   virginica       sepal_length  sepal_width  petal_length  ...
'''
print(pd.DataFrame(i_group).loc[1])
'''
0                                           versicolor
1        sepal_length  sepal_width  petal_length  p...
Name: 1, dtype: object
'''
print(pd.DataFrame(i_group).loc[1].values[1])
'''
    sepal_length  sepal_width  petal_length  petal_width     species
50           7.0          3.2           4.7          1.4  versicolor
51           6.4          3.2           4.5          1.5  versicolor
52           6.9          3.1           4.9          1.5  versicolor
53           5.5          2.3           4.0          1.3  versicolor
54           6.5          2.8           4.6          1.5  versicolor
55           5.7          2.8           4.5          1.3  versicolor

...

'''
print(pd.DataFrame(i_group).loc[1].values[1]['sepal_width'])
'''
50    3.2
51    3.2
52    3.1
53    2.3
54    2.8
55    2.8
...
'''
print(pd.DataFrame(i_group).loc[1].values[1]['sepal_width'].max())
'''
3.4
'''

print(i_group.petal_length.sum())
'''
species
setosa         73.1
versicolor    213.0
virginica     277.6
Name: petal_length, dtype: float64
'''

print(i_group.max()/i_group.min())
'''
            sepal_length  sepal_width  petal_length  petal_width
species                                                         
setosa          1.348837     1.913043      1.900000     6.000000
versicolor      1.428571     1.700000      1.700000     1.800000
virginica       1.612245     1.727273      1.533333     1.785714
'''

def peak_to_peak_ration(x): # x는 시리즈
 return x.max()/x.min()

result = peak_to_peak_ration(iris.sepal_length)
print(result) # 1.8372093023255816

# 그룹 객체의 각 그룹에 대해 열별로 peak_to_peak_ration 함수 호출
print(i_group.agg(peak_to_peak_ration))
'''
            sepal_length  sepal_width  petal_length  petal_width
species                                                         
setosa          1.348837     1.913043      1.900000     6.000000
versicolor      1.428571     1.700000      1.700000     1.800000
virginica       1.612245     1.727273      1.533333     1.785714
'''

print(i_group.apply(peak_to_peak_ration))
'''
            sepal_length  sepal_width  petal_length  petal_width
species                                                         
setosa          1.348837     1.913043      1.900000     6.000000
versicolor      1.428571     1.700000      1.700000     1.800000
virginica       1.612245     1.727273      1.533333     1.785714
'''

def top3_petal_length(df):
 return df.sort_values(by="petal_length", ascending=False)[:3]

result = top3_petal_length(iris)

print(result)
'''
     sepal_length  sepal_width  petal_length  petal_width    species
118           7.7          2.6           6.9          2.3  virginica
122           7.7          2.8           6.7          2.0  virginica
117           7.7          3.8           6.7          2.2  virginica
'''

print(i_group.apply(top3_petal_length))
'''
                sepal_length  sepal_width  ...  petal_width     species
species                                    ...                         
setosa     24            4.8          3.4  ...          0.2      setosa
           44            5.1          3.8  ...          0.4      setosa
           23            5.1          3.3  ...          0.5      setosa
versicolor 83            6.0          2.7  ...          1.6  versicolor
           77            6.7          3.0  ...          1.7  versicolor
           72            6.3          2.5  ...          1.5  versicolor
virginica  118           7.7          2.6  ...          2.3   virginica
           117           7.7          3.8  ...          2.2   virginica
           122           7.7          2.8  ...          2.0   virginica
'''

def q3cut(s):
 return pd.qcut(s, 3, labels=['소','중','대']).astype(str)

q = iris.groupby(iris.species).petal_length.apply(q3cut)
print(q)
'''
species       
setosa     0      소
           1      소
           2      소
           3      중
           4      소
                 ..
virginica  145    소
           146    소
           147    소
           148    중
           149    소
Name: petal_length, Length: 150, dtype: object
'''


print(iris.head(1))
'''
   sepal_length  sepal_width  petal_length  petal_width species
0           5.1          3.5           1.4          0.2  setosa
'''

# q1 = pd.Series(q, name="petal_width_class")
# print(q1)
# new_df = pd.concat([iris, q1], axis=1)
# print(new_df.head(3))

# iris['petal_length_class'] = iris.groupby(iris.species).petal_length.apply(q3cut)
iris['petal_length_class'] = iris.groupby('species').petal_length.apply(q3cut).reset_index(drop=True)

print(iris.head(5))
'''
   sepal_length  sepal_width  ...  species  petal_length_class
0           5.1          3.5  ...   setosa                   소
1           4.9          3.0  ...   setosa                   소
2           4.7          3.2  ...   setosa                   소
3           4.6          3.1  ...   setosa                   중
4           5.0          3.6  ...   setosa                   소

[5 rows x 6 columns]
'''
