# Machine Learning

# 개요

## 개요

- 데이터에서 지식을 추출하는 작업
- 코딩하지 않고 예제를 통해 학습할 수 있는 시스템
- 경험을 통해 데이터 기반으로 학습하고 예측
- 데이터로부터 유용한 규칙 등을 추출하는 기능

## 학습 개념

- 간단한 예
    
    입력과 출력이 여러 개의 데이터 쌍으로 주어짐.
    
    (1,2), (2,4), (4,8) …
    
    학습 후 출력이 입력의 2배임을 유추
    
    (3,?), (8,?) ⇒ 6, 16 등으로 답변
    

## 머신러닝과 프로그래밍의 차이점

- 프로그래밍에서는 모든 규칙들을 작성함
→ 만약 규칙들이 추가로 작성될 경우 유지 관리가 어려움
그러나 머신러닝은 시간에 따라 점차 효율이 향상됨
- 입출력 데이터의 관계를 학습하여 규칙을 생성
- 프로그래밍에서는 데이터와 규칙이 결합하여 출력을 생성
그러나 머신러닝에서는 데이터와 출력이 함께 들어가서 규칙 생성
    
    ![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled.png)
    

## 머신러닝과 인공지능과의 관계

- 머신러닝은 인공지능에 속하는 부분 집합
- 추구하는 개념과 목표가 다소 다름
- 인공지능은 추론, 계획 등과 머신러닝을 포함

![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%201.png)

- 머신러닝은 데이터로부터 학습하여 지식을 획득
- 인공지능은 지식을 획득한 후 그것을 활용
    
    
    |  | 머신러닝 | 인공지능 |
    | --- | --- | --- |
    | 주요 활동 | 학습을 통한 지식의 획득 | 지식의 획득과 활용 |
    | 구현과 실현 | 데이터로부터의 학습 실현 | 복잡한 문제 해결을 위한 지능의 구현 |
    | 개발 목표 | 스스로 학습하는 알고리즘 | 인간을 닮은 지능적인 시스템의 개발 |

## 머신러닝 과정에서의 고려 사항

- 주어진 데이터로부터 원하는 답을 찾을 수 있을까?
- 문제 해결을 위해 데이터가 충분한가?
- 어떤 머신러닝 기법을 적용하면 좋을까?
- 추출할 데이터의 특성은 무엇인가?
- 머신러닝의 결론은 무엇으로 설정할 것인가?
- 생성된 출력을 실제 응용에 어떻게 사용할 것인가?

## 머신러닝의 주요 종류

- 신경망(Neural Network) : 생물의 신경 네트워크 구조와 기능을 모방한 모델
- 클러스터링(Clustering) : 주어진 데이터를 클러스터라는 부분 집합들로 분리
- 분류(Classification) : 주어진 데이터를 비슷한 것들끼리 분류
- 의사결정 트리(Decision Tree) : 트리 구조 형태의 예측 모델로 의사를 결정
- 나이브 베이즈(Naive Bayes) : 베이즈 정리를 바탕으로 한 조건부 확률 모델 분류

# 머신러닝의 학습 방법

## 머신러닝의 학습 방법

- 학습 형태에 따라 3가지 학습 방법이 있다.
- 지도 학습, 비지도 학습, 강화 학습으로 구분
    
    ![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%202.png)
    
- 머신러닝의 학습 방법과 활용 분야 체계
    
    ![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%203.png)
    

## 지도 학습

### **지도학습이란?**

- **정답이 있는 데이터**를 활용해 데이터를 학습
- 입력 값(X data)이 주어지면 입력값에 대한 Label(Y data)를 주어 학습
- 대표적으로 분류, 회귀 문제가 있다.

### **지도학습의 장단점**

- **장점**
    - 이전의 경험으로부터 데이터 출력을 생성
    - 성능 기준을 최적화
    - 다양한 유형의 문제 해결에 도움이 됨
- **단점**
    - 출력에 반드시 레이블이 있는 데이터들을 사용해야 함.
    - 일반적으로 많은 시간이 걸림

### **분류(classification)**

- 주어진 데이터를 정해진 카테고리(라벨)에 따라 분류하는 문제
- 맞다, 아니다 등의 **이진 분류 문제** 또는 사과다 바나나다 포도다 등의 2가지 이상으로 분류하는 **다중 분류 문제**
- ex) 스팸메일 분류, 이미지 분류, 손으로 쓴 주소 판별, 종양 여부 판단

### **주요 분류 방법**

- **Naive Bayes 분류기**
    - 자료의 분류를 베이즈 정리를 활용하여 판단ㄴ
    - 나이브 베이즈 분류기는 조건부 확률 모델
    - 모든 특성값은 서로 독립이라고 가정
    - 구축이 쉽고 대규모 데이터셋에 유용
    - 지도 학습 환경에서 효율적으로 훈련될 수 있음
- **의사결정 트리(Decision Tree)**
    - 관측값과 목표값을 연결하는 예측 모델
    - 최대 2가지의 판단을 하는 이진 트리 사용
    - 스무고개 문답처럼 선택 방법으로 진행
    - 주택이나 자동차 구입 비용 등의 추정에 활용
- **SVM(Support Vector Machine : SVM)**
    - 데이터를 2개의 영역으로 분류하는 이진 분류기
    - 새로운 데이터가 어느 영역에 속하는지를 판단
    - 가장 큰 폭을 가진 하나의 경계선을 찾는 알고리즘
    - 분류, 회귀, 멀티미디어 정보 검색 등에 사용
- **K-Nearest Neighbor(K-NN)**
    - 간단한 분류 기법
    - 최근접 이웃 분류라고도 불림
    - 가장 가까운 것들과의 거리 계산으로 클래스 분류
    - 이웃 데이터들의 클래스 중 다수결로 데이터의 클래스 결정
    - 다수결에서 결과가 나오기 위해 k는 반드시 홀수여야 함.
    - 영화나 음악 추천에 대한 개인별 선호 예측
    - 얼굴인식
    - 질병의 질단과 유전자 데이터 인식
    - 재정 위험성 파악, 주식 시장 예측

### **회귀(regression)**

- 어떤 데이터들의 Feature를 기준으로, 연속된 값(그래프)을 예측하는 문제
- 주로 어떤 패턴이나 트렌드, 경향을 예측할 때 사용
- 하나의 독립 변수를 사용하는 직선 형태의 ‘선형 회귀’
- 회귀 분석
    - 변수 사이의 회귀에 대해 검정이나 추정
    - 학습 데이터를 사용하여 출력값 예측
    - 산출물은 항상 확률론적 의미를 내포
- ex) 날씨 예측, 판매액 예측, 주택 가격 예측, 원유 가격 추정

### **분류와 회귀의 차이점**

- 분류는 일정한 기준에 따라 명백하게 구분 짓는 것
- 회귀는 오차 제곱의 합을 최소화하는 직선을 긋는 작업
(명확히 직선으로 구별되는 것이 아님)
- 출력값 차이
    - 분류 : 남자/여자 등 선택식 출력 & “내일 날씨는 덥다”와 같이 이분법적 선택
    - 회귀 : 연속값으로 나타냄. “내일 기온?”에 대해 “18.3도로 추정”으로 출력

