# Numpy

## **Numpy 개요**

### 특징

- 다차원 배열(ndarray)을 효과적으로 처리할 수 있도록 도와주는 라이브러리
- Python의 기본 list보다 빠르고 강력한 기능 제공
- 다차원 배열자료 구조인 ndarray 클래스 제공
- 벡터화 연산 가능

## 1차원배열(벡터)

### 1차원배열 생성

- np. array((파이썬)리스트) → 1차원배열
    - 직접 지정한 리스트 값으로 dnarray 생성
    - 정수형의 기본은 int32(4byte)
    - 실수형의 기본은 float64(8byte)
    - python의 list는 값들의 구분이 , 로 표시됨
    - numpy 1차원배열의 값들은 , 로 구분되지 않음

1. 1차원배열(벡터) 생성 방법 1 - np.array(리스트) 이용
    1. 정수형
        
        ```python
        list_value = [10,20,30]  # list, tuple, set , 정수의 기본 dtype은 int32 ( 4byte )
        vector1 = np.array(list_value)
        print(list_value, type(list_value)) # [10, 20, 30] <class 'list'>
        print(vector1, type(vector1), vector1.dtype) # [10 20 30] <class 'numpy.ndarray'> int32
        ```
        
    2. 실수형
        
        ```python
        list_value = [10.,20.,30.]
        vector1 = np.array(list_value)
        print(vector1, type(vector1), vector1.dtype) # [10. 20. 30.] <class 'numpy.ndarray'> float64
        ```
        
    3. upcasting (자동으로 큰 데이터 타입으로 변경)
        
        ```python
        list_value = [10.,20,30] # 정수와 실수가 혼합된 리스트
        vector1 = np.array(list_value)
        print(vector1, type(vector1), vector1.dtype) # 모두 실수로 변경됨 [10. 20. 30.] <class 'numpy.ndarray'> float64
        ```
        
    4. 명시적으로 데이터 타입 변경 ( dtype= )
        
        ```python
        list_value = [10.,20.,30.] # 실수형
        vector1 = np.array(list_value, dtype=np.int32)
        print(vector1, type(vector1), vector1.dtype) # [10 20 30] <class 'numpy.ndarray'> int32
        ```
        

### 1차원배열 속성

```python
list_value = [10,20,30]
print(list_value, type(list_value)) # [10, 20, 30] <class 'list'>

vector1 = np.array(list_value) # [10 20 30] <class 'numpy.ndarray'>

print("1. 벡터의 차원(dimension,axis)갯수:", vector1.ndim) # 1 (1차원 [ )
print("2. 벡터의 각 차원의 크기(shape)-매우중요:", vector1.shape) # tuple로 반환 (3,)
print("3. 벡터의 총 요소 갯수(size):", vector1.size)   # 3
print("4. 벡터의 저장 데이터 type(dtype):", vector1.dtype) # int32 (4 byte)
```

### 랜덤함수

> 가. **np.random.seed(1234)** # 랜덤값 고정
나. **np.random.random([갯수])** : 0.0 <= 값 < 1.0 사이의 임의의 float 값 반환, 갯수 생략하면 1 개 반환
다. **np.random.rand([갯수])** :  0 ~ 1의 균등분포에서 표본 추출, 갯수 생략하면 1 개 반환, 동일한 확률로 랜덤값 추출
라. **np.random.randn([갯수])** :  표준편차가 1이고 평균값이 0인 정규분포에서 표본 추출. 갯수 생략하면  1개반환
마. **np.random.randint(최소범위, 최대범위, n개)** : 주어진 최소(inclusive) ~ 최대(exclusive) 범위안에서 임의의 정수 n개 반환    np.random.randint(최대범위, size=n개) :   0 ~ 최대(exclusive) 범위안에서 임의의 정수 n개 반환
바. **np.random.choice(리스트)**  : 주어진 리스트에서 임의의 값 1개 반환
사. **np.random.shuffle(리스트)**  :  주어진 리스트를 shuffle 함.
> 

1. **랜덤값 고정**
    
    ```python
    np.random.seed(1234)
    ```
    
    <aside>
    💡 np.random.seed란?
    난수를 예측 가능하도록 함.
    각각 다른 seed 값으로 랜덤을 돌리면 다른 값들을 얻을 수 있지만,같은 seed 값에서 랜덤을 돌리면 같은 배열의 결과 값만 얻을 수 있다.
    
    </aside>
    
2. **np.random.random(개수)**
    - 0.0 <= 값 < 1.0 사이의 임의의 float 값을 입력한 개수만큼 랜덤으로 반환.
    - 개수 생략하면 랜덤값 1개 반환
    
    ```python
     print("1. random(5)")
    arr = np.random.random() # => 개수 입력 안하면 결과 1개 반환
    arr = np.random.random(5) # => 결과값 5개 반환
    print(arr, type(arr), arr.dtype) # <class 'numpy.ndarray'> float64
    ```
    
3. **np.random.rand(개수)**
    - 0~1의 균등분포에서 표본 추출
    - 개수 생략하면 랜덤값 1개 반환
    
    ```python
    print("2. rand(5)")
    arr = np.random.rand()
    arr = np.random.rand(5)
    print(arr, type(arr), arr.dtype) # <class 'numpy.ndarray'> float64
    ```
    
