import pandas as pd
import numpy as np

'''
    데이터 프레임 인덱스 설정을 위해 set_index(), reset_index()
        set index() : 기존 행 인덱스를 제거하고 데이터 열 중 하나를 인덱스로 설정해주는 함수
        reset_index() : 기존 행인덱스를 제거하고 기본인덱스로 변경
        기본인덱스 : 0부터 1씩 증가하는 정수 인덱스
        따로 설정하지 않으면 기존 인덱스는 데이터열로 추가 됨
'''

#예제 데이터프레임 생성
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

# df3의 'a'열을 인덱스로 설정
print(df3.set_index('a'))
'''
   b  c
a      
1  2  1
3  3  5
4  1  2
3  4  4
4  5  4
'''

# 기존 인덱스 삭제
print(df3.reset_index(drop=True))
'''
   a  b  c
0  1  2  1
1  3  3  5
2  4  1  2
3  3  4  4
4  4  5  4
'''

# 설정한 인덱스 삭제
df3.set_index('a',inplace=True)
df3.reset_index(drop=True,inplace=True)
print(df3)
'''
   b  c
0  2  1
1  3  5
2  1  2
3  4  4
4  5  4
'''


'''
    index 이름 변경
        rename(index={현재 index:바꿀 index}) 사용,행인덱스
        rename(columns={현재 index:바꿀 index}) 사용,열인덱스
'''

# 행인덱스 값 변경
# df3의 인덱스 0 -> 1반으로 변경

print(df3.rename(index={0:'1반',1:'2반'}))
'''
    b  c
1반  2  1
2반  3  5
2   1  2
3   4  4
4   5  4
'''

# 컬럼명 변경
df3.rename(columns={'b':'학생'},inplace=True)
print(df3)
'''
   학생  c
0   2  1
1   3  5
2   1  2
3   4  4
4   5  4
'''