## 비지도 학습

- 출력값을 알려주지 않고 스스로 모델을 구축하여 학습
- **정답 라벨이 없는 데이터**를 비슷한 특징끼리 **군집화** 하여 새로운 데이터에 대한 결과를 예측하는 방법
- 입력만 있고 출력(Label)이 없음
- 규칙성을 스스로 찾아내는 것이 학습의 주 목표
- 지도 학습에서 적절한 피처를 찾아내기 위한 전처리 방법으로 비지도 학습을 이용하기도 함.
- 대표적인 종류로 클러스터링(Clustering)이 있음.
- ex) 비슷한 성향의 고객 그룹으로 묶기, 블로그에서  주제별로 구분하기, 유사한 꽃이나 동물들끼리 묶기, 네트워크상의 비정상적인 접근의 탐지

### **클러스터와 클러스터링**

- 클러스터는 유사한 여러 개의 클래스로 나누어진 데이터
- 클러스터링은 유사한 특성을 가진 그룹들로 묶는 작업
- 같은 클러스터의 것은 다른 클러스터의 것보다 더 유사
- 분류와 클러스터링의 차이점
    - 분류는 지도 학습, 클러스터링은 비지도 학습 영역
    - 분류는 데이터를 기준에 따라 직선으로 분류하는 것
    - 클러스터링은 유사성에 따라 몇 개의 클러스터로 묶는 것

### **주요 비지도 학습 방법**

- **k-means 클러스터링**
    - 비지도 학습 알고리즘 중 대표적인 클러스터링 방법
    - 우리말로 ‘K-평균 군집화’라고 함
    - 유사한 특성을 가진 k개의 데이터 그룹으로 묶는 방법
    - 알고리즘이 비교적 간단하고, 수행 속도가 빠르다.
    - 클러스터링의 개수 k와 최초로 지정하는 중심점들에 따라 결과
    가 다소 달라질 수 있다.
    - ex) 성향 분석, 고객 분류, 신용카드 사기 탐지, 매출 기반 회사 등급 분류, 폭풍 예측
- **추천 시스템(Recommender System)**
    - 사용자의 ‘선호도’를 예측하는 정보 필터링의 일종
    - 상업적으로 활용 중

## 지도 학습과 비지도 학습의 특징 비교

| 기반 | 지도 학습 | 비지도 학습 |
| --- | --- | --- |
| 입력 데이터 | 입출력(값 또는 레이블)이 지정된 데이터를 사용하여 학습함. | 출력값이나 레이블이 전혀 없는 데이터를 사용하여 학습함. |
| 주요 기능 | 분류, 회귀 | 클러스터링, 추천 시스템 |
| 계산의 복잡성 | 비교적 간단함 | 상당히 복잡함 |
| 정확성 | 매우 정확함 | 다소 덜 정확함 |

## 강화 학습

- 주어진 입력에 대응하는 행동에 대해 보상(reward)을 통해 학습
- 주어진 입력에 대한 출력, 즉 정답 행동이 주어지지 않음.
- 주요 응용 분야로 로봇, 게임, 내비게이션 등이 있다.

# 머신러닝을 위한 용어 정리

[https://wikidocs.net/book/5942](https://wikidocs.net/book/5942)

## Feature (속성, attribute)

- 머신러닝이나 데이터 분석에 사용되는 개별 독립 변수
- 학습 및 예측을 할 데이터의 특징, 항목
- Feature와 Attribute는 같은 용어로 이용된다.
- ex) 질병 유무 판단
키, 몸무게, 성별, 나이, 혈압, 식습관 등이 feature가 될 수 있다.

## Label (class, target, 결정값)

- 예측하고자 하는 대상 항목

![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%204.png)

# 사이킷런

## 사이킷런이란?

