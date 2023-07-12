import pandas as pd
import numpy as np

data = {
 "도시" : ['서울','서울','서울','부산','부산','부산','인천','인천'],
 "연도" : ['2015', '2010', '2005','2015', '2010,', '2005', '2015','2010'],
 "인구" : [1000,2000,3000,4000,5000,6000,7000,8000],
 "지역" : ["수도권","수도권","수도권","경상권","경상권","경상권", "수도권","수도권"]
}

columns = ["도시", '연도', '인구', '지역']
df1 = pd.DataFrame(data, columns=columns)
print(df1)
'''
   도시     연도    인구   지역
0  서울   2015  1000  수도권
1  서울   2010  2000  수도권
2  서울   2005  3000  수도권
3  부산   2015  4000  경상권
4  부산  2010,  5000  경상권
5  부산   2005  6000  경상권
6  인천   2015  7000  수도권
7  인천   2010  8000  수도권
'''

# 각 도시에 대한 연도별 인구 평균
print(df1.pivot_table(index="도시", columns="연도", values="인구"))
'''
연도    2005    2010   2010,    2015
도시                                
부산  6000.0     NaN  5000.0  4000.0
서울  3000.0  2000.0     NaN  1000.0
인천     NaN  8000.0     NaN  7000.0
'''

# 각 지역별 도시에 대한 연도별 인구 평균
print(df1.pivot_table(index=["지역", "도시"], columns="연도", values="인구"))
'''
지역  도시                                
경상권 부산  6000.0     NaN  5000.0  4000.0
수도권 서울  3000.0  2000.0     NaN  1000.0
    인천     NaN    8000.0     NaN  7000.0
'''

import seaborn as sns

df = sns.load_dataset('titanic')[['age','sex','class','fare','survived']]
print(df.head())
'''
    age     sex  class     fare  survived
0  22.0    male  Third   7.2500         0
1  38.0  female  First  71.2833         1
2  26.0  female  Third   7.9250         1
3  35.0  female  First  53.1000         1
4  35.0    male  Third   8.0500         0
'''

# 선실 등급별 숙박객의 성별 평균 나이
print(df.pivot_table(index="class", columns="sex", values="age", aggfunc='mean'))
'''
sex        female       male
class                       
First   34.611765  41.281386
Second  28.722973  30.740707
Third   21.750000  26.507589
'''

# 각 선실 등급별 숙박객의 성별에 따른 생존자 수와 생존율
print(df.pivot_table(index="class", columns="sex", values="survived", aggfunc=["sum","mean"]))
'''
          sum           mean          
sex    female male    female      male
class                                 
First      91   45  0.968085  0.368852
Second     70   17  0.921053  0.157407
Third      72   47  0.500000  0.135447
'''

# 선실 등급에 따른 성별에 대한 생존여부별로 나이와 티켓값의 평균과 최대값
print(df.pivot_table(index=["class","sex"], columns="survived", values=["age","fare"], aggfunc=["mean", "max"]))
'''
                    mean                         ...   max                  
                     age                   fare  ...   age    fare          
survived               0          1           0  ...     1       0         1
class  sex                                       ...                        
First  female  25.666667  34.939024  110.604167  ...  63.0  151.55  512.3292
       male    44.581967  36.248000   62.894910  ...  80.0  263.00  512.3292
Second female  36.000000  28.080882   18.250000  ...  55.0   26.00   65.0000
       male    33.369048  16.022000   19.488965  ...  62.0   73.50   39.0000
Third  female  23.818182  19.329787   19.773093  ...  63.0   69.55   31.3875
       male    27.255814  22.274211   12.204469  ...  45.0   69.55   56.4958
'''