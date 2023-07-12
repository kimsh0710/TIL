import pandas as pd
import numpy as np

'''
 리스트 내포 for문의 일반 문법
  [표현식(연산식) for 항목 in 반복가능객체 if 조건문]
  if 조건문은 생략 가능하다.
  반복가능객체 : 리스트, 튜플,딕셔너리,range()등
'''

a=[1,2,3,4]

# 위 a 리스트의 각 원소에 2배한 원소값을 만들고 리스트로 저장하시오. 반복문을 사용할 것

# 기존 for 문
a=[1,2,3,4]
result = [] # 빈리스트 생성
for num in a :
 result.append(num*2)

print(result)

'''
[2, 4, 6, 8]
'''

# 리스트 내포 for 문으로
result2 = [num * 2 for num in a]
print(result2)
'''
[2, 4, 6, 8]
'''

# ['id_1','id_2','id_3','id_4'] 와 같은 리스트 요소를
# 내포 for문을 이용해서 생성후 리스트로 추가하시오.

result3 = ['id_'+str(i) for i in a]
print(result3)
'''
['id_1', 'id_2', 'id_3', 'id_4']
'''