- 머신러닝을 위한 매우 다양한 알고리즘과 개발을 위한 편리한 프레임워크와 API를 제공
- 파이썬 기반의 다른 머신러닝 패키지도 사이킷런 스타일의 API를 지향할 정도로 쉽고 가장 파이썬스러운 API를 제공
- [https://scikit-learn.org/stable/](https://scikit-learn.org/stable/)
- 사이킷런으로 모델을 구축시, 해결할 문제에 따른 적절한 알고리즘
    
    ![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%205.png)
    

## 사이킷런 기반 프레임워크

- Estimate와 fit( ), predict( )
    
    ![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%206.png)
    
    - 분류 구현 클래스
        - DecisionTreeClassifier
        - RandomForestClassifier
        - GradientBoostingClassifier
        - GaussianNB
        - SVC
    - 회귀 구현 클래스
        - LinearRegression
        - Ridge
        - Lasso
        - RandomForestRegressor
        - GrandientBoostingRegressor

## ****사이킷런의 주요 모듈****

![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%207.png)

## 사이킷런 내장 예제 데이터셋

- 분류 및 회귀용
    
    
    | API명 | 설명 |
    | --- | --- |
    | datasets.load_boston() | 회귀 용도, 미국 보스턴의 집 피처들과 가격에
    대한 데이터 세트 |
    | datasets.load_breast_cancer() | 분류 용도. 위스콘신 유방암 피처들과 악성/음성
    레이블 데이터 세트 |
    | datasets.load_diabetes() | 회귀 용도. 당뇨 데이터 세트 |
    | datasets.load_digits() | 분류 용도. 0~9까지 숫자의 이미지 픽셀 데이터
    세트 |
    | datasets.load_iris() | 분류 용도. 붓꽃 데이터 피처를 가진 데이터 세
    트 |
- 내장 예제 데이터셋 구성
    
    ![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%208.png)
    

# iris 데이터 분류 예측 프로세스 실습

## 예측 전

- 목적 : 붓꽃 데이터 세트는 꽃잎의 길이와 너비, 꽃받침의 길이와 너비 피처
(Feature)을 기반으로 꽃의 품종을 예측
- Feature : Sepal length, Sepal width, Petal length, Petal width
- Label :  iris setosa, iris versicolor, iris virginica
- 학습데이터
    
    ![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%209.png)
    
- 테스트 데이터
    
    ![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%2010.png)
    
- 분류 예측 프로세스
    
    ![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%2011.png)
    
    - 데이터 세트 분리 : 데이터를 training data와 test data로 분리
    - 모델 학습 : training data를 기반으로 ML 알고리즘을 적용하여 모델을 학습
    - 예측 수행 : 학습된 ML 모델을 이용해 test data의 분류를 예측
    - 평가 : 이렇게 예측된 결과값과 test data의 실제 결괏값을 비교해 ML 성모델 성능을 평가

## 예측

### **데이터 세트를 로딩**

- **사이킷런에 필요한 모듈 로딩**
    
    ```python
    from sklearn.datasets import load_iris
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import train_test_split
    ```
    
- **데이터셋 로딩 & 데이터 정보 확인**
    
    ```python
    # 붓꽃 데이터 세트를 로딩
    iris = load_iris()
    
    # dir()는 객체가 어떤 변수와 메서드를 가지고 있는지 나열함
    print(type(dir(iris))) 
    
    # 메서드 확인
    print(iris.keys())
    
    # shape는 배열의 형상 정보를 출력
    print(iris_data.shape)
    
    # 각 label의 이름
    print(iris.target_names)
    
    # 각 feature의 이름
    print(iris.feature_names)
    ```
    
    <aside>
    <img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> <class 'list'>
    dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename', 'data_module'])
    (150, 4)
    ['setosa' 'versicolor' 'virginica']
    ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
    
    </aside>
    

### **DataFrame 자료형으로 변환**

```python
import pandas as pd

# iris.data는 iris 데이터 세트에서 피처(feature)만으로 된 데이터를 numpy로 가지고 있다.
iris_data = iris.data

# iris.target은 iris 데이터 세트에서 레이블(결정 값) 데이터를 numpy로 가지고 있다.
# iris 데이터 세트에서 피처들에 해당하는 열의 이름
iris_label = iris.target
print('iris target값 :', iris_label)
print('iris target명 :', iris.target_names)

# iris 데이터 세트를 자세히 보기 위해 DataFrame으로 변환
iris_df = pd.DataFrame(data=iris_data, columns=iris.feature_names)
iris_df['label'] = iris.target
iris_df.head(3)
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> iris feature 데이터 값 :
 [[5.1 3.5 1.4 0.2]
 [4.9 3.  1.4 0.2]
 [4.7 3.2 1.3 0.2]
 [4.6 3.1 1.5 0.2]
…
[6.7 3.  5.2 2.3]
 [6.3 2.5 5.  1.9]
 [6.5 3.  5.2 2. ]
 [6.2 3.4 5.4 2.3]
 [5.9 3.  5.1 1.8]]

iris target 데이터 값 : [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0  0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2]

iris target명 : ['setosa' 'versicolor' 'virginica']

![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%2012.png)

</aside>

### **train, test 데이터셋 분리**

학습용 데이터와 테스트용 데이터는 반드시 분리해야 한다. 학습 데이터로 학습된 모델이 얼마나 뛰어난 성능을 가지는지 평가하려면 테스트 데이터 세트가 필요하기 때문.

```python
X_train, X_test, y_train, y_test = train_test_split(iris_data, iris_label, test_size=0.2, random_state=11)

print('X_train 개수: ', len(X_train),', X_test 개수: ', len(X_test))
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> X_train 개수:  120 , X_test 개수:  30

</aside>

- 문제지 : 머신러닝 모델에게 입력되는 데이터. **feature**라고 부르기도 한다. 변수 이름으로는 `X`를 많이 사용한다.
- 정답지 : 머신러닝 모델이 맞혀야 하는 데이터. **label** 또는 **target**이라고 부르기도 한다. 변수 이름으로는 `y`를 많이 사용한다.
- 첫 번째 파라미터 iris_data : 피처(Feature) 데이터 세트
- 두 번째 파라미터 iris_label : 레이블(Label) 데이터 세트
- test_size : 전체 데이터 세트 중 테스트 데이터 세트의 비율
- random_state :  호출할 때마다 같은 학습/테스트용 데이터 세트를 생성하기 위해 주어지는 난수 발생 값

### ****테스트 데이터 세트로 학습(Train) 수행****

- 예측은 반드시 학습 데이터가 아닌 다른 데이터를 이용해야 하며, 일반적으로 테스트 데이터 세트를 이용
- DecisionTreeClassifier 객체의 predict( ) 메서드에 테스트용 피처 데이터 세트를 입력해 호출하면 학습된 모델 기반에서 테스트 데이터 세트에 대한 예측값을 반환하게 된다.

```python
# Decision Tree 사용하기
# DecisionTreeClassifier 객체 생성
dt_clf = DecisionTreeClassifier(random_state=11)

# dt_clf 의 type 확인
print(dt_clf._estimator_type)

# 학습수행
dt_clf.fit(X_train, y_train)
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> classifier

DecisionTreeClassifier(random_state=11)

</aside>

### **테스트 데이터 세트로 예측(Predict) 수행**

```python
# 학습이 완료된 DecisionTreeClassifier 객체에서 테스트 데이터 세트로 예측 수행
pred = dt_clf.predict(X_test)
print(pred)

from sklearn.metrics import classification_report
print(classification_report(y_test, pred))
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> [2 2 1 1 2 0 1 0 0 1 1 1 1 2 2 0 2 1 2 2 1 0 0 1 0 0 2 1 0 1]
              precision    recall  f1-score   support

           0       1.00      1.00      1.00         9
           1       0.83      1.00      0.91        10
           2       1.00      0.82      0.90        11

    accuracy                           0.93        30
   macro avg       0.94      0.94      0.94        30
weighted avg       0.94      0.93      0.93        30

</aside>

### **예측 정확도 평가**

- 정확도는 예측 결과가 실제 레이블 값과 얼마나 정확하게 맞는지를 평가하는 지표
- 사이킷런은 정확도 측정을 위해 accuracy_score( ) 함수를 제공
- 첫 번째 파라미터 : 실제 레이블 데이터 세트
- 두 번째 파라미터 : 예측 레이블 데이터 세트

```python
from sklearn.metrics import accuracy_score
print('예측 정확도: {0:.4f}'.format(accuracy_score(y_test,pred)))
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> 예측 정확도: 0.9333

</aside>

![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%2013.png)

# 교차 검증

## 교차 검증이란?

- 학습 데이터세트를 다시 `학습 데이터세트` / `검증 데이터세트`로 나눔
    - 학습 데이터 세트 : 학습을 위한 데이터
    - 검증 데이터 세트 : 학습된 모델의 성능을 일차 평가
    - 평가 데이터 세트 : 모든 학습/검증 과정이 완료된 후 최종적으로 성능을 평가
- 검증 데이터 세트가 필요한 이유?
    - train 데이터에 대해서 발생하는 과적합(Overfitting)을 방지하기 위해
    - train 데이터에만 열심히 학습 시켰는데, 막상 test 데이터에서는 맞지 않을 수 있기 때문에 우선 검증 데이터로 평가
    - 교차검증은 검증을 여러번 해서 어느 데이터에서나 잘 맞는지 확인

## K 폴드 교차 검증

- 가장 보편적인 교차 검증 기법
- K개의 데이터 폴드 세트를 만들어서 K번 만큼 각 폴트 세트에 학습과 검증 평가를 반복적으로 수행
- 각 검증마다 Test Fold를 다르게 지정하여 성능을 측정
    
    ![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%2014.png)
    
    - K 폴드 교차 검증 과정 자세히
        1. 전체 Dataset이 Train Dataset과 Test Dataset으로 주어집니다.
        2. Train Dataset을 나눌 *k*를 지정하고, 가급적 균등하게 그리고 랜덤으로 *k*개의 데이터 Fold로 나누되 (*k* - 1)개의 Fold는 Test용으로 1개는 Validation용으로 지정합니다.
        3. 튜닝하고자 하는 Hyperparameters를 정합니다.
        4. 정해진 Hyperparameters에 대하여 각각 검증하고자 하는 범위와 실험세트(요인 수준)를 정합니다.
        5. *k*개로 나누어진 Train Dataset 데이터 그룹에 대하여 서로 다른 Validation Fold를 지정하면서 아래의 오퍼레이션을 *k*번 반복합니다.
        · (*k* - 1)개의 Train Fold에 대하여 학습을 시킵니다.
        · 나머지 1개의 Validation Fold에 대하여 성능을 측정합니다. 즉, 앞서 학습된 파라미터를 이용하여 Validation Fold를 이용하여 결과를 얻습니다.
        6. 5번에서 얻은 각 Hyperparamer의 *k*개의 결과에 대한 평균을 계산하여 이 평균값을 각 Hyperaparameter로 지정합니다.
        7. 마지막으로, 6번에서 얻은 Hyperparameters를 적용하여 Test Data에 대하여 모델을 1회 평가합니다.

## **Stratified K 폴드**

- 데이터 레이블의 분포가 불균형할 경우, 원본 데이터와 유사한 레이블 값의 분포를 학습/테스트 세트에도 유지할 필요가 있다.
- 이렇게 분포를 유지하게 만드는 것을 stratify로 수행할 수 있으며, 특히 데이터의 개수가 적을 시에 이 과정이 필요하다.
- K 폴드가 레이블 데이터 집합이 원본 데이터 집합의 레이블 분포를 학습 및 테스트 세트에 제대로 분배하지 못하는 경우의 문제를 해결해 준다.
- Stratified K 폴드는 원본 데이터의 레이블 분포를 먼저 고려한 뒤 이 분포와 동일하게 학습과 검증 데이터 세트를 분배한다.

## GridSearchCV

- 머신러닝에서 모델의 성능향상을 위해 쓰이는 기법
- 사용자가 직접 모델의 하이퍼 파라미터의 값을 리스트로 입력하면 값에 대한 경우의 수마다 예측 성능을 측정 평가하여 비교하면서 최적의 하이퍼 파라미터 값을 찾는 과정
- 예시
    
    ```python
    parameters = {'max_depth':[1, 2, 3], 'min_samples_split':[2,3]}
    ```
    
    ![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%2015.png)
    
    ⇒ 파라미터의 집합을 만들고 이를 순차적으로 적용하면서 최적화를 수행
    
- 주요 파라미터
    - 하이퍼파라미터란 : 사용자의 입력값, 즉 우리가 설정 가능한 입력값
    - estimator : 예측기 객체 (Classifier, Regressor, Pipeline 등)
    - param_grid : 사용할 파라미터가 정의된 dictionary
    - scoring : 예측 성능을 측정할 평가 방법을 지정
    - cv : 교차검증 개수 (KFold 객체를 넣을 수도 있다.)
    - refit : 디폴트가 True이며 True로 생성 시 가장 최적의 하이퍼 파라미터를 찾은 뒤 입력된 esitmator 객체를 해당 하이퍼 파라미터로 재학습

## ****cross_val_score( )****

- 교차 검증을 좀 더 편리하게 수행할 수 있게 해주는 API
- KFold로 데이터를 학습하고 예측
- K 폴드의 예측 프로세스를 한번에 수행
- 선언 형태
    
    ```python
    cross_val_score(estimator, X, y=None, scoring=None, cv=None, 
    			n_jobs=1, verbose=0, fit_params=None, pre_dispatch='2*n_jobs')
    ```
    
    - **esmitator** :  사이킷런의 분류 알고리즘 클래스인 Classifier 또는 회귀 알고리즘 클래스인 Regressor를 의미
    - **X** : 피처 데이터 세트
    - **y** : 레이블 데이터 세트
    - **scoring** : 예측 성능 평가 지표를 기술
    - **cv** : 교차 검증 폴드 수
- cross_val_score( ) 수행 후 반환 값은 scoring 파라미터로 지정된 성능 지표 측정값을 배열 형태로 반환
- classifier가 입력되면 Stratified K 폴드 방식으로 레이블값의 분포에 따라 학습/테스트 세트를 분할
- 회귀인 경우에는 Stratified K 폴드 방식으로 분할할 수 없으므로 K 폴드 방식으로 분할

# iris 데이터 교차 검증 실습

## K 폴드

- K 폴드 교차 검증 프로세스를 구현하기 위해 KFold와 StratifiedKFold 클래스를 제공
- KFold 클래스를 이용해 붓꽃 데이터 세트를 교차 검증하고 예측 정확도를 알아본다.

### 데이터 로드

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold
import numpy as np

iris = load_iris()
features = iris.data
label = iris.target
dt_clf = DecisionTreeClassifier(random_state=156)
```

### k개의 폴드 세트로 분리하는 KFold 객체 생성

```python
kfold = KFold(n_splits=5)
cv_accuracy = []
print('붓꽃 데이터세트 크기 :', features.shape[0])
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> 붓꽃 데이터세트 크기 : 150

</aside>

현재 붓꽃 데이터 세트의 크기가 150이다.

k=5니까 5분할해서 학습 데이터세트 크기는 120, 검증 데이터세트 크기는 30

### 전체 붓꽃 데이터를 5개의 폴드 데이터 세트로 분리

- 이제 생성된 KFold 객체의 split( )을 호출해 전체 붓꽃 데이터를 5개의 폴드 데이터 세트로 분리
- KFold 객체는 split( )을 호출하면 학습용/검증용 데이터로 분할할 수 있는 인덱스를 반환한다.

```python
n_iter = 0

# KFold객체의 split() 호출하면 폴드 별 학습용, 검증용 테스트의 로우 인덱스를 array로 반환

for train_index, test_index in kfold.split(features): # features = iris.data
    # kfold.split()으로 반환된 인덱스를 이용하여 학습용, 검증용 데이터 추출
    X_train, X_test = features[train_index], features[test_index]
    y_train, y_test = label[train_index], label[test_index]
    # 학습 및 예측
    dt_clf.fit(X_train, y_train)
    pred = dt_clf.predict(X_test)
    n_iter += 1
    # 반복 시 마다 정확도 측정
    accuracy = np.round(accuracy_score(y_test,pred),4)
    train_size=X_train.shape[0]
    test_size=X_test.shape[0]
    print('\n#{0} 교차 검증 정확도:{1}, 학습데이터 크기:{2},  검증데이터 크기:{3}'
         .format(n_iter, accuracy, train_size, test_size))
    print('#{0} 검증 세트 인덱스{1}'.format(n_iter,test_index))
    cv_accuracy.append(accuracy)
    
# 개별 iteration별 정확도를 합하여 평균 정확도 계산
print('\n## 평균 검증 정확도', np.mean(cv_accuracy))
# 평균값을 각 Hyperaparameter로 지정
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> #1 교차 검증 정확도:1.0, 학습데이터 크기:120,  검증데이터 크기:30
#1 검증 세트 인덱스[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]

#2 교차 검증 정확도:0.9667, 학습데이터 크기:120,  검증데이터 크기:30
#2 검증 세트 인덱스[30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53
 54 55 56 57 58 59]

