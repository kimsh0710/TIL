import pandas as pd
import numpy as np

'''
 난수 발생시켜 dataframe 생성
   - 난수 seed(값)라는 함수를 사용할 수 있음
   - seed의 의미 : 난수 알고리즘에서 사용하는 기본 값으로
   - 시드값이 같으면 동일한 난수가 발생함
   - 난수 함수 사용시 매번 고정시켜야 함
   - 계속 변경되는 난수를 받고 싶으면 함수등을 이용해서 시드값이 매번 변하게 작업해야 함. Time.tiem()
'''

print(np.random.randint(5)) #3
print(np.random.randint(5, size =4)) # 난수 4개를 생성 [2 2 1 3]

# 난수 발생시 항상 고정된 값을 발생시킬 수도 있음
print(np.random.seed(3))
print(np.random.randint(5, size =4)) # 난수 4개를 생성 [2 0 1 3]

print(np.random.randint(5,size=(4,4)))
'''
[[0 0 0 3]
 [2 3 1 1]
 [2 0 4 4]
 [0 2 1 2]]
'''