4. **np.random.randn(개수)**
    - 표준편차가 1이고 평균값이 0인 정규분포에서 표본 추출.
    - 개수 생략하면 랜덤값 1개 반환
    
    ```python
    print("3. randn(5)")
    arr = np.random.randn()
    arr = np.random.randn(5)
    print(arr, type(arr), arr.dtype) # <class 'numpy.ndarray'> float64
    ```
    
5. **np.random.randint( low, high, 개수 )**
    - 주어진 최소/최대 범위 안에서 임의의 난수 n개 추출
    
    ```python
    print("4. randint(1,10,3)")
    arr = np.random.randint(1,10,3) # 1~9 중 3개 값 랜덤 추출
    print(arr)
    ```
    
6. **np.random.randint( high, size=n )**
    - 0~최대(exclusive) 범위 안에서 임의의 정수 n개 반
    
    ```python
    print("4. randint(5, size=4): ")
    arr = np.random.randint(5, size=4) # 0~4 중 4개 값 랜덤 추출, [2 3 3 0] <- 복원 추출
    ```
    
7. **np.random.choice(리스트)**
    - 주어진 리스트에서 임의의 값 1개 반환
    
    ```python
    print("5. np.random.choice(['foo','bar','baz']") # 문자열 리스트도 가능
    choice_value = np.random.choice(['foo','bar','baz'])
    print(choice_value)
    ```
    
8. **np.random.shuffle(리스트)**
    - 주어진 리스트를 shuffle 함.
    - in-place(True)로 동작됨. → 자기 자신이 shuffle & 원본 영향 o
    
    ```python
    print("6. np.random.shuffle([1,3,56,7,98])")
    shuffle_value = [1,3,56,7,98]
    np.random.shuffle(shuffle_value)
    print(shuffle_value)
    ```
    

### zero / ones / empty / full

1. **np.zero(개수)**
    - 개수만큼 0으로 채움.
    - 기본 type은 float64
    - dtype=np.int32를 통해 정수형으로 변환할 수 있음.
    
    ```python
    print("1. np.zeros(5):")
    data = np.zeros(5) # 기본 실수형
    #data = np.zeros(5, dtype=np.int32) # [0 0 0 0 0] int32
    print(data, data.dtype) # [0. 0. 0. 0. 0. ] float64
    ```
    

1. **np.one(개수)**
    - 개수만큼 1.0으로 채움
    - 기본 type은 float64
    - dtype=np.int32를 통해 정수형으로 변환할 수 있음.
    
    ```python
    print("2. np.ones(5):")
    data = np.ones(5)
    # data = np.ones(5, dtype=np.int32)
    print(data , data.dtype) # [1. 1. 1. 1. 1.] float64
    ```
    
2. **np.empty(개수)**
    - 개수만큼 임의의 값으로 채워짐 =⇒ 임의의 값으로 초기화 시킨 것
    - 기본 type은 float64
    - dtype=np.int32를 통해 정수형으로 변환할 수 있음.
    
    ```python
    print("3. np.empty(3)")
    data = np.empty(3)
    data = np.empty(3, dtype=np.int32)
    print(data , data.dtype ) # [1868832878 1847620453 1965061231] int32
    ```
    
3. **np.full(개수, 값)**
    - 개수만큼 지정된 값으로 채워짐
    
    ```python
    print("4. full(5, 10)")
    data = np.full(5, 10)
    print(data) # [10 10 10 10 10]
    ```
    

### arange

1. **np.arange(n)**
    - [0, n) 범위의 정수
    - 만약 n값이 실수이면 실수값으로 반환
    
    ```python
    print("1. arange(10)")
    data = np.arange(10)  # [0,10)형식으로 표현, [는 inclusive, )는 exclusive 임
    print(data)  # [0 1 2 3 4 5 6 7 8 9]
    ```
    
2. **np.arange(n, m)**
    - [n, m) 범위의 정수
    
    ```python
    print("2. arange(1,11)")
    data = np.arange(1,11) # [1,11)형식으로 표현
    print(data) # [ 1  2  3  4  5  6  7  8  9 10]
    ```
    
3. **np.arange(n, m, step)**
    - [n, m) 범위 & step 값 고려한 정수
    
    ```python
    print("3. arange(1,11,2)")
    data = np.arange(1,11,2) # start, end(exclusive), step
    print(data) # [1 3 5 7 9]
    ```
    

1. **np.arange(n, dtype=float32)**
    - [0, n) 범위 float 값으로 반환
    
    ```python
    print("4. float으로 설정1")
    data = np.arange(5, dtype=np.float32)
    print(data) # [0. 1. 2. 3. 4.]
    ```
    
2. **np.arane(실수n)**
    - 값 자리에 실수를 입력하면 실수로 반환됨
    
    ```python
    data = np.arange(5.0)
    print(data) # [0. 1. 2. 3. 4.]
    ```
    

### linspace

- np.linspace(start, stop, [num=50, endpoint=True])
- 지정된 범례에서 균일한 간격의 값을 반환
- [start, stop] 범위 사이의 값을 num개 생성
- 기본 type은 float64
- num을 지정하지 않으면 기본은 50
- 기본적으로 stop값이 범위에 포함됨. interval [’start’, ‘stop’]
- 포함시키지 않으려면 endpoint=False로 지정한다.

1. **np.linspace(n, m, num)**
    - n <= 값 ≤ m 사이의 값을 num개 생성
    
    ```python
    data = np.linspace(0, 1, 11)
    print(data, data.dtype)  
    # [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1. ]   float64
    ```
    