#3 교차 검증 정확도:0.8667, 학습데이터 크기:120,  검증데이터 크기:30
#3 검증 세트 인덱스[60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83
 84 85 86 87 88 89]

#4 교차 검증 정확도:0.9333, 학습데이터 크기:120,  검증데이터 크기:30
#4 검증 세트 인덱스[ 90  91  92  93  94  95  96  97  98  99 100 101 102 103 104 105 106 107
 108 109 110 111 112 113 114 115 116 117 118 119]

#5 교차 검증 정확도:0.7333, 학습데이터 크기:120,  검증데이터 크기:30
#5 검증 세트 인덱스[120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137
 138 139 140 141 142 143 144 145 146 147 148 149]

## 평균 검증 정확도 0.9

</aside>

## ****Stratified K 폴드****

### 데이터 로드

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold
import numpy as np
import pandas as pd

iris = load_iris()

iris_df = pd.DataFrame(data = iris.data, columns=iris.feature_names)
iris_df['label'] = iris.target
iris_df['label'].value_counts()
print(iris_df)
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> 0    50
1    50
2    50
Name: label, dtype: int64

```
     sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)  label
0                  5.1               3.5                1.4               0.2      0
1                  4.9               3.0                1.4               0.2      0
2                  4.7               3.2                1.3               0.2      0
3                  4.6               3.1                1.5               0.2      0
4                  5.0               3.6                1.4               0.2      0
..                 ...               ...                ...               ...    ...
145                6.7               3.0                5.2               2.3      2
146                6.3               2.5                5.0               1.9      2
147                6.5               3.0                5.2               2.0      2
148                6.2               3.4                5.4               2.3      2
149                5.9               3.0                5.1               1.8      2

[150 rows x 5 columns]
```

