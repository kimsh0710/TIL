import pandas as pd
import numpy as np

'''
    count 함수 사용 예제
        - 타이타닉 승객 데이터 사용
        - seaborn 패키지 내에 data로 존재
        - 데이터셋 읽어오기 : 패키지명.load_dataset("data명")
'''

import seaborn as sns

# 타이타닉 승객 데이터 로드
titanic = sns.load_dataset('titanic')
# del titanic['Unnamed: 0']
print(titanic.head())
'''
   survived  pclass     sex   age  ...  deck  embark_town  alive  alone
0         0       3    male  22.0  ...   NaN  Southampton     no  False
1         1       1  female  38.0  ...     C    Cherbourg    yes  False
2         1       3  female  26.0  ...   NaN  Southampton    yes   True
3         1       1  female  35.0  ...     C  Southampton    yes  False
4         0       3    male  35.0  ...   NaN  Southampton     no   True
'''

print(titanic.count())
# count()함수는 nan값을 제외하므로 각 열에 nan 값이 있는지 확인할 수 있음.
'''
survived       891
pclass         891
sex            891
age            714 # nan값 존재
sibsp          891
parch          891
fare           891
embarked       889 # nan값 존재
class          891
who            891
adult_male     891
deck           203 # nan값 존재
embark_town    889 # nan값 존재
alive          891
alone          891
dtype: int64
'''

'''
    카테고리 값 세기
        - 시리즈의 값이 정수,문자열 등 카테고리 값인 경우에
        - 시리즈.value_counts()메서드를 사용해 각각의 값이 나온 횟수를 셀 수 있음
        - 파라미터 normalize=True 를 사용하면 각 값 및 범주형 데이터의 비율을 계산
        - 시리즈.value_counts(normalize=True)
'''

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
print(len(s2)) # 100

print(s2.value_counts()) # 0~5의 정수가 각각 몇번 추출되었는지 확인
'''
1    22
0    18
4    17
5    16
3    14
2    13
Name: count, dtype: int64
'''

print(s2.value_counts(normalize=True))
'''
1    0.22
0    0.18
4    0.17
5    0.16
3    0.14
2    0.13
Name: proportion, dtype: float64
'''

'''
    범주형 데이터에 value_counts() 함수 적용
        - 범주형 데이터 : 관측 결과가 몇개의 범주 또는 항목의 형태로 나타나는 자료
            ex. 성별(남,여), 선호도(좋다, 보통, 싫다), 혈액형(A,B,O,AB) 등
'''

# titanic 데이터 alive열 로드 : 생존여부가 yes/no로 표시되어 있음
print(titanic['alive'].dtype) # object
print(titanic['alive'].value_counts())
'''
no     549
yes    342
Name: count, dtype: int64
'''
print(titanic['alive'].value_counts(normalize=True))
'''
no     0.616162
yes    0.383838
Name: proportion, dtype: float64
'''
print(titanic['alive'].value_counts(normalize=True) *100)
'''
no     61.616162
yes    38.383838
Name: proportion, dtype: float64
'''

# 타이타닉호에 승선한 승객의 남여 비율을 확인
# 성별 피처 : sex column

print(titanic['sex'].value_counts(normalize=True)*100)
'''
male      64.758698
female    35.241302
Name: proportion, dtype: float64
'''


'''
    데이터프레임에 value_counts() 함수 사용
        - 행을 하나의 value로 설정하고 동일한 행이 몇번 나타났는지 반환
        - 행의 경우가 인덱스로 개수된 값이 value로 표시되는 Series 반환
'''

print(titanic[['sex','alive']].head(2))
'''
      sex alive
0    male    no
1  female   yes
'''

print(titanic[['sex','alive']].value_counts()) # 시리즈로 반환
'''
sex     alive
male    no       468
female  yes      233
male    yes      109
female  no        81
Name: count, dtype: int64
'''

print(pd.DataFrame(titanic[['sex','alive']].value_counts()))# df로 변환
'''
              count
sex    alive       
male   no       468
female yes      233
male   yes      109
female no        81
'''