2. **np.linspace(n, m, num, endpoint=True|False)**
    - n <= 값 ≤ m or  n <= 값 < m 사이의 값을 num개 생성
    
    ```python
    data = np.linspace(0, 0.9, 10, endpoint=True)
    print(data)
    # [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9] <- 0.9 포함
    ```
    
    ```python
    data = np.linspace(0, 0.9, 10, endpoint=False)
    print(data)
    # [0.   0.09 0.18 0.27 0.36 0.45 0.54 0.63 0.72 0.81] <- 0.9 미포함
    ```
    

### 벡터 삭제

- **ndarray 삭제**
    - 문법 : arr = np.delete(arr, idx|fancy|slice, axis )
    - 삭제된 새로운 배열을 반환 (in-place가 False) → 원본 유지
    - axis = None 이면 flatten 적용됨
    - slice인 경우에는 np.s_[ : : 2] 형식 사용

1. **np.delete( arr, idx )**
    
    ```python
    arr = np.array([9, 8, 7, 5, 4, 3])
    new_arr = np.delete(arr, 0)  # 0번째 값을 삭제하라. (인덱스 삭제)
    new_arr = np.delete(arr, 1)  # 1번째 값을 삭제하라. (인덱스 삭제)
    new_arr = np.delete(arr, -1)  # -1번째(뒤에서 1번째) 값을 삭제하라. / 역방향 인덱싱 가능
    print(arr)  # [9 8 7 5 4 3]
    print(new_arr)  # [8 7 5 4 3] # 새로운 복사본 생성. 원본 유지.
    ```
    

1. **np.delete( arr, fancy )**
    - fancy : 정수배열 인덱싱
    
    ```python
    arr = np.array([9, 8, 7, 5, 4, 3])
    new_arr = np.delete(arr, [0, 3, 5])  # 0, 3, 5번째 인덱스 값 삭제
    new_arr = np.delete(arr, [0, 3, 5, -2])  # 0, 3, 5, -2번째 인덱스 값 삭제 / 역방향 인덱싱 가능
    print(arr)  # [9 8 7 5 4 3]
    print(new_arr)  # [8 7 4]
    ```
    

1. **np.delete( arr, slice )**
    
    ```python
    arr = np.array([9, 8, 7, 5, 4, 3])
    new_arr = np.delete(arr, np.s_[0:4])  # 0~3 번째 인덱스 값 삭제
    print(arr)  # [9 8 7 5 4 3]
    print(new_arr)  # [4 3]
    ```
    