</aside>

### ****Stratified K 폴드 객체 생성 & 3개의 데이터 폴드 세트 생성****

- 이슈가 발생하는 현상을 도출하기 위해 3개의 폴드 세트를 KFold로 생성하고, 각 교차 검증 시마다 생성되는 학습/검증 레이블 데이터 값의 분포도를 확인해본다.

```python
kfold = KFold(n_splits=3)

# kfol.split(X)는 폴드 세트를 3번 반복할 때마다 달라지는 학습/테스트용 데이터 로우 인덱스 번호 반환.

n_iter = 0
for train_index, test_index in kfold.split(iris_df):
    n_iter += 1
    label_train = iris_df['label'].iloc[train_index]
    label_test = iris_df['label'].iloc[test_index]
    print('## 교차 검증: {0}'.format(n_iter))
    print('학습 레이블 데이터 분포:\n', label_train.value_counts())
    print('검증 레이블 데이터 분포:\n', label_test.value_counts())
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> ## 교차 검증: 1
학습 레이블 데이터 분포:
 1    50
2    50
Name: label, dtype: int64
검증 레이블 데이터 분포:
 0    50
Name: label, dtype: int64

## 교차 검증: 2
학습 레이블 데이터 분포:
 0    50
2    50
Name: label, dtype: int64
검증 레이블 데이터 분포:
 1    50
Name: label, dtype: int64

## 교차 검증: 3
학습 레이블 데이터 분포:
 0    50
1    50
Name: label, dtype: int64
검증 레이블 데이터 분포:
 2    50
Name: label, dtype: int64

</aside>

- 교차 검증 시마다 3개의 폴드 세트로 만들어지는 학습 레이블과 검증 레이블이 완전히 다른 값으로 추출되었다.
- 예를 들어 첫 번째 교차 검증에서 학습 레이블은 1, 2밖에 없으므로 0의 경우는 전혀 학습하지 못한다. 반대로 검증 레이블은 0밖에 없으므로 학습 모델은 절대 0을 예측하지 못한다.
- 이런 유형으로 교차 검증 데이터 세트를 분할하면 검증 예측 정확도는 0이 될 수 밖에 없다.

<aside>
💡 StratifiedKFold는 이렇게 KFold로 분할된 레이블 데이터 세트가 전체 레이블 값의 분포도를 반영하지 못하는 문제를 해결해준다.

StratifiedKFold를 사용하는 방법은 KFold를 사용하는 방법과 거의 비슷하다. 

단 하나 큰 차이는 StratifiedKFold는 레이블 분포도에 따라 학습/검증 데이터를 나누기 때문에 split( )메서드에 인자로 피처 데이터 세트뿐만 아니라 레이블 데이터 세트도 반드시 필요하다.

</aside>

### KFold의 문제 해결

```python
from sklearn.model_selection import StratifiedKFold

skf = StratifiedKFold(n_splits=3)
n_iter = 0

for train_index, test_index in skf.split(iris_df, iris_df['label']):
    n_iter += 1
    label_train = iris_df['label'].iloc[train_index]
    label_test = iris_df['label'].iloc[test_index]
    print('## 교차 검증: {0}'.format(n_iter))
    print('학습 레이블 데이터 분포:\n', label_train.value_counts())
    print('검증 레이블 데이터 분호:\n', label_test.value_counts())
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> ## 교차 검증: 1
학습 레이블 데이터 분포:
 2    34
0    33
1    33
Name: label, dtype: int64
검증 레이블 데이터 분호:
 0    17
1    17
2    16
Name: label, dtype: int64

## 교차 검증: 2
학습 레이블 데이터 분포:
 1    34
0    33
2    33
Name: label, dtype: int64
검증 레이블 데이터 분호:
 0    17
2    17
1    16
Name: label, dtype: int64

## 교차 검증: 3
학습 레이블 데이터 분포:
 0    34
1    33
2    33
Name: label, dtype: int64
검증 레이블 데이터 분호:
 1    17
2    17
0    16
Name: label, dtype: int64

</aside>

- 학습 레이블과 검증 레이블 데이터 값의 분포도가 동일하게 할당됐음
- 

### **train, test 데이터셋 분리 & 예측 정확도 평가**

```python
df_clf = DecisionTreeClassifier(random_state=156)

skfold = StratifiedKFold(n_splits=3)
n_iter = 0
cv_accuracy = []

# StratifiedKFold의 split() 호출시 반드시 레이블 데이터셋도 추가 입력 필요
for train_index, test_index in skfold.split(features, label):
    # split()으로 반환된 인덱스를 이용하여 학습용, 검증용 테스트 데이터 추출
    X_train, X_test = features[train_index], features[test_index]
    y_train, y_test = label[train_index], label[test_index]
    # 학습 및 예측
    dt_clf.fit(X_train, y_train)
    pred = dt_clf.predict(X_test)
    
    #반복시 마다 정확도 측정
    n_iter += 1
    accuracy = np.round(accuracy_score(y_test, pred), 4)
    train_size = X_train.shape[0]
    test_size = X_test.shape[0]
    print('\n{0} 교차 검증 정확도 :{1}, 학습 데이터 크기: {2}, 검증 데이터 크기: {3}'
         .format(n_iter, accuracy, train_size, test_size))
    print('#{0} 검증 세트 인덱스:{1}'.format(n_iter, test_index))
    cv_accuracy.append(accuracy)
    
# 교차 검증별 정확도 및 평균 정확도 계산
print('\n## 교차 검증별 정확도:', np.round(cv_accuracy,4))
print('## 평균 검증 정확도:', np.mean(cv_accuracy))
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> 1 교차 검증 정확도 :0.98, 학습 데이터 크기: 100, 검증 데이터 크기: 50
#1 검증 세트 인덱스:[  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  50
  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66 100 101
 102 103 104 105 106 107 108 109 110 111 112 113 114 115]

2 교차 검증 정확도 :0.94, 학습 데이터 크기: 100, 검증 데이터 크기: 50
#2 검증 세트 인덱스:[ 17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  67
  68  69  70  71  72  73  74  75  76  77  78  79  80  81  82 116 117 118
 119 120 121 122 123 124 125 126 127 128 129 130 131 132]

3 교차 검증 정확도 :0.98, 학습 데이터 크기: 100, 검증 데이터 크기: 50
#3 검증 세트 인덱스:[ 34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  83  84
  85  86  87  88  89  90  91  92  93  94  95  96  97  98  99 133 134 135
 136 137 138 139 140 141 142 143 144 145 146 147 148 149]

## 교차 검증별 정확도: [0.98 0.94 0.98]
## 평균 검증 정확도: 0.9666666666666667

</aside>

- 3개의 Stratified K 폴드로 교차 검증한 결과 평균 검증 정확도가 약 96.04%로 측정되었다.
- Stratified K 폴드의 경우 원본 데이터의 레이블 분포도 특성을 반영한 학습 및 검증 데이터 세트를 만들 수 있으므로 왜곡된 레이블 데이터 세트에서는 반드시 Stratified K 폴드를 이용해 교차 검증해야 한다.
- **사실, 일반적으로 분류(Classification)에서의 교차 검증은 K 폴드가 아니라 Stratified K 폴드로 분할돼야 한다.**

## ****cross_val_score( )****

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score, cross_validate
from sklearn.datasets import load_iris

iris_data = load_iris()
dt_clf = DecisionTreeClassifier(random_state=156)

data = iris_data.data
label = iris_data.target

# 성능 지표는 정확도(accuracy), 교차 검증 세트는 3개
scores = cross_val_score(dt_clf, data, label, scoring='accuracy', cv=3)
print('교차 검증별 정확도:', np.round(scores,4))
print('평균 검증 정확도:', np.round(np.mean(scores),4))
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> 교차 검증별 정확도: [0.98 0.94 0.98]
평균 검증 정확도: 0.9667

</aside>

- cv로 지정된 횟수만큼 scoring 파라미터로 지정된 평가 지표로 평가 결괏값을 배열로 반환 ⇒ 일반적으로 이를 평균해 평가 수치로 사용
- 내부에서 Estimator를 학습(fit), 예측(predict), 평가(evaluation)시켜주므로 간단하게 교차 검증을 수행할 수 있다.

## GridSearchCV

### 데이터 로드 & 학습 및 테스트 데이터 분리

```python
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

# 데이터를 로딩하고 학습데이터와 테스트 데이터 분리
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris_data.data, iris_data.target, test_size=0.2, random_state=121)
dtree = DecisionTreeClassifier()

### parameter 들을 dictionary 형태로 설정
parameters = {'max_depth':[1,2,3], 'min_samples_split':[2,3]}
# max_depth는 결정 트리의 최대 깊이를 제한하는 파라미터 => 작은 값으로 설정하면 모델이 단순화되어 과적합을 줄일 수 있고, 큰 값으로 설정하면 복잡한 모델이 만들어질 수 있음.
# min_samples_split은 노드를 분할하기 위해 필요한 최소 샘플 수를 제한

```

- 테스트할 하이퍼 파라미터 세트는 딕셔너리 형태로
- 하이퍼 파라미터의 명칭은 문자열 Key 값으로
- 하이퍼 파라미터의 값은 리스트 형으로 설정

### 테스트 수행 설정 & 학습

- 학습 데이터 세트를 GridSearchCV 객체의 fit(학습 데이터 세트) 메서드에 인자로 입력한다.
- 학습 데이터를 cv에 기술된 폴딩 세트로 분할해 param_grid에 기술된 하이퍼 파라미터를 순차적으로 변경하면서 학습/평가를 수행하고 그 결과를 cv_result 속성에 기록한다.
- cv_result 는 gridsearchcv의 결과 세트로서 딕셔너리 형태로 key값과 리스트 형태의 value값을 가진다.

```python
import pandas as pd

# param_grid의 하이퍼 파라미터들을 3개의 train, test set fold로 나누어서 테스트 수행 설정.

grid_dtree = GridSearchCV(dtree, param_grid=parameters, cv=3, refit=True)

# iris train 데이터로 param_gird의 하이퍼 파라미터들을 순차적으로 학습/평가
grid_dtree.fit(X_train, y_train)

# GridSearchCV 결과를 추출하여 DataFrame으로 변환
scores_df = pd.DataFrame(grid_dtree.cv_results_)
scores_df[['params', 'mean_test_score', 'rank_test_score', \
         'split0_test_score', 'split1_test_score', 'split2_test_score']]
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" />

![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%2016.png)

</aside>

- 총 6개의 결과 ⇒ 하이퍼 파라미터 max_depth와 min_samples_split을 순차적으로 총 6번 변경하면서 학습 및 평가를 수행했음을 나타낸다.
- 맨 마지막에서 두 번째 행을 보면 평가한 결과 예측 성능이 1위라는 의미
- split0_test_score, split1_test_score, split2_test_score는 CV가 3인 경우, 즉 3개의 폴딩 세트에서 각각 테스트한 성능 수치
- mean_test_score는 이 세 개 성능 수치를 평균화한 것

<aside>
💡

- params 칼럼에는 수행할 때마다 적용된 개별 하이퍼 파라미터 값을 나타낸다.
- rank_test_score는 하이퍼 파라미터별로 성능이 좋은 score 순위를 나타낸다.
- mean_test_score는 개별 하이퍼 파라미터별로 CV의 폴딩 테스트 세트에 대해 총 수행한 평가 평균값이다.
</aside>

### 최적 파라미터 & 최고 정확도 도출

- GridSearchCV 객체의 fit( )을 수행하면 최고 성능을 나타낸 하이퍼 파라미터 값과 그때의 평가 결과 값이 각각 best_params, best_score_속성에 기록된다.