- **값으로 삭제**
    - np.where( (arr == 5) | (arr == 8) ) 활용하여 일치하는 인덱스를 먼저 찾고 삭제한다.
    - np.delete( arr, np.where )
        
        ⇒ np,where(arr = n) : n이 위치한 인덱스 값 array로 반환
        
    
    ```python
    arr = np.array([9,8,7,5,4,3])
    xx = np.delete(arr, np.where(arr == 5)) # 5 값 삭제
    print(arr) #[9 8 7 5 4 3]
    print(xx) # [9 8 7 4 3]
    ```
    
    <aside>
    💡 np.where(arr == 5) ⇒ array([3]) ⇒ 값 5의 위치 값
    
    xx = np.delete(arr, np.where(arr == 5))
    ⇒ xx = np.delete(arr, array([3])
    
    </aside>
    
    ```python
    arr = np.array([9,8,7,5,4,3])
    xx = np.delete(arr, np.where((arr==5)|(arr==8))) # 5 와 8 값 삭제,
    print(arr) #[9 8 7 5 4 3]
    print(xx) # [9 7 4 3]
    ```
    

### 벡터 추가 및 삽입

- **ndarray 추가**
    - 문법 : arr = np.append(arr, value, axis=None)
    - axis=None 이면 flatten 된 후에 추가 된다.
    1. **np.append( arr, value, axis )**
        
        ```python
        arr = np.array([9,8,7,5,4,3])
        new_arr = np.append(arr, [1,2,3])
        print(arr)       # [9 8 7 5 4 3]
        print(new_arr)   # [9 8 7 5 4 3 1 2 3] # 리스트 마지막에 추가됨
        ```
        
    
- **ndarray 삽입**
    - 문법 : arr = np.insert( arr, idx|fancy|slice, value, axis )
    - fancy 사용 시 value와 shape가 일치해야 한다.
    1. **np.insert( arr, idx|fancy, value, axis )**
        1. **idx 이용**
            
            ```python
            arr = np.array([9,8,7,5,4,3])
            new_arr = np.insert(arr, 0, [1,2,3])
            print(arr)  # [9 8 7 5 4 3]
            print(new_arr)  # [1 2 3 9 8 7 5 4 3]
            ```
            
        2. **fancy 이용**
            
            ```python
            arr = np.array([9,8,7,5,4,3])
            new_arr = np.insert(arr, [0,3,1], [1,2,3])  # 0->1 , 3->2, 1->3 삽입됨. 따라서 갯수가 일치해야 된다.
            print(arr)        #  [9 8 7 5 4 3]
                              #   1 9 8 7 5 4 3  <- 0에 1 삽입후
                              #   1 9 8 7 2 5 4 3  <- 3에 2 삽입후
                              #   1 9 3 8 7 2 5 4 3  <- 1에 3 삽입후
            print(new_arr)    #  [1 9 3 8 7 2 5 4 3]
            ```
            
        3. **slice 이용**
            
            ```python
            arr = np.array([9,8,7,5,4,3])
            new_arr = np.insert(arr, np.s_[0:2], [1,2])
            print(arr)  # [9 8 7 5 4 3]
                        #  1 9 8 7 5 4 3 <- 0에 1 삽입후
                        #  1 9 2 8 7 5 4 3 <- 1에 2 삽입후
            print(new_arr)  # [1 9 2 8 7 5 4 3]
            ```
            

## 2차원배열

### 2차원배열 생성

- **np.array(중첩 리스트) 이용**
    - 문법 : np.array([ [  ], [  ] ])
    
    ```python
    arr1 = [[1,2,3],[4,5,6]]
    arr2D = np.array(arr1) # 중첩리스트를 행렬 형태로 반환
    print("1. 2차원 행렬 생성: \n", arr2D, type(arr2D))  # <class 'numpy.ndarray'>
    ```
    
- **1차원을 2차원으로 변경, shape 속성 사용**
    1. **arr1D.shape = (행, 열)**  
        - 행 * 열 = ndarray 크기(size)와 일치
    
    ```python
    arr1D = np.array([1,2,3,4,5,6]) # 일반 리스트 -> 1차원배열
    print(arr1D)  # [1 2 3 4 5 6] # 1차원배열
    arr1D.shape=(2, 3) # 2행 3열 # [[1 2 3][4 5 6]]
    print("2. 1차원을 2차원으로 변경: \n", arr1D) # [[1 2 3][4 5 6]]
    ```
    
    1. **arr1D.shape(행, -1)**
        - 행 크기에 의해서 열 크기가 자동 지정됨
        
        ```python
        arr1D = np.array([1,2,3,4,5,6])
        print(arr1D)  # [1 2 3 4 5 6]
        arr1D.shape=(2, -1) # 행크기에 의해서 열크기가 자동 지정됨
        print("2. 1차원을 2차원으로 변경: \n", arr1D)
        # [[1 2 3], [4 5 6]]
        ```
        
    2. **arr1D.shape(-1, 행)**
        - 열 크기에 의해서 행 크기가 자동 지정됨
            
            ```python
            arr1D = np.array([1,2,3,4,5,6])
            print(arr1D)  # [1 2 3 4 5 6]
            arr1D.shape=(-1, 2) # 열크기에 의해서 행크기가 자동 지정됨
            print("2. 1차원을 2차원으로 변경: \n", arr1D)
            # [[1 2], [3 4], [5 6]]
            ```
            
- 다차원 shape 해석하기 ⇒ 맨 뒤에서 부터 해석
    
    ```python
    arr1D = np.array([1,2,3,4,5,6])
    arr1D.shape=(2, 3, 1) # 3행1열의 배열이 2개 겹친 형태
    print(arr1D)
    # [[[1 2 3]], [[4 5 6]]]
    arr1D.shape=(3, 1, 2) # 1행2열의 배열이 3개 겹친 형태
    print(arr1D)
    # [[[1 2]], [[3 4]], [[5 6]]]
    ```
    

### 2차원배열 속성

```python
arr1 = [[1,2,3],[4,5,6]]
arr2D = np.array(arr1)
print(arr2D, type(arr2D)) # [10, 20, 30] <class 'list'>

print("1. 2차원의 차원(dimension,axis)갯수:", arr2D.ndim) # 2 (1차원 [ )
print("2. 2차원의 각 차원의 크기(shape)-매우중요:", arr2D.shape) # tuple로 반환 (2,3)
print("3. 2차원의 총 요소 갯수(size):", arr2D.size)   # 6
print("4. 2차원의 저장 데이터 type(dtype):", arr2D.dtype) # int32 (4 byte )
```

### 랜덤함수

- 랜덤 값들을 행, 열에 맞추어(size) 반환
- 2행 3열 지정 ⇒ 2행 3열 형태의 6개 값 반환
1. **랜덤값 고정**
    
    ```python
    np.random.seed(1234)
    ```
    
2. **np.random.random( 행, 열 )**
    - 0.0 <= 값 < 1.0 사이의 임의의 float n개 랜덤값 반환.
    
    ```python
    print("1. random(size=(행,열)")
    arr = np.random.random(size=(2,3)) # size는 튜플로 지정해야 함.
    print(arr, type(arr), arr.dtype) 
    # 2*3 = 6개의 값 반환, <class 'numpy.ndarray'> float64
    ```
    
3. **np.random.rand( 행, 열 )**
    - 0~1의 균등분포에서 표본 추출
    
    ```python
    print("2. rand(행, 열)")
    arr = np.random.rand(2,3)
    print(arr, type(arr), arr.dtype)
    # 0~1 사이의 6개의 값, <class 'numpy.ndarray'> float64
    ```
    
4. **np.random.randn( 행, 열 )**
    - 표준편차가 1이고 평균이 0인 정규분포에서 표본 추출
    
    ```python
    print("3. randn(행,열)")
    arr = np.random.randn(2,3)
    print(arr, type(arr), arr.dtype) 
    # <class 'numpy.ndarray'> float64
    ```
    
5. **np.random.randint( low, high, size=(행, 열))**
    - 주어진 최소/최대(exclusive) 범위 안에서의 임의의 난수 n개 추출
    
    ```python
    print("4. randint(행,열)")
    arr = np.random.randint(1,10,size=(2,3)) # 1~9 중 2행 3열에 맞춰 값 랜덤 추출
    print(arr)
    ```
    
6. **np.random.randint(high, size=(행, 열))**
    - 0~최대(exclusive) 범위 안에서 임의의 정수 n개 반환
    
    ```python
    print("4. randint(5, size=(행,열)): ")
    arr = np.random.randint(5, size=(2,3)) # 0~4 중 2행3열에 맞춰 값 랜덤 추출
    ```
    

### zero / ones / empty / full

- **np. zero((행, 열))**
    - shape 만큼 0으로 채움
    - 기본 type은 float64 → dtype=np.int32로 type 변환 가능
    
    ```python
    print("1. np.zeros((행,열)):")
    data = np.zeros((2,3)) # 기본 실수형/2행3열
    data = np.zeros((2,3)), dtype=np.int32) <- type 변환 가능
    print(data, data.dtype) # [[0. 0. 0.] [0. 0. 0.]] float64
    ```
    
- **np.ones((행, 열))**
    - shape 만큼 1로 채움
    - 기본 type은 float64 → dtype=np.int32로 type 변환 가능
    
    ```python
    print("2. np.ones((행,열))):")
    data = np.ones((2,3))
    data = np.ones((2,3)), dtype=np.int32)
    print(data , data.dtype) # [[1. 1. 1.] [1. 1. 1.]] float64
    ```
    
- **np.empty((행, 열))**
    - shape 만큼 임의의 값으로 채워짐 ⇒ 임의의 값으로 초기화 시킨 것
    - 기본 type은 float64 → dtype=np.int32로 type 변환 가능
    
    ```python
    print("3. np.empty((행,열))")
    data = np.empty((2,9))
    data = np.empty((2,9), dtype=np.int32)
    print(data , data.dtype )
    ```
    
- **np.full((행, 열, 값))**
    - shape 만큼 지정된 값으로 채워짐
    
    ```python
    print("4. full((2,3), 10)")
    data = np.full((2,3), 10)
    print(data) # [[10 10 10] [10 10 10]]
    ```
    

### arange.reshanpe (중요)

```python
print("1. arange(10)")
data = np.arange(10).reshape(2,5) # 0~9 값을 2행 5열에 맞춰 반환
print(data)
```

### 행렬 삭제

- 문법 : np.delete(arr, idx | fancy | slice, axis = 0 | 1 | None)
- 삭제된 새로운 배열을 반환
- slice인 경우 np.s_[ : : 2] 형식 사용한다.
- axis = None 이면 flatten 적용 됨. ⇒ 값이 삭제 (default)
- axis = 0 이면 행 제거
- axis = 1 이면 열 제거

- **axis = None일 경우**
    1. **idx 이용한 삭제**
        - 2차원에서 axis 지정하지 않으면 자동으로 flatten 된다. & 값 삭제
        
        ```python
        ## 원본 2차원배열
        arr2D = np.arange(25).reshape(5,5) #0~25 값을 5행 5열로 반환
        print(arr2D)
        '''
        [[ 0  1  2  3  4]
         [ 5  6  7  8  9]
         [10 11 12 13 14]
         [15 16 17 18 19]
         [20 21 22 23 24]]
        '''
        
        xxx = np.delete(arr2D, -1) # 인덱스 -1 자리(24)가 삭제됨
        print(xxx) 
        # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
        # 마지막 값이 삭제되면서 5행 5열 형태 불가능하므로 행열 해체됨
        ```
        
        <aside>
        💡 flatten ⇒ 1행 배열에 모든 값이 들어간다.
        
        </aside>
        
    2. **fancy 이용한 삭제**
        - 2차원에서 axis 지정하지 않으면 자동으로 flatten 된다. & 값 삭제
        
        ```python
        ## 원본 2차원배열
        arr2D = np.arange(25).reshape(5,5) #0~25 값을 5행 5열로 반환
        print(arr2D)
        '''
        [[ 0  1  2  3  4]
         [ 5  6  7  8  9]
         [10 11 12 13 14]
         [15 16 17 18 19]
         [20 21 22 23 24]]
        '''
        
        xxx = np.delete(arr2D, [0,-1]) # 인덱스 0, -1 자리 값이 삭제됨 (0,24 삭제)
        print(xxx)  # [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
        # 두 값이 삭제되면서 5행 5열 형태 불가능하므로 행열 해체됨
        ```
        
    3. **slice 이용한 삭제**
        - 2차원에서 axis 지정하지 않으면 자동으로 flatten 된다. & 값 삭제
        
        ```python
        ## 원본 2차원배열
        arr2D = np.arange(25).reshape(5,5) #0~25 값을 5행 5열로 반환
        print(arr2D)
        '''
        [[ 0  1  2  3  4]
         [ 5  6  7  8  9]
         [10 11 12 13 14]
         [15 16 17 18 19]
         [20 21 22 23 24]]
        '''
        xxx = np.delete(arr2D, np.s_[:8]) # 0~7 값 삭제
        print(xxx) # [ 8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24]
        ```
        
- **axis = 0 인 경우**
    1. **idx + axis = 0 이용한 삭제**
        
        ```python
        # arr2D 원본
        '''
        [[ 0  1  2  3  4]
         [ 5  6  7  8  9]
         [10 11 12 13 14]
         [15 16 17 18 19]
         [20 21 22 23 24]]
        '''
        xxx = np.delete(arr2D, -1, axis=0) # -1 : 마지막, axis=0 : 행 삭제
        print(xxx)
        '''
        [[ 0  1  2  3  4]
         [ 5  6  7  8  9]
         [10 11 12 13 14]
         [15 16 17 18 19]]
        '''
        ```
        
    2. **fancy + axis = 0 이용한 삭제**
        
        ```python
        # arr2D 원본
        '''
        [[ 0  1  2  3  4]
         [ 5  6  7  8  9]
         [10 11 12 13 14]
         [15 16 17 18 19]
         [20 21 22 23 24]]
        '''
        xxx = np.delete(arr2D, [0,-1], axis=0) # [0,-1] : 0, -1번째, axis=0 : 행 삭제
        print(xxx)
        '''
        [[ 5  6  7  8  9]
         [10 11 12 13 14]
         [15 16 17 18 19]]
        '''
        ```
        
    3. **slice + axis = 0 이용한 삭제**
        
        ```python
        # arr2D 원본
        '''
        [[ 0  1  2  3  4]
         [ 5  6  7  8  9]
         [10 11 12 13 14]
         [15 16 17 18 19]
         [20 21 22 23 24]]
        '''
        xxx = np.delete(arr2D, np.s_[:3], axis=0) # np.s_[:3] : 0~2번째, axis=0 : 행 삭제
        print(xxx)
        '''
        [[15 16 17 18 19]
         [20 21 22 23 24]]
        '''
        ```
        
- **axis = 1 인 경우**
    1. **idx + axis=1 이용한 삭제 ==> 열이 삭제됨**
        
        ```python
        # arr2D 원본
        '''
        [[ 0  1  2  3  4]
         [ 5  6  7  8  9]
         [10 11 12 13 14]
         [15 16 17 18 19]
         [20 21 22 23 24]]
        '''
        xxx = np.delete(arr2D, -1, axis=1) # -1 : 마지막, axis=1 : 열 삭제
        print(xxx)
        '''
        [[ 0  1  2  3]
         [ 5  6  7  8]
         [10 11 12 13]
         [15 16 17 18]
         [20 21 22 23]]
        '''
        ```
        
    2. **fancy + axis=1 이용한 삭제**
        
        ```python
        # arr2D 원본
        '''
        [[ 0  1  2  3  4]
         [ 5  6  7  8  9]
         [10 11 12 13 14]
         [15 16 17 18 19]
         [20 21 22 23 24]]
        '''
        xxx = np.delete(arr2D, [0,-1], axis=1) # [0,-1] : 0,-1번째, axis=1 : 열삭제
        print(xxx)
        '''
        [[ 1  2  3]
         [ 6  7  8]
         [11 12 13]
         [16 17 18]
         [21 22 23]]
        '''
        ```
        
    3. **slice + axis=1 이용한 삭제**
        
        ```python
        # arr2D 원본
        '''
        [[ 0  1  2  3  4]
         [ 5  6  7  8  9]
         [10 11 12 13 14]
         [15 16 17 18 19]
         [20 21 22 23 24]]
        '''
        xxx = np.delete(arr2D, np.s_[:3], axis=1)
        print(xxx)
        '''
        [[ 3  4]
         [ 8  9]
         [13 14]
         [18 19]
         [23 24]]
        '''
        ```
        

### 행렬 추가 및 삽입

- **ndarray 추가 (append)**
    - 문법 : np.append(arr, value, axis=None)
    - 추가된 새로운 배열을 반환
    - axis=None 이면 flatten 된후에 추가된다.
    - axis=0 이면 행 추가. 반드시 shape가 일치해야 된다.
    - axis=1 이면 열 추가. 반드시 shape가 일치해야 된다.
    
    1. **axis = None 지정한 추가**
        
        ```python
        arr = np.array([[1,2,3],[4,5,6]])
        '''
        [[1 2 3]
         [4 5 6]]
        '''
        xxx = np.append(arr, [100,200,300,400])
        print(xxx)  # [  1   2   3   4   5   6 100 200 300 400]
        ```
        
        <aside>
        💡 2차원에서 axis 지정하지 않으면 flatten 되어 추가됨.
        따라서 size가 일치하지 않아도 된다.
        
        </aside>
        
    2. **axis=0 지정한 추가 ==> 행 추가**
        
        ```python
        arr = np.array([[1,2,3],[4,5,6]])
        '''
        [[1 2 3]
         [4 5 6]]
        '''
        xxx = np.append(arr, [[100,200,300]], axis=0) # 원본(3열)과 shape 일치해야 함.
        print(xxx)
        '''
        [[  1   2   3]
         [  4   5   6]
         [100 200 300]]
        '''
        ```
        
        <aside>
        💡 행을 추가할 때 원본 배열이 ‘3열’ 이므로 추가할 배열도 ‘3열’로 일치해야 한다.
        
        </aside>
        
    3. **axis=1 지정한 추가 ==> 열 추가**
        
        ```python
        arr = np.array([[1,2,3],[4,5,6]])
        '''
        [[1 2 3]
         [4 5 6]]
        '''
        xxx = np.append(arr, [[100],[200]], axis=1) # 원본(2행)과 shape 일치해야 함.
        print(xxx)
        '''
        [[  1   2   3 100]
         [  4   5   6 200]]
        '''
        ```
        
        <aside>
        💡 열을 추가할 때 원본 배열이 ‘2행’ 이므로 추가할 배열도 ‘2행’으로 일치해야 한다.
        
        </aside>
        
    4. **axis = None 지정한 추가**
        
        ```python
        arr = np.array([[1,2,3],[4,5,6]])
        '''
        [[1 2 3]
         [4 5 6]]
        '''
        xxx = np.append(arr, [100,200,300,400])
        print(xxx)  # [  1   2   3   4   5   6 100 200 300 400]
        ```
        
        <aside>
        💡 2차원에서 axis 지정하지 않으면 flatten 되어 추가됨.
        따라서 size가 일치하지 않아도 된다.
        
        </aside>
        
- **ndarray 삽입 (insert)**
    - 문법 : np.insert( arr, idx | fancy, value, axis )
    - fancy 사용시 value와 shape가 일치해야 한다.
    
    1. **axis = None 지정한 삽입**
        
        ```python
        arr = np.array([[1,2,3],[4,5,6]])
        '''
        [[1 2 3]
         [4 5 6]]
        '''
        xxx = np.insert(arr, 0,  [100,200,300,400])
        print(xxx)  # [100 200 300 400   1   2   3   4   5   6]
        ```
        
        <aside>
        💡 2차원에서 axis 지정하지 않으면 flatten 되어 추가됨.
        따라서 shape 일치하지 않아도 된다.
        
        </aside>
        
    2. **axis=0 지정한 삽입 ==> 행 삽입**
        
        ```python
        arr = np.array([[1,2,3],[4,5,6]])
        '''
        [[1 2 3]
         [4 5 6]]
        '''
        xxx = np.insert(arr, 0,  [[100,200,300]], axis=0) # 원본(3열)과 shape 일치해야 함.
        print(xxx)
        '''
        [[100 200 300]
         [  1   2   3]
         [  4   5   6]]
        '''
        ```
        
        <aside>
        💡 행을 추가할 때 원본 배열이 ‘3열’ 이므로 추가할 배열도 ‘3열’로 일치해야 한다.
        
        </aside>
        
    3. **axis=1 지정한 삽입 ==> 열 삽입**
        
        ```python
        arr = np.array([[1,2,3],[4,5,6]])
        '''
        [[1 2 3]
         [4 5 6]]
        '''
        xxx = np.insert(arr, 0, [[100],[200]], axis=1) # 원본(2행)과 shape 일치해야 함.
        print(xxx)
        ```
        
        <aside>
        💡 열을 추가할 때 원본 배열이 ‘2행’ 이므로 추가할 배열도 ‘2행’으로 일치해야 한다.
        
        </aside>
        

## 타입 변경

- 타입변경 ⇒ 다차원 배열의 모든 요소가 한꺼번에 변경된다. (벡터화 연산)
- dtype 속성 이용
- astype 속성 이용 (기억)

### int → float64

```python
data = [10,20,30] # 일반 리스트
arr1 = np.array(data) # 1차원배열로 변환
arr2 = np.array(data , dtype=np.float64) # 가. dtype 속성 이용
arr3 = arr1.astype(np.float64)           # 나. astype 함수 이용
print("1. 원본 데이터: ", arr1.dtype , arr1)  # int32 [10 20 30]
print("2. int값을 float으로 변경 1: ", arr2.dtype , arr2)  # float64 [10. 20. 30.]
print("2. int값을 float으로 변경 2: ", arr3.dtype , arr3)  # float64 [10. 20. 30.]
```

### float64 → int64

```python
data = [10.5,20.7,30.23] # 실수형 값이 있는 리스트
arr1 = np.array(data) # 1차원배열로 변환
arr2 = np.array(data , dtype=np.int64) # 가. dtype 속성 이용
arr3 = arr1.astype(np.int64)           # 나. astype 함수 이용
print("3. 원본 데이터: ", arr1.dtype , arr1)  # float64 [10.5  20.7  30.23]
print("4. float 값을 int 으로 변경 1: ", arr2.dtype , arr2) # int64 [10 20 30]
print("4. float 값을 int 으로 변경 2: ", arr3.dtype , arr3) # int64 [10 20 30]
print()
```

### int → byte, str

```python
data = [10,20,30]
arr1 = np.array(data)
arr2 = np.array(data , dtype=np.string_)  # bytes 타입,  np.string 안됨.
arr3 = arr1.astype(np.string_)
arr4 = np.array(data , dtype=np.str_)   # str 타입 , dtype=np.str 가능
arr5 = arr1.astype(np.str_)
print("5. 원본 데이터: ", arr1.dtype , arr1)  # int32 [10 20 30]
print("6. int 값을 bytes 으로 변경 1: ", arr2.dtype , arr2) # |S2 [b'10' b'20' b'30']
print("6. int 값을 bytes 으로 변경 2: ", arr3.dtype , arr3) # |S11 [b'10' b'20' b'30']
print("7. int 값을 str 으로 변경 : ", arr4.dtype , arr4) # <U2 ['10' '20' '30']
print("7. int 값을 str 으로 변경 : ", arr5.dtype , arr5) # <U11 ['10' '20' '30']
```

### str → int

```python
data =['10','20','30']
arr1 = np.array(data)
arr2 = arr1.astype(np.int32)
print("8. str 값을 int 으로 변경 :",arr2) # [10 20 30]
```

```python
arr3 = np.array(data).astype(np.int32) # 권장 (arr1+arr2)
print(arr3) # [10 20 30]
```

## 벡터 함수

### 기존 python 연산

```python
print("1. 파이썬의 리스트 + 리스트")
print([10,20,30]+[10,20,30])  #[10, 20, 30, 10, 20, 30]
```

<aside>
💡 리스트+리스트 ⇒ 하나의 리스트로 병합됨

</aside>

```python
print("2. 기본 파이썬의 리스트 * 스칼라(값)")
# print([10,20,30] + 2)  # TypeError: can only concatenate list (not "int") to list
print([10,20,30] * 3)  # [10, 20, 30, 10, 20, 30, 10, 20, 30]
```

<aside>
💡 리스트 * 수치값 ⇒ 리스트 안의 값들이 수치값만큼 반복됨

</aside>

### 벡터 연산

- 기존 파이썬에서 지원되지 않는 요소 간의 연산을 numpy는 지원한다.
- 다차원 배열 간 연산, 다차원 배열과 스칼라 연산
- 비교 연산도 가능 ⇒ 논리값(True, False) 반환 ⇒ boolean 색인 (중요)
    
    ⇒ 파이썬 : and, or, not / numpy : &, |, ~
    
- 브로드캐스팅(broadcasting)
    
    ⇒ 서로 다른 차원을 가지고 있는 두 개의 값을 산술하는 도중, 연산이 가능하도록 차원을 자동으로 맞춰주는 작업
    
1. **다차원배열 + 다차원배열 ⇒ 요소간 연산, 반드시 shape 일치해야 한다.**
    
    ```python
    arr1D_1 = np.array([10,20,30])
    arr1D_2 = np.array([5,4,3])
    print("3. numpy의 벡터간 연산 처리")
    print(arr1D_1 + arr1D_2)  # [15 24 33]
    print(arr1D_1 - arr1D_2)  # [ 5 16 27]
    print(arr1D_1 * arr1D_2)  # [50 80 90]
    print(arr1D_1 / arr1D_2)  # [ 2.  5. 10.] # 실수형 반환
    ```
    
2. **다차원배열 + 스칼라 ⇒ 자동으로 브로드캐스팅 되어 연산됨**
    
    ```python
    arr1D_1 = np.array([10,20,30])
    print("4. numpy의 벡터 + 스칼라 연산 처리")
    print(arr1D_1 + 2)  # [12 22 32]
    print(arr1D_1 - 2)  # [ 8 18 28]
    print(arr1D_1 * 2)  # [20 40 60]
    print(arr1D_1 / 2)  # [ 5. 10. 15.]
    ```
    
3. **비교 연산도 벡터화 가능 ⇒ boolean 색인 적용 가능**
    
    ```python
    arr1D_1 = np.array([10,20,30])
    print("5. 벡터의 비교 연산처리1: ", arr1D_1%3 == 0)
    # [False False  True]
    print("5. 벡터의 비교 연산처리2: ", arr1D_1 > 15) 
    # [False  True  True]
    print("5. 벡터의 비교 연산처리3: ", (arr1D_1 > 15) & ( arr1D_1%6 == 0)) 
    # [False False  True]
    ```
    
    <aside>
    💡 각 요소들을 비교 연산하여 논리값을 반환한다.
    
    </aside>
    

## 색인

- **1차원 배열 색인**
    - python의 인덱싱/슬라이싱 모두 가능
    - fancy 색인
    - boolean 색인
        
        ⇒ 반드시 색인 대상(요소)과 길이가 같아야 한다.
        

### indexing (순방향, 역방향)

```python
arr = np.arange(10)
print(arr)
# [0 1 2 3 4 5 6 7 8 9]

rint(arr[0], arr[-1]) # 0 9 
```

<aside>
💡 값으로 반환

</aside>

### slicing

```python
arr = np.arange(10)
print(arr)
# [0 1 2 3 4 5 6 7 8 9]

print(arr[1:5]) # [1 2 3 4]
print(arr[:5]) # [0 1 2 3 4]
print(arr[1:]) # [1 2 3 4 5 6 7 8 9]
print(arr[1:10:2]) # [1  3  5  7  9]
print(arr[:]) # [0 1 2 3 4 5 6 7 8 9]
```

```python
print(arr[...]) # [0 1 2 3 4 5 6 7 8 9] <- arr[:] 와 동일
```

<aside>
💡 1차원배열로 반환
arr[…] ⇒ 자주 쓰임

</aside>

### fancy

```python
data = np.arange(10) * 100
print("1. original: ", data)
# [  0 100 200 300 400 500 600 700 800 900]
# print(data[1,3,5]) # 주의 꼭 대괄호 넣어서 실행해야 함.
print("2. data[[1,3,5]]: ", data[[1,3,5]]) # [100 300 500]
print("3. data[[8,1,5]]: ", data[[8,1,5]]) # [800 100 500]
# 인덱싱한 순서대로 반환됨.
```

<aside>
💡 1차원배열로 반환됨
인덱싱한 순서대로 반환됨

</aside>

### boolean

```python
data = np.array([1,2,3,4,5])
print("1. original: " , data) # [1 2 3 4 5]
print("2. 벡터연산,  data%2==0: " , data%2==0) 
# [False  True False  True False]
print("3. boolean 색인, [True,True,True,True,False]: ",data[[True,True,True,True,False]]) # [1 2 3 4] => True인 값만 반환
```

<aside>
💡 boolean색인 ⇒ 반드시 색인 대상 (요소)과 길이가 같아야 한다.
True인 값만 반환됨

</aside>

```python
print("4. boolean 색인 활용,data[data%2==0]: ",data[data%2==0])  
# [2 4]
print("5. boolean 색인 활용,data[data > 3 ]: ",data[data > 3])  
# [4 5]
print("6. boolean 색인의 & 연산자: " , data[(data%2==0) & (data >2)]) 
# [4]
print("7. boolean 색인의 | 연산자 " , data[(data%2!=0) | (data < 4)]) 
# [1 2 3 5]
print("8. boolean 색인 ~ 연산자: ",data[~(data > 3)])  
# [1 2 3]
```