```python
print('GridSearchCV 최적 파라미터:', grid_dtree.best_params_)
print('GridSearchCV 최고 정확도:{0:4f}'.format(grid_dtree.best_score_))
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> GridSearchCV 최적 파라미터: {'max_depth': 3, 'min_samples_split': 2}
GridSearchCV 최고 정확도:0.975000

</aside>

```python
# refit=True로 설정된 GridSearchCV 객체가 fit()를 수행시 학습이 완료된 Estimator를 내포하고 있으므로 predict()을 통해 예측도 가능

pred = grid_dtree.predict(X_test)
print('테스트 데이터 세트 정확도: {0:.4f}'.format(accuracy_score(y_test,pred)))
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> 테스트 데이터 세트 정확도: 0.9667

</aside>

<aside>
💡 일반적으로 학습 데이터를 GridSearchCV를 이용해 최적 하이퍼 파라미터 튜닝을 수행한 뒤에 별도의 테스트 세트에서 이를 평가하는 것이 일반적인 머신러닝 모델 적용 방법이다.

</aside>

# 데이터 전처리(Preprocessing)

## 개요

### 데이터 전처리가 필요한 이유

- 결측치 값이 허용되지 않는다.
    - Null 값이 얼마 없으면 중앙값이나 평균값으로 대체한다.
    - Null 값이 대다수라면 해당 피쳐값은 드롭하는 것도 좋다.
    - 중요도가 높은 피처는 유지시킨다.
- 문자열도 허용되지 않는다.
    - 문자열이 허용되지 않기 때문에 해당 피처값에 대한 인코딩(숫자로 변환)이 필요하다.
    - 인코딩은 카테고리형(코드 값)으로 대부분 변환시킨다.
    - 필요없는 피처는 드롭시킨다.

### 데이터 전처리 종류

- 데이터 클린징
- 결손값 처리(Null,NaN 처리)
- 데이터 인코딩(레이블, 원-핫 인코딩)
- 데이터 스케일링
- 이상치 제거
- Feature 선택, 추출 및 가공

## 데이터 인코딩

- 대표적인 데이터 인코딩 방식 : Label encoding, One Hot Encoding
- 숫자의 크고 작음이 있기 때문에 Tree 계열 AL을 제외하면 가중치가 적용되어 문제가 될 수 있음.
- Label Encoding의 문제점을 해결한 것이 One Hot Encoding

### 레이블 인코딩(Label Encoding)

- 문자열로 구성되어 있는 items 데이터를 카테코리화(코드화) 하는 것
- sklearn의 label encoding은 LabelEncoder Class로 구현함.
- Label Encoder를 객체로 생성한 후 fit(), transform()을 호출해 레이블 인코딩을 수행

<aside>
💡 fit(), transform()을 사용하는 목적?

- fit()은 데이터 변환을 위한 기준 정보를 설정 (data set의 max/min 값 설정 등)을 적용해 줌.
- transform()은 설정된 정보를 이용해 데이터를 변환함.

</aside>

```python
from sklearn.preprocessing import LabelEncoder

items=['TV', '냉장고', '전자렌지', '컴퓨터', '선풍기', '선풍기', '믹서', '믹서']

# LabelEncoder를 객체로 생성한 후, fit()과 transfor()으로 label 인코딩 수행.
encoder=LabelEncoder()
encoder.fit(items)
labels=encoder.transform(items)
print('인코딩 변환값:', labels)
print(type(labels))
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> 인코딩 변환값: [0 1 4 5 3 3 2 2]
<class 'numpy.ndarray'>

</aside>

```python
print('인코딩 클래스:', encoder.classes_)
print('디코딩 원본 값:', encoder.inverse_transform([4,5,2,0,1,1,3,3]))
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> 인코딩 클래스: ['TV' '냉장고' '믹서' '선풍기' '전자렌지' '컴퓨터']

디코딩 원본 값: ['전자렌지' '컴퓨터' '믹서' 'TV' '냉장고' '냉장고' '선풍기' '선풍기']

</aside>

- .class_ 속성은 0번부터 순서대로 변환된 인코딩 값에 대한 원본을 가지고 있음
    
    ⇒ TV가 0, 냉장고가 1, 믹서가 2, 선풍기가 3, 전제렌지가 4, 컴퓨터가 5로 인코딩되었음.
    
- 거꾸로 인코딩 결과를 통해 원본 추적도 가능

### 원-핫 인코딩 (One-Hot Encoding)

- feature 값의 유형에 따라 새로운 feature를 추가해 고유 값에 해당하는 column만 1을 표시. 나머지 column에는 0을 표시하는 방식
- 즉 행 형태로 되어있는 feature의 고유 값을 열 형태로 차원을 변환함 → 고유값에 해당하는 column에만 1, 나머지 column에는 0을 표시
- 원-핫 인코딩은 sklearn에서 OneHotEncoder Class로 쉽게 변환 가능
- 주의할 점
    - OneHotEncoder로 변환하기 전에 모든 문자열 값이 숫자형 값으로 변환되어야 함. (LabelEncoder가 선행되어야 함.)
    - 입력 값으로 2차원의 데이터가 필요함.

```python
from sklearn.preprocessing import OneHotEncoder
import numpy as np

items = ['TV', '냉장고', '전자렌지', '컴퓨터', '선풍기', '선풍기', '믹서', '믹서']

#먼저 숫자 값으로 변환하기 위해 LabelEncoder로 변환
encoder = LabelEncoder()
encoder.fit(items)
labels = encoder.transform(items)

# 2차원 데이터로 변환
# 머신러닝 모델에 데이터를 입력으로 사용할 때, 일반적으로 2차원 형태로 주어짐.
# 첫 번째 차원은 샘플의 개수를 나타내는 차원이고,
# 두 번째 차원은 각 샘플의 특성(feature)을 나타내는 차원
labels = labels.reshape(-1,1)
# print(labels)
# -1을 사용하면 해당 차원의 크기를 자동으로 계산
# 1은 두 번째 차원의 크기를 1로 지정하라는 의미

# 원-핫 인코딩 적용
oh_encoder = OneHotEncoder()
oh_encoder.fit(labels)
oh_labels = oh_encoder.transform(labels)
print('원-핫 인코딩 데이터')
print(oh_labels.toarray()) # 일반적인 2차원 배열로 변환하는 메서드-> 2차원 배열로 변환하여 보여줌
print('원-핫 인코딩 데이터 차원')
print(oh_labels.shape)
# items 리스트에서 유일한 값의 개수가 6개이므로, 
# 원-핫 인코딩은 6개의 이진 자리를 만들어 각 항목에 대해 해당하는 자리를 1로 표시하고 나머지 자리를 0으로 표시
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> 원-핫 인코딩 데이터
[[1. 0. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0. 0.]
 [0. 0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 0. 1.]
 [0. 0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0. 0.]
 [0. 0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0. 0.]]

원-핫 인코딩 데이터 차원
(8, 6)

</aside>

- 좀 더 쉬운 원-핫 인코딩 방법(get_dummies)
    
    Label Encoding 과정(문자열 카테고리 값을 숫자형으로 변환) 거칠 필요 없이 바로 사용 가능
    

```python
import pandas as pd

df = pd.DataFrame({'itmes':['TV', '냉장고', '전자렌지', '컴퓨터', '선풍기', '선풍기', '믹서', '믹서']})
pd.get_dummies(df)
```

![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%2017.png)

## 피처 스케일(feature scaling)

### 피처 스케일링이란?

- 서로 다른 변수의 값 범위를 일정한 수준으로 맞추는 작업
- 대표적인 방법 : 표준화(Standardization), 정규화(Nomalization)

### 표준화(Standardization)

- data의 feature 각각을 평균=0, 분산=1인 가우시안 정규분포를 가진 값으로 변환하는 것
- 𝑿_𝑺𝒕𝒂𝒏𝒅𝒂𝒓𝒅𝒊𝒛𝒂𝒕𝒊𝒐𝒏 = 𝑿 − 𝒎𝒆𝒂𝒏(𝑿) / 𝒔𝒕𝒅 (𝑿)

### 정규화(Nomalization)

- 서로 다른 feature의 크기를 통일하기 위해 크기를 변환함. 변수를 모두 동일한 크기 단위로 비교하기 위해 값을 모두 최소 0~ 최대 1의 값으로 변환.
- 즉 개별 데이터의 크기를 모두 똑같은 단위로 변경함.
- 𝑿_𝑵𝒐𝒓𝒎𝒂𝒍𝒊𝒛𝒂𝒕𝒊𝒐𝒏 = 𝑿 − 𝒎𝒊𝒏(𝑿) / 𝒎𝒂𝒙 𝑿 − 𝒎𝒊𝒏(𝑿)

### StandardScaler(표준화 Class)

- 표준화를 쉽게 지원하기 위한 Class
- 개별 feature의 평균이 0, 분산이 1인 값으로 변환해줌.
- data가 가우시안 정규 분포를 가지도록 변환하는 것의 중요성
    - 선형 회귀
    - 로지스틱 회귀
    - 서포트 백터 머신
    - 위 세개 모델의 경우 데이터가 가우시안 분포를 가진다고 가정하고 구현됐기 때문에 사전에 데이터 변환 작업이 예측 성능 향상에 중요한 요소가 될 수 있음.

```python
from sklearn.datasets import load_iris
import pandas as pd

# 붓꽃 데이터셋을 로딩하고 Datarame으로 변환
iris = load_iris()
iris_data = iris.data
iris_df = pd.DataFrame(data=iris_data, columns=iris.feature_names)

print('feature들의 평균 값')
print(iris_df.mean())
print('\nfeature들의 분산 값')
print(iris_df.var())
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> feature들의 평균 값
sepal length (cm)    5.843333
sepal width (cm)     3.057333
petal length (cm)    3.758000
petal width (cm)     1.199333
dtype: float64

feature들의 분산 값
sepal length (cm)    0.685694
sepal width (cm)     0.189979
petal length (cm)    3.116278
petal width (cm)     0.581006
dtype: float64

</aside>

```python
from sklearn.preprocessing import StandardScaler

# StandardScaler 객체 생성
scaler = StandardScaler()
# StandardScaler로 데이터셋 변환. fit() 과 transform() 호출
scaler.fit(iris_df)
iris_scaled = scaler.transform(iris_df)

#transform()시 scale 변환된 데이터셋이 numpy ndarry로 반환되어 이를 DataFrame으로 변환
iris_df_scaled = pd.DataFrame(data=iris_scaled, columns=iris.feature_names)
print('feature들의 평균값')
print(iris_df_scaled.mean())
print('\nfeature들의 분산값')
print(iris_df_scaled.var())
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> feature들의 평균값
sepal length (cm)   -1.690315e-15
sepal width (cm)    -1.842970e-15
petal length (cm)   -1.698641e-15
petal width (cm)    -1.409243e-15
dtype: float64

feature들의 분산값
sepal length (cm)    1.006711
sepal width (cm)     1.006711
petal length (cm)    1.006711
petal width (cm)     1.006711
dtype: float64

</aside>

<aside>
💡 평균은 0, 분산은 1에 매우 가깝게 맞춰진 것을 확인할 수 있다.

</aside>

### MinMaxScaler(정규화 Class)

- 표준화를 쉽게 지원하기 위한 Class
- 개별 feature의 평균이 0, 분산이 1인 값으로 변환해줌.
- data가 가우시안 정규 분포를 가지도록 변환하는 것의 중요성
    - 서포트 벡터 머신
    - 선형 회귀
    - 로지스틱 회귀
    - 위 3개의 모델의 경우 데이터가 가우시안 분포를 가진다고 가정하고 구현됐기 때문에 사전에 데이터 변환 작업이 예측 성능 향상에 중요한 요소가 될 수 있음.

```python
from sklearn.preprocessing import MinMaxScaler

# MinMaxScaler 객체 생성
scaler = MinMaxScaler()

# MinMaxScaler로 데이터셋 변환. fit()과 transform() 호출
scaler.fit(iris_df)
iris_scaled = scaler.transform(iris_df)

# transform()시 scale 변환된 데이터셋이 numpy ndarray로 반환되어 이를 DF로 변환
iris_df_scaled = pd.DataFrame(data=iris_scaled, columns=iris.feature_names)
print('feature들의 최소값')
print(iris_df_scaled.min())
print('\nfeature들의 최대값')
print(iris_df_scaled.max())
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> feature들의 최소값
sepal length (cm)    0.0
sepal width (cm)     0.0
petal length (cm)    0.0
petal width (cm)     0.0
dtype: float64

feature들의 최대값
sepal length (cm)    1.0
sepal width (cm)     1.0
petal length (cm)    1.0
petal width (cm)     1.0
dtype: float64feature들의 최소값

</aside>

<aside>
💡 feature들의 값이 최소 0 ~ 최대 1로 변환되었다.

</aside>

### Scaler를 이용한 fit(), fit_transform 적용 시 유의사항

- fit / transform을 사용하는 목적은?
    - fit()은 데이터 변환을 위한 기준 정보 설정
    - transform()은 설정된 정보를 이용해 데이터를 변환
    - fit_transform()은 fit()+transform()을 한번에 적용하는 기능을 수행

❗training data set, test data set에 fit, transform 적용 시 주의 사항 ❗

- Scaler 객체를 이용해 training data set으로 fit, transform을 적용하면 test data set으로는 다시 fit을 수행하지 않고, 그냥 앞서 trianing data set으로 fit()을 수행한 결과를 이용해 transform() 변환을 적용해야 한다.
- 즉 training data로 fit() 적용된 스케일링 정보를 test data에 그대로 적용해야 함.

<aside>
💡 따라서  trainig data와 test data에 각각 fit()을 적용하면 안되고, 
테스트 데이터에서는 학습 데이터 세트로 `fit()`을 수행한 결과를 이용해 `transform()`을 해야 한다.

`fit_transform()`은 자동으로 `fit()` 과정을 포함시키게 되므로 테스트 데이터에 사용하면 안된다.

</aside>

# 타이타닉 생존자 예측 실습

## 데이터 로드