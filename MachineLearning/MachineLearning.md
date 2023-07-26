# Machine Learning

📖[https://github.com/wikibook/pymlrev2/tree/main](https://github.com/wikibook/pymlrev2/tree/main)

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
    - 자료의 분류를 베이즈 정리를 활용하여 판단
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
    

---

---

# 분류

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
- **사실, 일반적으로 분류(Classification)에서의 교차 검증은 K 폴드가 아니라 Stratified K 폴드로 분할해야 한다.**

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

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

## 데이터 불러오기
titanic_df = pd.read_csv('./titanic_train.csv')
titanic_df.info()
titanic_df.isnull().sum() # NaN값 확인
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> <class 'pandas.core.frame.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  891 non-null    int64  
 1   Survived     891 non-null    int64  
 2   Pclass       891 non-null    int64  
 3   Name         891 non-null    object 
 4   Sex          891 non-null    object 
 5   Age          714 non-null    float64
 6   SibSp        891 non-null    int64  
 7   Parch        891 non-null    int64  
 8   Ticket       891 non-null    object 
 9   Fare         891 non-null    float64
 10  Cabin        204 non-null    object 
 11  Embarked     889 non-null    object 
dtypes: float64(2), int64(5), object(5)
memory usage: 83.7+ KB

PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64

</aside>

- Age, Cabin, Embarked에 결측치가 있는 것을 확인할 수 있다.

## ****데이터 확인 & Null 값 처리****

### Null 값 처리

```python
titanic_df['Age'].fillna(titanic_df['Age'].mean(), inplace=True)
titanic_df['Cabin'].fillna('N', inplace = True)
titanic_df['Embarked'].fillna('N', inplace = True)
print('데이터 세트 Null 값 갯수 ',titanic_df.isnull().sum().sum())
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> 데이터 세트 Null 값 갯수  0

</aside>

```python
print(' Sex 값 분포 :\n',titanic_df['Sex'].value_counts())
print('\n Cabin 값 분포 :\n',titanic_df['Cabin'].value_counts())
print('\n Embarked 값 분포 :\n',titanic_df['Embarked'].value_counts())
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" />  Sex 값 분포 :
 male      577
female    314
Name: Sex, dtype: int64

 Cabin 값 분포 :
 N              687
C23 C25 C27      4
G6               4
B96 B98          4
C22 C26          3
              ...
E34              1
C7               1
C54              1
E36              1
C148             1
Name: Cabin, Length: 148, dtype: int64

 Embarked 값 분포 :
 S    644
C    168
Q     77
N      2
Name: Embarked, dtype: int64

</aside>

### Cabin 컬럼 데이터 제일 앞 등급 표시만 가져오도록

```python
titanic_df['Cabin'] = titanic_df['Cabin'].str[:1]
print(titanic_df['Cabin'].head(3))
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> 0    N
1    C
2    N
Name: Cabin, dtype: object

</aside>

### 데이터 확인

- 생존자의 남녀 성비 구성 확인
    
    ```python
    titanic_df.groupby(['Sex','Survived'])['Survived'].count()
    ```
    
    <aside>
    <img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> Sex     Survived
    female  0            81
                 1           233
    male     0           468
                 1           109
    Name: Survived, dtype: int64
    
    </aside>
    
    - 확인 결과 : 남성보다 여성이 더 생존능력이 뛰어나다 라고 분석을 하는건 너무 성급한 일반화의 오류
    
    ```python
    sns.barplot(x='Sex', y = 'Survived', data=titanic_df)
    ```
    
    <aside>
    <img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" />
    
    ![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%2018.png)
    
    </aside>
    
- 성별과 객실 등급에 따른 생존 여부 비교
    
    ```python
    sns.barplot(x='Pclass', y='Survived', hue='Sex', data=titanic_df)
    ```
    
    <aside>
    <img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" />
    
    ![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%2019.png)
    
    </aside>
    
    <aside>
    💡 생존자수가 1이 넘지 않는 이유 'sns.barplot()' 함수는 기본적으로 막대 그래프를 그릴 때 각 범주의 평균 값을 계산하여 표시. 
    
    생존 여부(Survived) 열은 0과 1의 두 가지 값으로 구성되어 있으며, 이 값들은 사망(0)과 생존(1)을 나타냄.
    
    따라서 평균 생존율은 0과 1 사이의 값으로 표현됨.
    
    </aside>
    
    ```python
    sns.barplot(x="Sex", y="Survived", hue="Pclass", data=titanic_df)
    ```
    
    <aside>
    <img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" />
    
    ![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%2020.png)
    
    </aside>
    
- 나이별 생존 여부 비교
    
    ```python
    def get_categroy(age):
        cat = ""
        if age <= -1: cat = "Unknown"
        elif age <= 5: cat = "Baby"
        elif age <= 12: cat = "Child"
        elif age <= 18: cat = "Teenager"
        elif age <= 25: cat = "Student"
        elif age <= 35: cat = "Young Adult"
        elif age <= 60: cat = "Adult"
        else : cat = "Elderly"
        return cat
    
    #X축의 값을 순차적으로 표시하기 위한 설정
    group_names = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Elderly']
    
    # lambda 식에 위에서 생성한 get_category( ) 함수를 반환값으로 지정. 
    # get_category(X)는 입력값으로 'Age' 컬럼값을 받아서 해당하는 cat 반환
    titanic_df["AgeGroup"] = titanic_df["Age"].apply(lambda x : get_categroy(x))
    titanic_df["AgeGroup"].value_counts()
    ```
    
    <aside>
    <img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> Young Adult    373
    Adult          195
    Student        162
    Teenager        70
    Baby            44
    Child           25
    Elderly         22
    Name: AgeGroup, dtype: int64
    
    </aside>
    
    ```python
    # 나이대 그룹과 성별에 따른 생존 여부
    sns.barplot(x="AgeGroup", y="Survived", hue="Sex", data=titanic_df,  order=group_names)
    ```
    
    <aside>
    <img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" />
    
    ![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%2021.png)
    
    </aside>
    
- Parch(같이 탑승한 부모님 또는 어린이 인원수)와 SibSp(같이 탑승한 형제 또는 배우자 인원수)에 따른 생존 여부 비교
    
    ```python
    sns.barplot(x="Parch", y="Survived", data=titanic_df)
    ```
    
    <aside>
    <img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" />
    
    ![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%2022.png)
    
    </aside>
    
    <aside>
    💡 결과 : 다른 비교 그래프들에 비해 균등하므로 좋은 변수는 아님
    
    </aside>
    
    ```python
    sns.barplot(x="SibSp", y="Survived", data=titanic_df)
    ```
    
    <aside>
    <img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" />
    
    ![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%2023.png)
    
    </aside>
    
- 머신러닝 알고리즘에 불필요한 속성 제거
    
    ```python
    def drop_features(df):
        df.drop(['PassengerId','Name','Ticket'],axis=1,inplace=True)
        return df
    ```
    

## 인코딩

```python
# 레이블 인코딩 수행.
# 'Cabin','Sex','Embarked'의 데이터 값을 숫자로 변환

from sklearn import preprocessing

def format_features(df):
    features = ['Cabin','Sex','Embarked']
    for feature in features:
        le = preprocessing.LabelEncoder()
        le = le.fit(df[feature])
        df[feature] = le.transform(df[feature])
    return df

titanic_df = format_features(titanic_df)
titanic_df.head()
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" />

![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%2024.png)

</aside>

- 위에서 실행한 Null값 처리, 불필요한 속성 제거, 인코딩을 하나의 def로 생성
    
    ```python
    from sklearn.preprocessing import LabelEncoder
    
    # Null 처리 함수
    def fillna(df):
        df['Age'].fillna(df['Age'].mean(),inplace=True)
        df['Cabin'].fillna('N',inplace=True)
        df['Embarked'].fillna('N',inplace=True)
        df['Fare'].fillna(0,inplace=True)
        return df
    
    # 머신러닝 알고리즘에 불필요한 속성 제거
    def drop_features(df):
        df.drop(['PassengerId','Name','Ticket'],axis=1,inplace=True)
        return df
    
    # 앞에서 설정한 Data Preprocessing 함수 모두 호출
    def transform_features(df):
        df = fillna(df)
        df = drop_features(df)
        df = format_features(df)
        return df
    ```
    

## 원본 데이터를 재로딩 & feature 데이터셋과 Label 데이터셋 분리

- 원본 데이터 재로딩
    
    ```python
    import pandas as pd
    
    titanic_df = pd.read_csv('./titanic_train.csv')
    
    y_titanic_df = titanic_df['Survived']
    X_titanic_df= titanic_df.drop('Survived',axis=1)
    
    X_titanic_df = transform_features(X_titanic_df) # 데이터 전처리 & 인코딩
    
    X_titanic_df
    ```
    
    <aside>
    <img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" />
    
    ![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%2025.png)
    
    </aside>
    
- feature 데이터셋과 Label 데이터셋 분리
    
    ```python
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test=train_test_split(X_titanic_df, y_titanic_df, \
                                                      test_size=0.2, random_state=11)
    ```
    

## 생존자 예측 수행

- 결정트리, 랜덤 포레스트, 로지스틱 회귀를 이용
- 사이킷런 Classifier 객체 생성

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 결정트리, Random Forest, 로지스틱 회귀를 위한 사이킷런 Classifier 클래스 생성
dt_clf = DecisionTreeClassifier(random_state=11)
rf_clf = RandomForestClassifier(random_state=11)
lr_clf = LogisticRegression()
```

- 학습/예측평가

```python
# DecisionTreeClassfier 학습/예측평가
dt_clf.fit(X_train, y_train)
dt_pred = dt_clf.predict(X_test)
print('DecisionTreeClassifier 정확도 : {0:.4f}'.format(accuracy_score(y_test, dt_pred)))

# RandomForestClassifier 학습/예측/평가
rf_clf.fit(X_train, y_train)
rf_pred = rf_clf.predict(X_test)
print('RandomForestClassifier 정확도 : {0:.4f}'.format(accuracy_score(y_test, rf_pred)))

# LogisticRegression 학습/예측/평가
lr_clf.fit(X_train, y_train)
lr_pred = lr_clf.predict(X_test)
print('LogisticRegression 정확도 : {0:.4f}'.format(accuracy_score(y_test, lr_pred)))
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> DecisionTreeClassifier 정확도 : 0.7989
RandomForestClassifier 정확도 : 0.8436
LogisticRegression 정확도 : 0.8603

</aside>

- 결과 : 3개의 알고리즘 중 LogisticRegression이 타 알고리즘에 비해 높은 정확도를 나타내고 있음.
- 그러나 아직 최적화 작업을 수행하지 않았고, 데이터 양도 충분하지 않기에 LogistiocRegression이 가장 좋은 모델이라고 할 수는 없음.

## 교차 검증

- KFold

```python
from sklearn.model_selection import KFold

def exec_kfold(clf, folds = 5) :
    # 폴드 세트가 5개인 KFold 객체 생성. 폴드 수만큼 예측결과 저장 위한 리스트 생성
    kfold = KFold(n_splits = folds)
    scores = []
    
    # KFold 교차 검증 수행
    for iter_count, (train_index, test_index) in enumerate(kfold.split(X_titanic_df)) :
        # X_titanic_df 데이터에서 교차 검증별로 학습과 검증 데이터를 가리키는 index 생성
        X_train, X_test = X_titanic_df.values[train_index], X_titanic_df.values[test_index] # values를 통해 df를 ndarray로 변환
        y_train, y_test = y_titanic_df.values[train_index], y_titanic_df.values[test_index]
        
        # Classifier 학습/예측/평가
        clf.fit(X_train, y_train)
        clf_pred = clf.predict(X_test)
        accuracy = accuracy_score(y_test, clf_pred)
        scores.append(accuracy)
        print("교차 검증 {0} 정확도 : {1:.4f}".format(iter_count, accuracy))
        
    # 5개의 fold에서 평균 정확도 계산
    mean_score = np.mean(scores)
    print("평균 정확도: {0:.4f}".format(mean_score))

#exec_fold 호출
exec_kfold(dt_clf, folds = 5)
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> 교차 검증 0 정확도 : 0.7486
교차 검증 1 정확도 : 0.7640
교차 검증 2 정확도 : 0.8202
교차 검증 3 정확도 : 0.7809
교차 검증 4 정확도 : 0.7921
평균 정확도: 0.7812

</aside>

- cross_val_score()

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(dt_clf, X_titanic_df, y_titanic_df, cv = 5)
print("scores : ", scores)
for iter_count, accuracy in enumerate(scores) :
    print("교차 검증 {0} 정확도: {1:.4f}".format(iter_count, accuracy))
    
print("평균 정확도: {0:.4f}".format(np.mean(scores)))
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> scores :  [0.74860335 0.7752809  0.80898876 0.75842697 0.80337079]
교차 검증 0 정확도: 0.7486
교차 검증 1 정확도: 0.7753
교차 검증 2 정확도: 0.8090
교차 검증 3 정확도: 0.7584
교차 검증 4 정확도: 0.8034
평균 정확도: 0.7789

</aside>

- GridSearchCV

```python
from sklearn.model_selection import GridSearchCV

parameters = {'max_depth':[2, 3, 5, 10],
             'min_samples_split':[2, 3, 5],
             'min_samples_leaf':[1, 5, 8]}
grid_dclf = GridSearchCV(dt_clf, param_grid = parameters, scoring = 'accuracy', cv = 5)
grid_dclf.fit(X_train, y_train)

print('GridSearchCV 최적 하이퍼 파라미터 : ', grid_dclf.best_params_)
print('GridSearchCV 최고 정확도: {0:.4f}'.format(grid_dclf.best_score_))
best_dclf = grid_dclf.best_estimator_

#GridSearchCV의 최적 하이퍼 파라미터로 학습된 Estimator로 예측 및 평가 수행
dpredictions = best_dclf.predict(X_test)
accuracy = accuracy_score(y_test, dpredictions)
print('테스트 세트에서의 DecisionTreeClassifier 정확도 : {0:.4f}'.format(accuracy))
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> GridSearchCV 최적 하이퍼 파라미터 :  {'max_depth': 5, 'min_samples_leaf': 1, 'min_samples_split': 5}
GridSearchCV 최고 정확도: 0.7993
테스트 세트에서의 DecisionTreeClassifier 정확도 : 0.8659

</aside>

# 분류(Classification) 성능 평가 지표

## 정확도(Accuracy)

### 정확도란?

- 정확도는 직관적으로 모델 예측 성능을 나타내는 평가 지표
- 이진 분류의 경우 데이터의 구성에 따라 ML 모델의 성능을 왜곡할 수 있
기 때문에 정확도 수치 하나만 가지고 성능을 평가하지 않음.
- 특히 정확도는 불균형한(imbalanced) 레이블 값 분포에서 ML 모델의
선능을 판단할 경우, 적합한 평가 지표가 아님

![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%2026.png)

### 적용

```python
import numpy as np
from sklearn.base import BaseEstimator

class MyDummyClassfier(BaseEstimator):
    # fit() 메소드는 아무것도 학습하지 않음.
    def fit(self, X, y=None):
        pass
    
    #predict() 메소드는 단순히 sex feature가 1이면 0, 그렇지 않으면 1로 예측함.
    def predict(self, X):
        pred = np.zeros((X.shape[0],1))
        for i in range(X.shape[0]):
            if X['Sex'].iloc[i] == 1:
                pred[i] = 0
            else :
                pred[i] = 1
                
        return pred
```

```python
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Null 처리 함수
def fillna(df):
    df['Age'].fillna(df['Age'].mean(),inplace=True)
    df['Cabin'].fillna('N', inplace = True)
    df['Embarked'].fillna('N', inplace = True)
    df['Fare'].fillna(0, inplace = True)
    return df

# 머신러닝 알고리즘에 불필요한 속성 제거

def drop_features(df):
    df.drop(['PassengerId','Name','Ticket'],axis=1, inplace=True)
    return df

# 레이블 인코딩 수행
def format_features(df):
    df['Cabin'] = df['Cabin'].str[:1]
    features = ['Cabin','Sex','Embarked']
    for feature in features:
        le = LabelEncoder()
        le = le.fit(df[feature])
        df[feature] = le.transform(df[feature])
    return df

# 앞에서 설정한 Data Preprocessing 함수 호출
def transform_features(df):
    df = fillna(df)
    df = drop_features(df)
    df = format_features(df)
    return df
```

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 원본 데이터를 재로딩, 데이터 가공, 학습데이터/테스트데이터 분할
titanic_df = pd.read_csv('C:/JupyterTest/머신러닝/titanic_train.csv')
y_titanic_df = titanic_df['Survived']
X_titanic_df = titanic_df.drop('Survived',axis=1)
X_titanic_df = transform_features(X_titanic_df)
X_train, X_test, y_train, y_test = train_test_split(X_titanic_df, y_titanic_df,test_size=0.2, random_state=0)

# 위에서 생성한 Dummy Classfier를 이용하여 학습/예측/평가 수행
myclf = MyDummyClassfier()
myclf.fit(X_train, y_train)

mypredictions = myclf.predict(X_test)
print('Dummy Classfier의 정확도는: {0: .4f}'.format(accuracy_score(y_test, mypredictions)))

# 아무 알고리즘을 적용하지 않아도 정확도가 0.7877이 나옴.
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> Dummy Classfier의 정확도는:  0.7877

</aside>

```python
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.base import BaseEstimator
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd

class MyFakeClassfier(BaseEstimator):
    def fit(self,X,y):
        pass
    
    #입력값으로 들어오는 X 데이터셋의 크기만큼 모두 0값으로 만들어서 반환
    def predict(self,X):
        return np.zeros((len(X),1), dtype=bool)
    
# 사이킷런의 내장 데이터 셋인 load_digits()를 이용하여 MNIST 데이터 로딩
digits = load_digits()

print(digits.data)
print('### digits.data.shape:', digits.data.shape)
print(digits.target)
print('### digits.target.shape:', digits.target.shape)
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> [[ 0.  0.  5. ...  0.  0.  0.]
 [ 0.  0.  0. ... 10.  0.  0.]
 [ 0.  0.  0. ... 16.  9.  0.]
 ...
 [ 0.  0.  1. ...  6.  0.  0.]
 [ 0.  0.  2. ... 12.  0.  0.]
 [ 0.  0. 10. ... 12.  1.  0.]]
### digits.data.shape: (1797, 64)
[0 1 2 ... 8 9 8]
### digits.target.shape: (1797,)

</aside>

```python
digits.target == 7
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> array([False, False, False, ..., False, False, False])

</aside>

```python
# digits 번호가 7이면 Ture이고 이를 astype(int)로 1로 변환
# 7 아니면 False이고 0으로 변환

y = (digits.target ==7).astype(int)
X_train, X_test, y_train, y_test = train_test_split(digits.data, y, random_state=11)
```

```python
# 불균형한 레이블 데이터 분포도 확인
print('레이블 테스트 세트 크기:', y_test.shape)
print('테스트 세트 레이블 0과 1의 분포도')
print(pd.Series(y_test).value_counts())

# Dummy Classfier로 학습/예측/정확도 평가
# 들어오는 값들을 모두 0으로 예측하는 MyFakeClassfier()을 이용
# 7을 제외한 모든 숫자는 0으로 인식하기 때문에 0으로 예측할 확률이 높다. 이러한 예측을 가상으로 만든 것이 MyFakeClassfier
fakeclf = MyFakeClassfier()
fakeclf.fit(X_train, y_train)
fakepred = fakeclf.predict(X_test)
print('모든 예측을 0으로 하여도 정확도는:{:3f}'.format(accuracy_score(y_test, fakepred)))

# 모든 예측이 0임에도 불구하고 정확도가 0.9가 나왔다 => 문제 있음.
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> 레이블 테스트 세트 크기: (450,)

테스트 세트 레이블 0과 1의 분포도
0    405
1     45
dtype: int64

모든 예측을 0으로 하여도 정확도는:0.900000

</aside>

## 오차행렬(Confusion Matrix)

### 오차행렬이란?

- 오차 행렬은 이진 분류의 예측 오류가 얼마인지가 더불어 어떠한 유형의
예측 오류가 발생하고 있는지를 함께 나타내는 지표

![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%2027.png)

![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%2028.png)

- 예시)
- 의사가 암환자를 정상 환자로 잘못 진단한 것은 FN(False Negative)에 해당
- 의사가 정상 환자를 암환자로 잘못 진단한 것은 FP(False Positive)에 해당
- **정확도**는 전체 중 맞게 예측할 확률을 의미한다.
**정밀도**는 맞다고 예측했는데 실제 맞을 확률을 의미한다.
**민감도**는 실제 맞았는데 맞다고 예측했을 확률을 의미한다.
**특이도**는 실제 틀렸는데 틀렸다고 예측했을 확률을 의미한다.

### 적용

```python
from sklearn.metrics import confusion_matrix

# 앞절의 예측 결과인 fakepred와 실제 결과인 y_test의 Confusion Matrix 출력
confusion_matrix(y_test, fakepred)
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> array([[405,   0],
           [ 45,   0]], dtype=int64)

</aside>

- 정확도는 높게 나오지만 계산에서 0인 것들이 제대로 고려되지 않았음
- 그걸 고려해주는 정밀도와 재현율을 알아보자

## 정밀도(Precision)와 재현율(Recall)

### 정밀도와 재현율이란?

- **정밀도**
    - 예측을 Positive로 한 대상 중에 예측을 실제 값이 Positive로 일치한 데이터의 비율
    - 정밀도 = TP / (FP + TP)
- **재현율**
    - 실제값이 Positive인 대상 중에 예측과 실제 값이 Positive로 일치한 데이터의 비율
    - 재현율 = TP / (FN + TP)

### 업무에 따른 재현율과 정밀도의 상대적 중요도

- 재현율이 상대적으로 더 중요한 지표인 경우는 실제 Positive 양성의 데이터 예측을 Negative로 잘못 판단하게 되면 큰 영향이 발생하는 경우
⇒ 암 진단, 금융 사기 판별
- 정밀도가 상대적으로 더 중요한 지표는 실제 Negative 음성인 데이터 예측을 Positive 양성으로 잘못 판단하게 되면 큰 영향이 발생하는 경우
⇒ 스팸 메일
- 불균형한 레이블 클래스를 가지는 이진 분류 모델에서는 많은 데이터 중에서 중점적으로 찾아야 하는 매우 적은 수의 결과값에 Positive를 설정해 1값을 부여하고, 그렇지 않은 경우는 Negative로 0 값을 일반적으로 부여

### 정밀도/재현율 트레이드오프(Trade off)

- 정밀도 또는 재현율이 특별히 강조되어야 할 경우 분류의 결정 임계값(Threshold)을 조정해 정밀도 또는 재현율의 수치를 높일 수 있음
- 정밀도와 재현율은 상호 보완적인 평가 지표이기 때문에 어느 한쪽을 강제로 높이면 다른 하나의 수치는 떨어지기 쉬움
- 정밀도/재현율의 트레이드오프(Trade-off)
    
    ![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%2029.png)
    

### 적용

- **정확도와 정밀도**
    
    ```python
    from sklearn.metrics import accuracy_score, precision_score, recall_score
    
    print("정밀도:", precision_score(y_test, fakepred))
    print("재현율:", recall_score(y_test, fakepred))
    ```
    
    <aside>
    <img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> 정밀도: 0.0
    재현율: 0.0
    
    </aside>
    
    - 둘다 0이 나왔음, 정확도랑은 매우 큰 차이가 나는 것을 볼 수 있다.
    
    ```python
    from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
    
    # 오차행렬, 정확도, 정밀도, 재현율을 한꺼번에 계산하는 함수 생성
    
    def get_clf_eval(y_test, pred):
        confusion = confusion_matrix(y_test, pred)
        accuracy = accuracy_score(y_test, pred)
        precision = precision_score(y_test, pred)
        recall = recall_score(y_test, pred)
        print('오차행렬')
        print(confusion)
        print('정확도: {0: .4f}, 정밀도: {1:.4f}, 재현율: {2:.4f}'.format(accuracy, precision, recall))
    ```
    
    ```python
    import numpy as np
    import pandas as pd
    
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    
    # 원본 데이터를 재로딩, 데이터 가공, 학습데이터/테스트데이터 분할
    
    titanic_df = pd.read_csv('C:/JupyterTest/머신러닝/titanic_train.csv')
    y_titanic_df = titanic_df['Survived']
    X_titanic_df = titanic_df.drop('Survived',axis=1)
    X_titanic_df = transform_features(X_titanic_df)
    
    X_train, X_test, y_train, y_test = train_test_split(X_titanic_df,y_titanic_df, \
                                                       test_size=0.20, random_state=11)
    
    lr_clf = LogisticRegression()
    
    lr_clf.fit(X_train, y_train)
    pred = lr_clf.predict(X_test)
    get_clf_eval(y_test, pred)
    ```
    
    <aside>
    <img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> 오차행렬
    [[104  14]
     [ 13  48]]
    정확도:  0.8492, 정밀도: 0.7742, 재현율: 0.7869
    
    </aside>
    
    - 일반적인 Estimator를 사용하니까 정밀도와 재현율이 적당히 나오는 것을 볼 수 있다.
    
    - 평가지표들을 한번에 출력해주는 `classification_report`라는 scikit-learn 함수가 있음
    
    ```python
    from sklearn.metrics import classification_report
    print(classification_report(y_test, pred))
    ```
    
    <aside>
    <img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" />
    
    ![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%2030.png)
    
    </aside>
    
- ****Precision/Recall Trade-off****
    1. **predict_proba()**
    
    ```python
    pred_proba =lr_clf.predict_proba(X_test)
    pred = lr_clf.predict(X_test)
    print('pred_proba()결과 Shape: {0}'.format(pred_proba.shape))
    print('pred_proba array에서 앞 3개만 샘플로 추출 \n:', pred_proba[:3])
    
    # 예측 확율 array와 예측 결과값 array를 concatenate하여 예측 확률과 결과값을 한눈에 확인
    pred_proba_result = np.concatenate([pred_proba, pred.reshape(-1,1)],axis =1)
    print('두개의 class 중에서 더 큰 확률을 클래스 값으로 예측 \n', pred_proba_result[:3])
    ```
    
    <aside>
    <img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> pred_proba()결과 Shape: (179, 2)
    
    pred_proba array에서 앞 3개만 샘플로 추출
    : [[0.46208787 0.53791213]
     [0.87861827 0.12138173]
     [0.87710724 0.12289276]]
    
    두개 class 중에서 더 큰 확률을 클래스 값으로 예측
     [[0.46208787 0.53791213 1.        ]
     [0.87861827 0.12138173 0.        ]
     [0.87710724 0.12289276 0.        ]]
    
    </aside>
    
    - 이진 분류라서 열이 2개인 것을 볼 수 있다.
        - 첫 번째 열: 0 (Negative)으로 예측할 확률
        - 두 번째 열: 1 (Positive)로 예측할 확률
    - 두 열을 합치면 1
    - 0.5를 기준으로 하여 pred 값 확인
    
    1. **Binarizer**
    - scikit-learn의 Binarizer에서 `threshold`로 불리는 임곗값을 조정해서 분류를 진행할 수 있다.
    
    ```python
    from sklearn.preprocessing import Binarizer
    
    X = [[ 1, -1,  2],
        [ 2,  0,  0],
        [ 0,  1.1, 1.2]]
    
    # threshold 기준값보다 같거나 작으면 0을, 크면 1을 반환
    binarizer = Binarizer(threshold=1.1)                     
    print(binarizer.fit_transform(X))
    ```
    
    <aside>
    <img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> [[0. 0. 1.]
     [1. 0. 0.]
     [0. 0. 1.]]
    
    </aside>
    
    - 1.1보다 큰 값은 1로, 1.1보다 작거나 같은 값은 0으로 분류된 것을 확인
    - 분류 결정 임계값 0.5 기반에서 Binarizer를 이용하여 예측값 변환해보자
    - predict_proba()의 두 번째 열인 1을 예측하는 확률을 뽑아서, 그것이 0.5보다 큰지 작은지를 Binarizer로 판단하고, 평가하는 것이다.
    
    ```python
    from sklearn.preprocessing import Binarizer
    
    #Binarizer의 threshold 설정값. 분류 결정 임곗값임.  
    custom_threshold = 0.5
    
    # predict_proba( ) 반환값의 두번째 컬럼 , 즉 Positive 클래스 컬럼 하나만 추출하여 Binarizer를 적용
    pred_proba_1 = pred_proba[:,1].reshape(-1,1)
    
    binarizer = Binarizer(threshold=custom_threshold).fit(pred_proba_1) 
    custom_predict = binarizer.transform(pred_proba_1)
    
    get_clf_eval(y_test, custom_predict)
    ```
    
    <aside>
    <img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> 오차 행렬
    [[104  14]
     [ 13  48]]
    정확도: 0.8492, 정밀도: 0.7742, 재현율: 0.7869
    
    </aside>
    
    - 기본값인 `0.5`로 지정하니까 앞에서 한 것과 완전히 동일하게 나왔다.
    
    <aside>
    💡 predict_proba( ) 반환값에서 첫번째 열은 Negative 클래스에 대한 예측 확률, 두번째 열은 Positive 클래스에 대한 예측 확률이다.
    
    </aside>
    
    - 임계치를 0.4로 변경
    
    ```python
    custom_threshold = 0.4
    pred_proba_1 = pred_proba[:,1].reshape(-1,1)
    binarizer = Binarizer(threshold=custom_threshold).fit(pred_proba_1)
    custom_predict = binarizer.transform(pred_proba_1)
    
    get_clf_eval(y_test, custom_predict)
    ```
    
    <aside>
    <img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> 오차행렬
    [[98 20]
     [10 51]]
    정확도:  0.8324, 정밀도: 0.7183, 재현율: 0.8361
    
    </aside>
    
    - 임곗값을 낮추니까 정밀도는 낮아지고, 재현율은 높아졌다.
    
    - 반복문을 이용해서 임곗값 상승에 따른 정밀도와 재현율의 Trade-off를 확인
    
    ```python
    # 테스트를 수행할 모든 임곗값을 리스트 객체로 저장. 
    thresholds = [0.4, 0.45, 0.50, 0.55, 0.60]
    
    def get_eval_by_threshold(y_test , pred_proba_c1, thresholds):
        # thresholds list객체내의 값을 차례로 iteration하면서 Evaluation 수행.
        for custom_threshold in thresholds:
            binarizer = Binarizer(threshold=custom_threshold).fit(pred_proba_c1) 
            custom_predict = binarizer.transform(pred_proba_c1)
            print('임곗값:',custom_threshold)
            get_clf_eval(y_test , custom_predict)
    
    get_eval_by_threshold(y_test ,pred_proba[:,1].reshape(-1,1), thresholds )
    ```
    
    <aside>
    <img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> 임곗값: 0.4
    오차 행렬
    [[99 19]
     [10 51]]
    정확도: 0.8380, 정밀도: 0.7286, 재현율: 0.8361
    
    임곗값: 0.45
    오차 행렬
    [[103  15]
     [ 12  49]]
    정확도: 0.8492, 정밀도: 0.7656, 재현율: 0.8033
    
    임곗값: 0.5
    오차 행렬
    [[104  14]
     [ 13  48]]
    정확도: 0.8492, 정밀도: 0.7742, 재현율: 0.7869
    
    임곗값: 0.55
    오차 행렬
    [[109   9]
     [ 15  46]]
    정확도: 0.8659, 정밀도: 0.8364, 재현율: 0.7541
    
    임곗값: 0.6
    오차 행렬
    [[112   6]
     [ 16  45]]
    정확도: 0.8771, 정밀도: 0.8824, 재현율: 0.7377
    
    </aside>
    
    1. **precision_recall_curve()**
    - scikit-learn에서 임곗값별 정밀도와 재현율을 구하는 함수
    - 일반적으로 0.11 ~ 0.95 정도의 임곗값을 담은 ndarray와 이 임곗값에 해당하는 정밀도 및 재현율 값을 담은 ndarray를 반환
    
    ```python
    from sklearn.metrics import precision_recall_curve
    
    # 레이블 값이 1일때의 예측 확률을 추출 
    pred_proba_class1 = lr_clf.predict_proba(X_test)[:, 1] 
    
    # 실제값 데이터 셋과 레이블 값이 1일 때의 예측 확률을 precision_recall_curve 인자로 입력 
    precisions, recalls, thresholds = precision_recall_curve(y_test, pred_proba_class1 )
    print('반환된 분류 결정 임곗값 배열의 Shape:', thresholds.shape)
    print('반환된 precisions 배열의 Shape:', precisions.shape)
    print('반환된 recalls 배열의 Shape:', recalls.shape)
    
    print("thresholds 5 sample:", thresholds[:5])
    print("precisions 5 sample:", precisions[:5])
    print("recalls 5 sample:", recalls[:5])
    ```
    
    <aside>
    <img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> 반환된 분류 결정 임곗값 배열의 Shape: (143,)
    
    반환된 precisions 배열의 Shape: (144,)
    
    반환된 recalls 배열의 Shape: (144,)
    
    thresholds 5 sample: [0.10393302 0.10393523 0.10395998 0.10735757 0.10891579]
    
    precisions 5 sample: [0.38853503 0.38461538 0.38709677 0.38961039 0.38562092]
    
    recalls 5 sample: [1.         0.98360656 0.98360656 0.98360656 0.96721311]
    
    </aside>
    
    - 임계값의 변경에 따른 정밀도-재현율 변화 곡선을 그림
    
    ```python
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker
    %matplotlib inline
    
    def precision_recall_curve_plot(y_test, pred_proba_c1):
        #threshold ndarray와 이 threshold에 따른 정밀도, 재현율, ndarray 출출
        precicsons, recalls, thresholds = precision_recall_curve(y_test, pred_proba_c1)
        
        # x 축을 threshold값으로, y축은 정밀도, 재현율 값으로 각각 plot 수행.
        # 정밀도는 점섬으로 표시
        plt.figure(figsize=(8,6))
        treshold_boindary = thresholds.shape[0]
        plt.plot(thresholds, precisions[0:treshold_boindary],linestyle='--',
                 label='precision')
        plt.plot(thresholds, recalls[0:treshold_boindary], label='recall')
        
        # threshold 값 X 축의 Scalse을 0,1 단위로 변경
        start, end = plt.xlim()
        plt.xticks(np.round(np.arange(start, end, 0.1),2))
        
        # x축, y축 label과 legend 그리고 grid 설정
        plt.xlabel('Treshold value'); plt.ylabel('Precision and Recall value')
        plt.legend(); plt.grid()
        plt.show()
        
    precision_recall_curve_plot(y_test, lr_clf.predict_proba(X_test)[:,1])
    ```
    
    <aside>
    <img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" />
    
    ![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%2031.png)
    
    </aside>
    

## F1 Score

### F1 Score란?

- F1 스코어(Score)는 정밀도와 재현율을 결합한 지표
- 정밀도와 재현율이 어느 한쪽으로 치우치지 않는 수치를 나타낼 때 상대적으로 높은 값을 가짐

![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%2032.png)

### 적용

```python
# pred : 타이타닉 데이터 LogisitcRegression으로 fit() 후 predict() 한 것

from sklearn.metrics import f1_score
f1 = f1_score(y_test, pred)
print('F1 스코어: {0: .4f}'.format(f1))
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> `F1 스코어: 0.7805`

</aside>

- `get_clf_eval()` 에 F1 Score를 추가

```python
def get_clf_eval(y_test , pred):
    confusion = confusion_matrix( y_test, pred)
    accuracy = accuracy_score(y_test , pred)
    precision = precision_score(y_test , pred)
    recall = recall_score(y_test , pred)
    # F1 스코어 추가
    f1 = f1_score(y_test,pred)
    print('오차 행렬')
    print(confusion)
    # f1 score print 추가
    print('정확도: {0:.4f}, 정밀도: {1:.4f}, 재현율: {2:.4f}, F1:{3:.4f}'.format(accuracy, precision, recall, f1))

thresholds = [0.4 , 0.45 , 0.50 , 0.55 , 0.60]
pred_proba = lr_clf.predict_proba(X_test)
get_eval_by_threshold(y_test, pred_proba[:,1].reshape(-1,1), thresholds)
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> 임곗값: 0.4
오차 행렬
[[99 19]
 [10 51]]
정확도: 0.8380, 정밀도: 0.7286, 재현율: 0.8361, F1:0.7786

임곗값: 0.45
오차 행렬
[[103  15]
 [ 12  49]]
정확도: 0.8492, 정밀도: 0.7656, 재현율: 0.8033, F1:0.7840

임곗값: 0.5
오차 행렬
[[104  14]
 [ 13  48]]
정확도: 0.8492, 정밀도: 0.7742, 재현율: 0.7869, F1:0.7805

임곗값: 0.55
오차 행렬
[[109   9]
 [ 15  46]]
정확도: 0.8659, 정밀도: 0.8364, 재현율: 0.7541, F1:0.7931

임곗값: 0.6
오차 행렬
[[112   6]
 [ 16  45]]
정확도: 0.8771, 정밀도: 0.8824, 재현율: 0.7377, F1:0.8036

</aside>

- 임곗값이 0.6일 때 F1 Score가 가장 큰 것을 확인

## ****ROC Curve와 AUC****

### ****ROC Curve와 AUC란?****

- ROC 곡선(Receiver Operation Characteristic Curve)과 이에 기반한 AUC 스코어는 이진 분류의 예측 성능 측정에서 중요하게 사용되는 지표
- 일반적으로 의학 분야에서 많이 사용되지만, 머신러닝의 이진 분류 모델의 예측 성능을 판단하는 중요한 평가 지표
- ROC 곡선은 FPR(False Positive Rate)이 변할 때 TPR(True Positive Rate)이 어떻게 변하는지를 나타내는 곡선
- FPR을 X축으로, TPR을 Y축으로 잡으면 FPR이 변화에 따른 TPR의 변화가 곡선 형태로 나타냄
- 분류의 성능 지표로 사용되는 것은 ROC 곡선 면접에 기반한 AUC값으로 결정
- AUC(Area Under Curve) 값이 ROC 곡선 밑의 면적을 구한 것으로써일반적으로 1에 가까울수록 좋은 수치

### FPR의 변화에 따른 TPR의 변화 곡선

- TPR은 Ture Positive Rate의 약자이며, 이는 재현율을 나타냄 ⇒ 민감도
- FPR은 실제 Negative(음성)을 잘못 예측한 비율을 나타냄
(실제는 Negative인데 Positive로 또는 Negative로 예측한 것 중 Positive로 잘못 예측한 비율)
- FPR은 FP / (FP + TN)

### 적용

- `predict_proba()[:,1]`로 1 (Positive)로 예측할 확률을 뽑음
- `roc_curve()`로 FPR, TPR, 그에 해당하는 임곗값(Threshold)를 뽑음 (ndarray)
- 임곗값을 5 Step으로 추출해서 `thr_index`에 저장

```python
from sklearn.metrics import roc_curve

# 레이블 값이 1일 때의 예측 확률을 추출
pred_proba_class1 = lr_clf.predict_proba(X_test)[:,1]

fprs, tprs, thresholds = roc_curve(y_test, pred_proba_class1)
# 반환된 임계값 배열에서 샘플로 데이터를 추출하되, 임계값을 5 step으로 추출
# thresholds[0]은 max(예측확률)+1로 임의 설정됨. 이를 제외하기 위해 np.arange는 1부터 시작
thr_index = np.arange(1, thresholds.shape[0],5)
print('샘플 추출을 위한 임계값 배열의 index:', thr_index)
print('샘플 index로 추출한 임계값:', thresholds[thr_index][::5])  # 수정된 부분

# 5 step 단위로 추출된 임계값에 따른 FPR, TPR 값
print('샘플 임계값별 FPR:', np.round(fprs[thr_index][::5], 3))  # 수정된 부분
print('샘플 임계값별 TPR:', np.round(tprs[thr_index][::5], 3))  # 수정된 부분
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> 샘플 추출을 위한 임계값 배열의 index: [ 1  6 11 16 21 26 31 36 41 46 51]
샘플 index로 추출한 임계값: [0.96504653 0.4008847  0.10786876]
샘플 임계값별 FPR: [0.    0.169 0.797]
샘플 임계값별 TPR: [0.033 0.836 0.984]

</aside>

```python
from sklearn.metrics import roc_curve

# 레이블값이 1일 때의 예측 확률을 추출
pred_proba_class1 = lr_clf.predict_proba(X_test)[:,1]
print('max predict_proba:', np.max(pred_proba_class1))

fprs, tprs, thresholds = roc_curve(y_test, pred_proba_class1)
print('thresholds[0]:', thresholds[0])

#반환된 임계값 배열 로우가 47건이므로 샘플로 10건만 추출하되 임계값을 5 step으로 추출
thr_index = np.arange(0, thresholds.shape[0], 5)
print('샘플 추출을 위한 임계값 배열의 index 10개:', thr_index)
print('샘플용 10개의 임계값:', np.round(thresholds[thr_index],2))

# 5 step 단위로 추출된 임계값에 따른 FPR, TPR 값
print('샘플 임계값별 FPR:', np.round(fprs[thr_index],3))
print('샘플 임계값별 TPR:', np.round(fprs[thr_index],3))
```

<aside>
<img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" />

![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%2033.png)

</aside>

- AUC 구하기

```python
from sklearn.metrics import roc_auc_score

pred_proba = lr_clf.predict_proba(X_test)[:, 1]
roc_score = roc_auc_score(y_test, pred_proba)
print('ROC AUC 값: {0:.4f}'.format(roc_score))
```

- 성능지표를 구하는 get_clf_eval() 함수에 ROC AUC Score까지 추가

```python
def get_clf_eval(y_test, pred=None, pred_proba=None):
    confusion = confusion_matrix( y_test, pred)
    accuracy = accuracy_score(y_test , pred)
    precision = precision_score(y_test , pred)
    recall = recall_score(y_test , pred)
    f1 = f1_score(y_test,pred)
    # ROC-AUC 추가 
    roc_auc = roc_auc_score(y_test, pred_proba)
    print('오차 행렬')
    print(confusion)
    # ROC-AUC print 추가
    print('정확도: {0:.4f}, 정밀도: {1:.4f}, 재현율: {2:.4f}, F1: {3:.4f}, AUC:{4:.4f}'.format(accuracy, precision, recall, f1, roc_auc))
    
get_clf_eval(y_test, pred, pred_proba)
```

# **주요 분류**(Classification) **방법**

## **LogisticRegression**

### **LogisticRegression이란?**

- 데이터가 어떤 범주에 속할 확률을 0에서 1 사이의 값으로 예측하고 그 확률에 따라 가능성이 더 높은 범주에 속하는 것으로 분류해주는 지도 학습 알고리즘
- 독립변수를 input값으로 받아 종속변수가 1이 될 확률을 결과값으로 하는 sigmoid함수를 찾는 과정
- sigmoid함수
    
    종속변수가 1이 될 확률의 결과값을 plot으로 그렸을 때 S자 곡선이 나오는 함수
    
- 종속변수가 이항형 문제(즉, 유효한 범주의 개수가 두개인 경우)를 지칭할 때 사용된다.
- 사용 예시
    - 제품이 불량인지 양품인지 분류
    - 이메일이 스팸인지 정상메일인지 분류

### 주요 하이퍼 파라미터

- solver
    - lbfgs(defalut) : 최적화 병렬
    - liblinear : 다차원이고 작은 데이터에 적합
    - newton-cg : 좀 더 정교한 최적화
    - sag : 경사 하강법 기반의 최적화
    - sega : sag와 유사, L1 정규화 가능
- penalty : 규제. L1과 L2(default) 중 선택. 단, lbfgs, newton-cg, sag의 경우 L2만 가능.
- C : 규제 강도를 조절. 값이 작을 수록 규제 강도가 크다.

### 적용

```python
from sklearn.linear_model import LogisticRegression

# step 1 : 모델선언
model = LogisticRegression()

# step 2 : 모델 학습
model.fit(x_train, y_train)
prediction = model.predict(x_valid)
prediction[:5]
```

<aside>
▶️ `array([2, 1, 0, 1, 0])`

</aside>

```python
# step 4 : 평가
(prediction == y_valid).mean()
```

<aside>
▶️ `1.0`

</aside>

## ****SGDClassfier****

### ****SGDClassfier이란?****

- 확률적 경사 하강법
- 경사 하강법을 이용한 정규화된 선형 분류 모델
    - 경사 하강법 : 점진적으로 반복적인 계산을 통해 W파라미터(가중치) 값을 업데이트하면서 오류값이 최소가 되는 W파라미터를  구하는 방식
- 전체 데이터(Batch) 대신 일부 데이터의 모듬(Mini-Batch)를 사용하여 계산
- 다소 부정확할 수 있으나 계산 속도가 빠름.
- 미니 배치를 사용하여 학습하기 때문에 배치 경사 하강법보다 큰 데잉터를 학습 시킬 때 효과적임.
- 

### 적용

```python
from IPython.display import Image
from sklearn.linear_model import SGDClassifier

# 모델 선언
sgd = SGDClassifier(loss='log',
                      max_iter=5000,  #최대반복수
                      tol=1e-5,       # max_iter에 도달하지 않더라도 작업 중단
                      random_state=2) # 실행할 때마다 바뀌지 않게 초깃값

# 모델 학습
sgd.fit(x_train, y_train)

# 예측
prediction = sgd.predict(x_valid)
(prediction == y_valid).mean()
```

<aside>
▶️ `0.8157894736842105`

</aside>

## K-Nearest Neighbor

### K-Nearest Neighbor이란?

- 최근접 이웃 알고리즘
- 가장 가깝게 위치하는 멤버로 분류하는 방식

### 주요 하이퍼 파라미터

- n_neibors : 이웃의 개수를 지정 (기본값 5)
- p : 거리를 재는 방법 (1 : 맨해튼 거리, 2 : 유클리안거리(기본))
- n_jobs : CPU 코어 지증(기본값 1, -1은 모든 CPU 코어 사용)

### 적용

```python
from sklearn.neighbors import KNeighborsClassifier

knc = KNeighborsClassifier()
knc.fit(x_train, y_train)

knc_pred = knc.predict(x_valid)
(knc_pred == y_valid).mean()
```

<aside>
▶️ 0.9473684210526315

</aside>

```python
knc = KNeighborsClassifier(n_neighbors=9)
knc.fit(x_train, y_train)
knc_pred = knc.predict(x_valid)

(knc_pred == y_valid).mean()
```

<aside>
▶️ 0.9736842105263158

</aside>

## ****SVC****

### ****SVC란?****

- 서포트 벡터 머신
- 새로운 데이터가 어느 카테고리에 속할지 판단하는 비확률적 이진 선형 분류 모델을 만듦
- 경계로 표현되는 데이터들 중 가장 큰 폭을 가진 경계를 찾는 알고리즘
- 로지스틱 회귀분석과 같이 이진 분류만 가능

### 적용

```python
from sklearn.svm import SVC

svc = SVC(random_state = 0,)
svc.fit(x_train, y_train)
svc_pred = svc.predict(x_valid)

(svc_pred == y_valid).mean()
```

<aside>
▶️ 0.9736842105263158

</aside>

```python
svc_pred[:5]
```

<aside>
▶️ array([1, 0, 1, 1, 1])

</aside>

```python
# 각 클래스별 확률값을 return 해주는 decision_function()
svc.decision_function(x_valid)[:5]
```

<aside>
▶️ array([[-0.20912048,  2.23376113,  0.86697649],
       [ 2.22983376,  1.15500581, -0.25183065],
       [-0.23052329,  2.21459287,  1.10104249],
       [-0.23366655,  2.21779577,  1.10493102],
       [-0.18191884,  2.23726065,  0.81363042]])

</aside>

## 의사 결정 나무(Decision Tree)

### 의사결정나무란?

- 스무고개 게임과 유사
- if, else를 자동으로 찾아내 에측을 위한 규칙을 만드는 알고리즘
- 구조
    - 규칙 노드 : 규칙 조건
    - 리프 노드 : 결정된 클래스 값
    - 새로운 규칙 조건마다 서브 트리 생성
- 많은 규칙이 있을 수록 복잡 & 깊이가 깊어질수록→ 과적합
- 최대한 균일한 데이터 세트를 구성하도록 분할해야 함.
- 균일도만 신경쓰면 되기 때문에 피처의 스케일링이나 정규화 같은 전처리 작업 불필요

### 결정 트리 파라미터

| 파라미터 명 | 설명 |
| --- | --- |
| min_sample_split | - 노드를 분리하기 위한 최소한의 샘플 데이터 수로 과적합을 제어하는 데 사용
- 기본값은 2, 작게 설정할 수록 분할되는 노드가 많아져 과적합 가능성 증가 |
| min_sample_leaf | - 분할이 될 경우 왼쪽과 오른쪽 브랜치 노드에서 가져야 할 최소한의 데이터 수
- 과적합 제어 용도
- 비대칭적 데이터의 경우 특정 클래스의 데이터가 극도로 작을 수 있으므로 이 경우는 작게 설정 |
| max_feature | - 최적의 분할을 위해 고려할 최대 피처 개수
- 기본값은 None으로 데이터 세트의 모든 피처를 사용해 분할
- sqrt : 전체 피처 개수의 제곱근 만큼 선정
- auto = sqrt
- log : 전체 피처 중 log2(전체 피처 수)  |
| max_depth | - 트리의 최대 깊이 규정
- 기본값은 None → 클래스 값이 완벽하게 결정될 때까지 계속 분할 or min_sample_split보다 작아질 때 까지 깊이 증가 → 과적합 우려 |
| max_leaf_nodes | 말단 노드(leaf)의 최대 개수  |

### 시각화

- 어떠한 규칙을 가지고 트리를 생성하는지 시각적으로 보여

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

# DecisionTree Classifier 생성
dt_clf = DecisionTreeClassifier(random_state=156)

# 붓꽃 데이터를 로딩하고, 학습과 테스트 데이터 셋으로 분리
iris_data = load_iris()
X_train , X_test , y_train , y_test = train_test_split(iris_data.data, iris_data.target,
                                                       test_size=0.2,  random_state=11)

# DecisionTreeClassifer 학습. 
dt_clf.fit(X_train , y_train)
```

```python
from sklearn.tree import export_graphviz

# export_graphviz()의 호출 결과로 out_file로 지정된 tree.dot 파일을 생성함. 
export_graphviz(dt_clf, out_file="tree.dot", class_names=iris_data.target_names , \
feature_names = iris_data.feature_names, impurity=True, filled=True)
```

```python
import graphviz

# 위에서 생성된 tree.dot 파일을 Graphviz 읽어서 Jupyter Notebook상에서 시각화 
with open("tree.dot") as f:
    dot_graph = f.read()
graphviz.Source(dot_graph)
```

<aside>
▶️

![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%2034.png)

</aside>

- 피처별 중요도

```python
import seaborn as sns
import numpy as np
%matplotlib inline

# feature importance 추출 
print("Feature importances:\n{0}".format(np.round(dt_clf.feature_importances_, 3)))

# feature별 importance 매핑
for name, value in zip(iris_data.feature_names , dt_clf.feature_importances_):
    print('{0} : {1:.3f}'.format(name, value))

# feature importance를 column 별로 시각화 하기 
sns.barplot(x=dt_clf.feature_importances_ , y=iris_data.feature_names)
```

<aside>
▶️

![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%2035.png)

</aside>

# 앙상블 학습

## 개요

- 여러 개의 분류기를 생성하고 그  예측을 결합함으로써 보다 정확한 최종 예측을 도출하는 기법
- 단일 분류기보다 신뢰성이 높은 예측값을 얻는다.
- 앙상블 학습의 유형으로는 보팅, 배깅, 부스팅, 스태깅 등이 있다.

## 보팅(Voting)

### 보팅이란?

- 여러 개의 분류기가 투표를 통해 최종 예측 결과를 결정
- 배깅(Vagging)과 다른 점 : 보팅은 서로 다른 알고리즘을 가진 분류기를 결합. 배깅은 모두 같은 유형의 알고리즘 기반(데이터 샘플링은 다르게 가져감)

### 보팅의 유형

- 하드 보팅 (Hard Voting)
    - 분류기들이 예측한 결과값들 중 다수의 분류기가 결정한 예측값을 최종 보팅 결과값으로 선정
- 소프트 보팅 (Soft Voting)
    - 레이블 값 결정 확률을 모두 더하고 이를 평균해서 이들 중 확률이 가장 높은 레이블 값을 최종 보팅 결과값으로 선정

### 보팅 분류기(Voting Classifier)

- 사이킷런은 보팅 방식의 앙상블을 구현한 VotingClassfier 클래스를 제공
- **유방암 데이터 세트 예측 분석**
    
    ```python
    import pandas as pd
    
    from sklearn.ensemble import VotingClassifier
    from sklearn.linear_model import LogisticRegression
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.datasets import load_breast_cancer
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    
    cancer = load_breast_cancer()
    
    data_df = pd.DataFrame(cancer.data, columns=cancer.feature_names)
    data_df.head(3)
    ```
    
    <aside>
    <img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" />
    
    ![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%2036.png)
    
    </aside>
    
    - 개별 모델은 로지스틱 회귀와 KNN
    - VotingClassifier의 인자
        - estimators : 리스트 값으로, 보팅에 사용될 여러 개의 Classfier 객체들을 튜플 형식으로 입력 받는다.
        - voting : hard, soft 보팅 방식 지정
    
    ```python
    # 개별 모델은 로지스틱 회귀와 KNN 임. 
    lr_clf = LogisticRegression(solver='liblinear')
    knn_clf = KNeighborsClassifier(n_neighbors=8)
    
    # 개별 모델을 소프트 보팅 기반의 앙상블 모델로 구현한 분류기 
    vo_clf = VotingClassifier( estimators=[('LR',lr_clf),('KNN',knn_clf)] , voting='soft' )
    
    X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, 
                                                        test_size=0.2 , random_state= 156)
    
    # VotingClassifier 학습/예측/평가. 
    vo_clf.fit(X_train , y_train)
    pred = vo_clf.predict(X_test)
    print('Voting 분류기 정확도: {0:.4f}'.format(accuracy_score(y_test , pred)))
    
    # 개별 모델의 학습/예측/평가.
    classifiers = [lr_clf, knn_clf]
    for classifier in classifiers:
        classifier.fit(X_train , y_train)
        pred = classifier.predict(X_test)
        class_name= classifier.__class__.__name__
        print('{0} 정확도: {1:.4f}'.format(class_name, accuracy_score(y_test , pred)))
    ```
    
    <aside>
    <img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> Voting 분류기 정확도: 0.9561
    LogisticRegression 정확도: 0.9474
    KNeighborsClassifier 정확도: 0.9386
    
    </aside>
    
    - 보팅 분류기 정확도가 조금 높게 나왔으나, 눈에 띄는 성능 향상은 아님.
    - 그럼에도 불구하고 단일 알고리즘보다는 뛰어난 예측 성능을 가짐.
    

## 배깅(Bagging)

### 배깅이란?

- 같은 알고리즘으로 여러 개의 분류기를 만들어서 보팅으로 최종 결정하는 알고리즘
- 서로 다른 데이터 샘플링을 가져가면서 학습을 수행
- 배깅의 대표적인 알고리즘은 ‘랜덤 포레스트’

### 랜덤 포레스트

- 랜덤 포레스트의 기반 알고리즘은 결정트리
- 여러 개의 결정트리 분류기가 전체 데이터에서 배깅 방식으로 각자의 데이터 샘플링해 개별적으로 학습 수행 후 최종 보팅을 통해 예측 결정함.
- 개별 트리가 학습하는 데이터  세트는 전체 데이터에서 일부가 중첩되게 샘플링된 데이터 세트임. ⇒ 부트스트래핑 분할 방식
- 이렇게 생성된 데이터 세트에 결정 트리 분류기를 적용하는 것이 랜덤 포레스

### RandomForesstClassifier

- **사용자 행동 인식 데이터 세트**
    - 결정트리에서 사용된 정제된 데이터
    
    ```python
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score
    import pandas as pd
    import warnings
    warnings.filterwarnings('ignore')
    
    # 결정 트리에서 사용한 get_human_dataset( )을 이용해 학습/테스트용 DataFrame 반환
    X_train, X_test, y_train, y_test = get_human_dataset()
    
    # 랜덤 포레스트 학습 및 별도의 테스트 셋으로 예측 성능 평가
    rf_clf = RandomForestClassifier(random_state=0)
    rf_clf.fit(X_train , y_train)
    pred = rf_clf.predict(X_test)
    accuracy = accuracy_score(y_test , pred)
    print('랜덤 포레스트 정확도: {0:.4f}'.format(accuracy))
    ```
    
    <aside>
    <img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> 랜덤 포레스트 정확도: 0.9253
    
    </aside>
    

### 랜덤 포레스트 하이퍼 파라미터 및 튜닝

- **하이퍼 파라미터 종류**
    - n_estimatirs
        - 랜덤 포레스트에서 결정 트리 개수를 지정.
        - 디폴트는 10개
    - max_features
        - 최적 분할을 위해 고려할 최대 feature 수
        - 디폴트는 auto (=sqrt) ⇒ sqrt(전체 feature 수)
    - max_depth, min_sample, min_sample_split와 같이 결정트리에서 사용된 하이퍼 파라미터가 동일하게 적용됨.
- **사용자 행동 인식 데이터 세트**
    - GridSearchCV 이용
    - n_estimators = 100, CV = 2 로 설정해 최적 파라미터 구해보자
    
    ```python
    from sklearn.model_selection import GridSearchCV
    
    params = {
        'n_estimators':[100], # 결정 트리 개수 지정
        'max_depth' : [6, 8, 10, 12], # 트리의 최대 깊이 지정
        'min_samples_leaf' : [8, 12, 18 ], # 분할된 경우 왼족, 오른쪽의 브랜치 노드에서 가져가야 할 최소한의 샘플 데이터 수
        'min_samples_split' : [8, 16, 20] # 노드를 분할하기 위한 최소한의 샘플 데이터 수 => 과적합 제어
    }
    # RandomForestClassifier 객체 생성 후 GridSearchCV 수행
    rf_clf = RandomForestClassifier(random_state=0, n_jobs=-1)
    grid_cv = GridSearchCV(rf_clf , param_grid=params , cv=2, n_jobs=-1 )
    grid_cv.fit(X_train , y_train)
    
    print('최적 하이퍼 파라미터:\n', grid_cv.best_params_)
    print('최고 예측 정확도: {0:.4f}'.format(grid_cv.best_score_))
    ```
    
    <aside>
    <img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> 최적 하이퍼 파라미터:
     {'max_depth': 10, 'min_samples_leaf': 8, 'min_samples_split': 8, 'n_estimators': 100}
    
    최고 예측 정확도: 0.9180
    
    </aside>
    
    - 'max_depth': 10, 'min_samples_leaf': 8, 'min_samples_split': 8 일 때 두개의 CV 세트에서 약 91.8%의 평균 정확도가 측정 됨.
    
    - 이 추출된 파라미터로 다시 RandomForestClassfier 학습 후 별도의 테스트 데이터세트에서 예측 성능 측정
    
    ```python
    rf_clf1 = RandomForestClassifier(n_estimators=100, max_depth=10, min_samples_leaf=8, \
                                     min_samples_split=8, random_state=0)
    rf_clf1.fit(X_train , y_train)
    pred = rf_clf1.predict(X_test)
    print('예측 정확도: {0:.4f}'.format(accuracy_score(y_test , pred)))
    ```
    
    <aside>
    <img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> 예측 정확도: 0.9196
    
    </aside>
    
    - 피처 중요도 막대그래프 시각화
    
    ```python
    import matplotlib.pyplot as plt
    import seaborn as sns
    %matplotlib inline
    
    ftr_importances_values = rf_clf1.feature_importances_
    ftr_importances = pd.Series(ftr_importances_values,index=X_train.columns  )
    ftr_top20 = ftr_importances.sort_values(ascending=False)[:20]
    
    plt.figure(figsize=(8,6))
    plt.title('Feature importances Top 20')
    sns.barplot(x=ftr_top20 , y = ftr_top20.index)
    fig1 = plt.gcf()
    plt.show()
    plt.draw()
    fig1.savefig('rf_feature_importances_top20.tif', format='tif', dpi=300, bbox_inches='tight')
    ```
    
    <aside>
    <img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" />
    
    ![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%2037.png)
    
    </aside>
    

## GBM(Gradient Boosting Machine)

### 부스팅이란?

- 여러 개의 약한 학습기(week learner)를 순차적으로 학습-예측하면서 잘못 예측한 데이터에 가중치 부여를 통해 개선해 가면서 학습하는 방식
- 에이다부스트와 GBM이 있음.

### GBM

- 가중치 업데이트를 경사 하강법을 이용
- 반복 수행을 통해 오류를 최소화할 수 있도록 가중치의 업데이트 값을 도출하는 기법

### GradientBoostingClassfier

- **사용자 행동 인식 데이터 세트**
    - 결정트리에서 사용된 정제된 데이터 사용
    
    ```python
    from sklearn.ensemble import GradientBoostingClassifier
    import time
    import warnings
    warnings.filterwarnings('ignore')
    
    X_train, X_test, y_train, y_test = get_human_dataset()
    
    # GBM 수행 시간 측정을 위함. 시작 시간 설정.
    start_time = time.time()
    
    gb_clf = GradientBoostingClassifier(random_state=0)
    gb_clf.fit(X_train , y_train)
    gb_pred = gb_clf.predict(X_test)
    gb_accuracy = accuracy_score(y_test, gb_pred)
    
    print('GBM 정확도: {0:.4f}'.format(gb_accuracy))
    print("GBM 수행 시간: {0:.1f} 초 ".format(time.time() - start_time))
    ```
    
    <aside>
    <img src="https://www.notion.so/icons/playback-play_red.svg" alt="https://www.notion.so/icons/playback-play_red.svg" width="40px" /> GBM 정확도: 0.9389
    GBM 수행 시간: 547.3 초
    
    </aside>
    
    - 기본 파라미터만으로 000%의 예측 정확도로 랜덤 포레스트보다 나은 예측 성능을 나타냄.
    - 그러나 수행시간이 오래 걸리고 하이퍼 파라미터 튜닝 노력도 더  필요

### GBM 하이퍼 파라미터

- n_estimators, max_depth, max_features와 같은 트리 파라미터는 결정 트리, 랜덤 포레스트에서 언급했으므로 생략
- loss
    - 경사 하강법에서 사용할 비용 함수를 지정
    - 보통 기본값인 deviance를 그대로 적용
- learnig_rate
    - GBM이 학습을 진행할 때 마다 적용하는 학습률
    - Weak learner가 순차적으로 오류 값을 보정해 나가는데 적용하는 계수. 0~1 사이의 값을 지정할 수 있으며 기본 값은 0.1임.
    - 너무 작은 값을 적용하면 예측 성능이 높아질 가능성이 높다.
    - 반대로 큰 값을 적용하면 최소 오류 값을 찾지 못하고 그냥 지나쳐 버려 예측 성능이 떨어질 가능성이 높다.
        
        ⇒ n_estimators와 조합해 사용 해야 함.
        
- n_estimators
    - weak learner의 개수
    - 기본값 = 100
    - 많을 수록 예측 성능이 일정 수준까지 높아질 수 있음.
- subsample
    - weak learner가 학습에 사용하는 데이터 샘플링의 비율
    - 기본값 = 1 (전체 학습 데이터를 기반으로 학습)
    0.5 이면 전체 학습 데이터의 50%를 학습
    - 과적합이 염려되는 경우 1보다 작은 값으로 설정
    

## XGBoost(eXtra Gradient Boost)

### XGBoost란?

- 부스팅 계열 알고리즘
- 트리 기반의 앙상블 학습
- 분류에 있어 다른 머신러닝보다 뛰어난 예측 성능
- 주요 장점
    - 뛰어난 예측 성능
    - GBM 대비 빠른 수행 시간
    - 과적합 규제
    - Tree puring (지나치게 많은 분할 발생 방지)
    - 자체 내장된 교차 검증
    - 결손값 자체 처리

### XGBoost 하이퍼 파라미터

- learning_rate
    - GBM의 학습률과 같은 파라미터
    - 부스팅 스텝을 반복적으로 수행할 때 업데이트되는 학습률 값
    - 디폴트 = 0.1, 보통 0.01~0.2 선호
- subsample
    - 트리가 커져서 과적합되는 것을 제어하기 위해 데이터를 샘플링하는 비율을 지정
    - 0.5로 지정하면 전체 데이터의 절반을 트리르 생성하는 데 사용
    - 보통 0,5~1 사이의 값을 사용
- reg_lambda
    - L2 Regularization 적용 값
    - 피처 개수가 많을 경우 적용을 검토하며 값이 클수록 과적합 감소 효과가 있음.
- reg_alpha
    - L1 Regularization 적용 값
    - 피처 개수가 많을 경우 적용을 검토하며 값이 클수록 과적합 감소 효과가 있음.

### XGBClassifier

- **유방암 데이터 세트**
    - xgboost 설치 필요
    
    ```python
    !pip install xgboost
    ```
    
    ```python
    import xgboost as xgb
    from xgboost import plot_importance
    import pandas as pd
    import numpy as np
    from sklearn.datasets import load_breast_cancer
    from sklearn.model_selection import train_test_split
    import warnings
    warnings.filterwarnings('ignore')
    
    dataset = load_breast_cancer()
    X_features= dataset.data
    y_label = dataset.target
    
    cancer_df = pd.DataFrame(data=X_features, columns=dataset.feature_names)
    cancer_df['target']= y_label
    cancer_df.head(3)
    ```
    
    <aside>
    ▶️
    
    ![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%2038.png)
    
    </aside>
    
    ```python
    # cancer_df에서 feature용 DataFrame과 Label용 Series 객체 추출
    # 맨 마지막 칼럼이 Label임. Feature용 DataFrame은 cancer_df의 첫번째 칼럼에서 맨 마지막 두번째 칼럼까지를 :-1 슬라이싱으로 추출.
    X_features = cancer_df.iloc[:, :-1]
    y_label = cancer_df.iloc[:, -1]
    
    # 전체 데이터 중 80%는 학습용 데이터, 20%는 테스트용 데이터 추출
    X_train, X_test, y_train, y_test=train_test_split(X_features, y_label,
                                             test_size=0.2, random_state=156 )
    ```
    
    - 모델의 예측 성능을  평가하는 get_clf_eval() 생성
    
    ```python
    from sklearn.metrics import confusion_matrix, accuracy_score
    from sklearn.metrics import precision_score, recall_score
    from sklearn.metrics import f1_score, roc_auc_score
    
    def get_clf_eval(y_test, pred=None, pred_proba=None):
        confusion = confusion_matrix( y_test, pred)
        accuracy = accuracy_score(y_test , pred)
        precision = precision_score(y_test , pred)
        recall = recall_score(y_test , pred)
        f1 = f1_score(y_test,pred)
        # ROC-AUC 추가 
        roc_auc = roc_auc_score(y_test, pred_proba)
        print('오차 행렬')
        print(confusion)
        # ROC-AUC print 추가
        print('정확도: {0:.4f}, 정밀도: {1:.4f}, 재현율: {2:.4f},\
        F1: {3:.4f}, AUC:{4:.4f}'.format(accuracy, precision, recall, f1, roc_auc))
    ```
    
    - 예측 수행
    
    ```python
    # 사이킷런 래퍼 XGBoost 클래스인 XGBClassifier 임포트
    from xgboost import XGBClassifier
    
    xgb_wrapper = XGBClassifier(n_estimators=400, learning_rate=0.1, max_depth=3)
    xgb_wrapper.fit(X_train, y_train)
    w_preds = xgb_wrapper.predict(X_test)
    w_pred_proba = xgb_wrapper.predict_proba(X_test)[:, 1]
    ```
    
    - 예측 성능 평가
    
    ```python
    get_clf_eval(y_test , w_preds, w_pred_proba)
    ```
    
    <aside>
    ▶️ 오차 행렬
    [[35  2]
     [ 1 76]]
    정확도: 0.9737, 정밀도: 0.9744, 재현율: 0.9870,    F1: 0.9806, AUC:0.9951
    
    </aside>
    

## LightGBM

### LightGBM이란?

- 부스팅 계열 알고리즘
- 리프 중심 트리 분할
    - 최대 손실 값을 가지는 리프 노드를 지속적으로 분할
    - 트리의 깊이가 깊어지고 비대칭적인 규칙 트리 생성
    - 예측 오류 손실을 최소화
- 사이킷런 패키지가 아님
- XGBoost 대비 장점
    - 빠른 학습과 예측 수행 시간
    - 더 적은 메모리 사용
    - 카테고리형 피처의 자동 변환과 최적 분할
    (원-핫 인코딩 등을 사용하지 않고도 카테고리형 피처를 최적으로 변환하고 이에 따른 노드 분할 수행)

### LightGBM 하이퍼 파라미터

- **주요 하이퍼 파라미터**
    - num_iterations [default=100] : 반복 수행하려는 트리의 개수
    - learnig_rate [default=0.1] : 0~1 사이의 값을 지정하며 부스팅 스텝을 반복적으로 수행할 때 업데이트되는 확률 값
    - max_depth [default=-1] : 트리 기반 알고리즘의 max_depth
    - min_child_samples [default=20] : 결정 트리의 min_sample_leaf와 같은 파라미터
    - num_leaves [default=31] : 하나의 트리가 가질 수 있는 최대 리프 개수
    - boosting [default=gbdt] : 부스팅의 트리를 생성하는 알고리즘 기술
        - gbdt : 일반적인 그래디언트 부스팅 결정 트리
        - rf : 랜덤 포레스트
    - bagging_fraction [default=1.0] : 트리가 커져서 과적합되는 것을 제어하기 위해 데이터 샘플링하는 비율을 지정
    - feature_fraction [default=1.0] : 개별 트리를 학습할 때마다 무작위로 선택하는 피처의 비율. 과적합을 막기 위해 사용.
    - lambda_l2 [default=0.0] : L2 regulation 제어를 위한 값
    - lambda_l1 [default=0.0] : L1 regulation 제어를 위한 값
- **하이퍼 파라미터 튜닝 방안**
    - num_leaves의 개수를 중심으로 min_child_saples, max_depth를 함께 조정하면서 모델의 복잡도를 줄이는 것이 기본 튜닝 방안
    - learning_rate를 작게 하면서 n_estimators를 크게 하는 부스팅 계열 튜닝 방안

### LGBMClassifier

- **위스콘신 유방암 예측**
    
    ```python
    !pip install lightgbm
    ```
    
    ```python
    from lightgbm import LGBMClassifier
    import pandas as pd
    import numpy as np
    from sklearn.datasets import load_breast_cancer
    from sklearn.model_selection import train_test_split
    from lightgbm import LGBMClassifier
    
    dataset = load_breast_cancer()
    
    cancer_df = pd.DataFrame(data=dataset.data, columns=dataset.feature_names)
    cancer_df['target'] = dataset.target
    X_features = cancer_df.iloc[:, :-1]
    y_label = cancer_df.iloc[:, -1]
    
    # 전체 데이터 중 80%는 학습용 데이터, 20%는 테스트용 데이터 추출
    X_train, X_test, y_train, y_test = train_test_split(X_features, y_label, test_size=0.2, random_state=156)
    
    # 위에서 만든 X_train, y_train을 다시 쪼개서 90%는 학습과 10%는 검증용 데이터로 분리
    X_tr, X_val, y_tr, y_val = train_test_split(X_train, y_train, test_size=0.1, random_state=156)
    
    # 앞서 LightGBM에서는 조기 중단을 위해 n_estimators 값을 적절하게 설정하는 방법을 사용.
    lgbm_wrapper = LGBMClassifier(n_estimators=1000, learning_rate=0.05, verbosity=-1)  # -1로 설정하여 메시지 출력하지 않음
    
    # LightGBM는 eval_set에 검증 세트를 지정하여 학습 중 검증 세트의 성능 모니터링
    evals = [(X_tr, y_tr), (X_val, y_val)]
    lgbm_wrapper.fit(X_tr, y_tr, eval_metric="logloss", eval_set=evals)
    
    # 검증 세트에서 성능이 개선되지 않으면 자동으로 학습 중단됨
    preds = lgbm_wrapper.predict(X_test)
    pred_proba = lgbm_wrapper.predict_proba(X_test)[:, 1]
    ```
    
    ```python
    from sklearn.metrics import confusion_matrix, accuracy_score
    from sklearn.metrics import precision_score, recall_score
    from sklearn.metrics import f1_score, roc_auc_score
    
    def get_clf_eval(y_test, pred=None, pred_proba=None):
        confusion = confusion_matrix( y_test, pred)
        accuracy = accuracy_score(y_test , pred)
        precision = precision_score(y_test , pred)
        recall = recall_score(y_test , pred)
        f1 = f1_score(y_test,pred)
        # ROC-AUC 추가 
        roc_auc = roc_auc_score(y_test, pred_proba)
        print('오차 행렬')
        print(confusion)
        # ROC-AUC print 추가
        print('정확도: {0:.4f}, 정밀도: {1:.4f}, 재현율: {2:.4f},\
        F1: {3:.4f}, AUC:{4:.4f}'.format(accuracy, precision, recall, f1, roc_auc))
    ```
    
    ```python
    get_clf_eval(y_test, preds, pred_proba)
    ```
    
    <aside>
    ▶️ 오차 행렬
    [[34  3]
     [ 2 75]]
    정확도: 0.9561, 정밀도: 0.9615, 재현율: 0.9740,    F1: 0.9677, AUC:0.9940
    
    </aside>
    
    ```python
    # plot_importance( )를 이용하여 feature 중요도 시각화
    from lightgbm import plot_importance
    import matplotlib.pyplot as plt
    %matplotlib inline
    
    fig, ax = plt.subplots(figsize=(10, 12))
    plot_importance(lgbm_wrapper, ax=ax)
    plt.savefig('lightgbm_feature_importance.tif', format='tif', dpi=300, bbox_inches='tight')
    ```
    
    <aside>
    ▶️
    
    ![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%2039.png)
    
    </aside>
    

## Staking

### Staking이란?

- 개별적인 여러 알고리즘을 서로 결합해 예측 결과를 도출
- 위는 배깅, 부스팅과 같은 특징이지만 개별 알고리즘으로 예측한 데이터를 기반으로 다시 예측을 수행한다는 차이가 있다.
⇒ 개별 알고리즘의 예측 결과 데이터 세트를 최종 메타 데이터 세트로 만들어 별도 ML 알고리즘으로 최종 학습 수행하고 테스트 데이터를 기반으로 다시 최종 예측을 수

---

---

# 회귀

# 회귀란?

## 회귀의 특징

- 예측 값이 연속형 숫자 값이다. (분류는 이산형 클래스)
- 회귀 예측의 핵심 : 주어진 피처와 결정 값 데이터 기반에서 학습을 통해 최적의 회귀 계수를 찾아내는 것
- 최적의 회귀 모델을 만든 다는 것 = 전체 데이터의 잔차(오류 값) 합이 최소가 되는 모델을 만드는 것
- 동시에 오류 값 합이 최소가 될 수 있는 최적의 회귀 계수를 찾는 것
    - 보통 오류 합 계산할 때는 절대값을 취해서 더하거나 (Mean Absolute Eooro) 오류 값의 제곱을 구해서 더하는 방식 (RSS)
    - 일반적으로 RSS 사용

# 주요 회귀  방법

## 선형 회귀(LinearRegression)

### LinearRegression 란?

- 선형 회귀
- RSS를 최소화해 OLS(Ordiary Least Squares) 추정 방식

### 적용

- **보스턴 주택 가격 회귀 구현**
    
    ```python
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns
    from scipy import stats
    from sklearn.datasets import load_boston
    import warnings
    warnings.filterwarnings('ignore')  #사이킷런 1.2 부터는 보스턴 주택가격 데이터가 없어진다는 warning 메시지 출력 제거
    %matplotlib inline
    
    # boston 데이타셋 로드
    boston = load_boston()
    
    # boston 데이타셋 DataFrame 변환 
    bostonDF = pd.DataFrame(boston.data , columns = boston.feature_names)
    
    # boston dataset의 target array는 주택 가격임. 이를 PRICE 컬럼으로 DataFrame에 추가함. 
    bostonDF['PRICE'] = boston.target
    print('Boston 데이타셋 크기 :',bostonDF.shape)
    bostonDF.head()
    ```
    
    <aside>
    ▶️ Boston 데이타셋 크기 : (506, 14)
    
    ![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%2040.png)
    
    </aside>
    
    - Null 값 없으며, 모두 float 형
    
    - 각 컬럼별로 주택가격에 미치는 영향도를 조사
        - 8개의 컬럼에 대해 값이 증가할수록 PRICE 값이 어떻게 변하는지 확인
    
    ```python
    # 2개의 행과 4개의 열을 가진 subplots를 이용. axs는 4x2개의 ax를 가짐.
    fig, axs = plt.subplots(figsize=(16,8) , ncols=4 , nrows=2)
    lm_features = ['RM','ZN','INDUS','NOX','AGE','PTRATIO','LSTAT','RAD']
    for i , feature in enumerate(lm_features):
        row = int(i/4)
        col = i%4
        # 시본의 regplot을 이용해 산점도와 선형 회귀 직선을 함께 표현
        sns.regplot(x=feature , y='PRICE',data=bostonDF , ax=axs[row][col])
    
    fig1 = plt.gcf()
    fig1.savefig('p322_boston.tif', format='tif', dpi=300, bbox_inches='tight')
    ```
    
    <aside>
    ▶️
    
    ![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%2041.png)
    
    </aside>
    
    - 다른 컬럼보다 RM과 LSTAT의 PRICE 영향도가 가장 두드러지게 나타남.
        - RM(방 개수)가 클수록 가격 증가
        - LSTAT(하위 계층 비율)이 많을수록 가격 감소
    
    - 학습과 테스트 데이터 세트로 분리하고 학습/예측/평가 수행
    
    ```python
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error, r2_score
    
    y_target = bostonDF['PRICE']
    X_data = bostonDF.drop(['PRICE'],axis=1,inplace=False)
    
    X_train , X_test , y_train , y_test = train_test_split(X_data , y_target ,test_size=0.3, random_state=156)
    
    # Linear Regression OLS로 학습/예측/평가 수행. 
    lr = LinearRegression()
    lr.fit(X_train ,y_train )
    y_preds = lr.predict(X_test)
    mse = mean_squared_error(y_test, y_preds)
    rmse = np.sqrt(mse)
    
    print('MSE : {0:.3f} , RMSE : {1:.3F}'.format(mse , rmse))
    print('Variance score : {0:.3f}'.format(r2_score(y_test, y_preds)))
    ```
    
    <aside>
    ▶️ MSE : 17.297 , RMSE : 4.159
    Variance score : 0.757
    
    </aside>
    
    ```python
    print('절편 값:',lr.intercept_)
    print('회귀 계수값:', np.round(lr.coef_, 1))
    ```
    
    <aside>
    ▶️ 절편 값: 40.99559517216412
    회귀 계수값: [ -0.1   0.1   0.    3.  -19.8   3.4   0.   -1.7   0.4  -0.   -0.9   0.
      -0.6]
    
    </aside>
    
    - coef_ 속성은 회귀 계수 값만 가지고 있으므로 이를 피처별 회귀 계수 값으로 다시 매핑
    
    ```python
    # 회귀 계수를 큰 값 순으로 정렬하기 위해 Series로 생성. index가 칼럼명에 유의
    coeff = pd.Series(data=np.round(lr.coef_, 1), index=X_data.columns )
    coeff.sort_values(ascending=False)
    ```
    
    <aside>
    ▶️ RM          3.4
    CHAS        3.0
    RAD         0.4
    ZN          0.1
    INDUS       0.0
    AGE         0.0
    TAX        -0.0
    B           0.0
    CRIM       -0.1
    LSTAT      -0.6
    PTRATIO    -0.9
    DIS        -1.7
    NOX       -19.8
    dtype: float64
    
    </aside>
    
    - 교차 검증
    
    ```python
    from sklearn.model_selection import cross_val_score
    
    y_target = bostonDF['PRICE']
    X_data = bostonDF.drop(['PRICE'],axis=1,inplace=False)
    lr = LinearRegression()
    
    # cross_val_score( )로 5 Fold 셋으로 MSE 를 구한 뒤 이를 기반으로 다시  RMSE 구함. 
    neg_mse_scores = cross_val_score(lr, X_data, y_target, scoring="neg_mean_squared_error", cv = 5)
    rmse_scores  = np.sqrt(-1 * neg_mse_scores)
    avg_rmse = np.mean(rmse_scores)
    
    # cross_val_score(scoring="neg_mean_squared_error")로 반환된 값은 모두 음수 
    print(' 5 folds 의 개별 Negative MSE scores: ', np.round(neg_mse_scores, 2))
    print(' 5 folds 의 개별 RMSE scores : ', np.round(rmse_scores, 2))
    print(' 5 folds 의 평균 RMSE : {0:.3f} '.format(avg_rmse))
    ```
    
    <aside>
    ▶️ 5 folds 의 개별 Negative MSE scores:  [-12.46 -26.05 -33.07 -80.76 -33.31]
     5 folds 의 개별 RMSE scores :  [3.53 5.1  5.75 8.99 5.77]
     5 folds 의 평균 RMSE : 5.829
    
    </aside>
    

## 규제 선형 모델(릿지, 라쏘, 엘라스틱넷)

### alpha와 회귀 계수의 관계

- 선형 모델의 비용 함수는 RSS(실제 값과 예측값의 차이)를 최소화 하는 것
- 비용 함수는 학습 데이터와 잔차 오류 값을 최소로 하는 RSS 최소화 방법과 과적합을 방지하기 위해 회귀 계수 값이 커지지 않도록 하는 방법이 서로 균형을 이뤄야 함.
- 이를 위해 학습 데이터의 적합 정도와 회귀 계수 값의 크기를 제어하는 것이 alpha
    
    ![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%2042.png)
    

<aside>
💡 alpha 값을 크게 하면 비용 함수는 회귀 계수 W의 값을 작게 해 과적합을 개선
alpha 값을 작게 하면 회귀 계수 W의 값이 커져도 어느 정도 상쇄가 가능하무로 학습 데이터 적합을 개선할 수 있음

</aside>

- 이처럼 비용함수에 alpha 값으로 패널티를 부여해 회귀 계수 값의 크기를 감소시켜 과적합을 개선하는 방식을 규제라고 부름

### 릿지 회귀

- alpha L2 규제 계수에 해당
- 적용
    
    ```python
    # 앞의 LinearRegression예제에서 분할한 feature 데이터 셋인 X_data과 Target 데이터 셋인 Y_target 데이터셋을 그대로 이용 
    from sklearn.linear_model import Ridge
    from sklearn.model_selection import cross_val_score
    
    # boston 데이타셋 로드
    boston = load_boston()
    
    # boston 데이타셋 DataFrame 변환 
    bostonDF = pd.DataFrame(boston.data , columns = boston.feature_names)
    
    # boston dataset의 target array는 주택 가격임. 이를 PRICE 컬럼으로 DataFrame에 추가함. 
    bostonDF['PRICE'] = boston.target
    
    y_target = bostonDF['PRICE']
    X_data = bostonDF.drop(['PRICE'],axis=1,inplace=False)
    
    ridge = Ridge(alpha = 10)
    neg_mse_scores = cross_val_score(ridge, X_data, y_target, scoring="neg_mean_squared_error", cv = 5)
    rmse_scores  = np.sqrt(-1 * neg_mse_scores)
    avg_rmse = np.mean(rmse_scores)
    print(' 5 folds 의 개별 Negative MSE scores: ', np.round(neg_mse_scores, 3))
    print(' 5 folds 의 개별 RMSE scores : ', np.round(rmse_scores,3))
    print(' 5 folds 의 평균 RMSE : {0:.3f} '.format(avg_rmse))
    ```
    
    <aside>
    ▶️  5 folds 의 개별 Negative MSE scores:  [-11.422 -24.294 -28.144 -74.599 -28.517]
     5 folds 의 개별 RMSE scores :  [3.38  4.929 5.305 8.637 5.34 ]
     5 folds 의 평균 RMSE : 5.518
    
    </aside>
    
    - alpha값을 0 , 0.1 , 1 , 10 , 100 으로 변경하면서 RMSE 측정
    
    ```python
    # 릿지에 사용될 alpha 파라미터의 값을 정의
    alphas = [0, 0.1, 1, 10, 100]
    
    # alphas list 값을 반복하면서 alpha에 따른 평균 rmse를 구함.
    for alpha in alphas :
        ridge = Ridge(alpha = alpha)
        
        # cross_val_score를 이용해 5 폴드의 평균 RMSE를 계산
        neg_mse_scores = cross_val_score(ridge, X_data, y_target, scoring="neg_mean_squared_error", cv = 5)
        avg_rmse = np.mean(np.sqrt(-1 * neg_mse_scores))
        print('alpha {0} 일 때 5 folds 의 평균 RMSE : {1:.3f} '.format(alpha, avg_rmse))
    ```
    
    <aside>
    ▶️ alpha 0 일 때 5 folds 의 평균 RMSE : 5.829
    alpha 0.1 일 때 5 folds 의 평균 RMSE : 5.788
    alpha 1 일 때 5 folds 의 평균 RMSE : 5.653
    alpha 10 일 때 5 folds 의 평균 RMSE : 5.518
    alpha 100 일 때 5 folds 의 평균 RMSE : 5.330
    
    </aside>
    
    - alpha 100 일 때 가장 좋다.
    
    - 각 alpha에 따른 회귀 계수 값을 시각화. 각 alpha값 별로 plt.subplots로 맷플롯립 축 생성
    
    ```python
    # 각 alpha에 따른 회귀 계수 값을 시각화하기 위해 5개의 열로 된 맷플롯립 축 생성  
    fig , axs = plt.subplots(figsize=(18,6) , nrows=1 , ncols=5)
    # 각 alpha에 따른 회귀 계수 값을 데이터로 저장하기 위한 DataFrame 생성  
    coeff_df = pd.DataFrame()
    
    # alphas 리스트 값을 차례로 입력해 회귀 계수 값 시각화 및 데이터 저장. pos는 axis의 위치 지정
    for pos , alpha in enumerate(alphas) :
        ridge = Ridge(alpha = alpha)
        ridge.fit(X_data , y_target)
        # alpha에 따른 피처별 회귀 계수를 Series로 변환하고 이를 DataFrame의 컬럼으로 추가.  
        coeff = pd.Series(data=ridge.coef_ , index=X_data.columns )
        colname='alpha:'+str(alpha)
        coeff_df[colname] = coeff
        # 막대 그래프로 각 alpha 값에서의 회귀 계수를 시각화. 회귀 계수값이 높은 순으로 표현
        coeff = coeff.sort_values(ascending=False)
        axs[pos].set_title(colname)
        axs[pos].set_xlim(-3,6)
        sns.barplot(x=coeff.values , y=coeff.index, ax=axs[pos])
    
    # for 문 바깥에서 맷플롯립의 show 호출 및 alpha에 따른 피처별 회귀 계수를 DataFrame으로 표시
    plt.show()
    ```
    
    <aside>
    ▶️
    
    ![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%2043.png)
    
    </aside>
    
    - alpha 값을 증가시킬수록 회귀 계수 값은 지속적으로 작아짐
    - 특히 NOX 피처의 경우 alpha 값을 계속 증가시킴에 따라 회귀 계수가 크게 작아지고 있다.
    
    - alpha 값에 따른 컬럼별 회귀계수 출력
    
    ```python
    ridge_alphas = [0 , 0.1 , 1 , 10 , 100]
    sort_column = 'alpha:'+str(ridge_alphas[0])
    coeff_df.sort_values(by=sort_column, ascending=False)
    ```
    
    <aside>
    ▶️
    
    ![Untitled](Machine%20Learning%201bf9420c06824cc1bdabb2497ca8765d/Untitled%2044.png)
    
    </aside>
    
    - alpha 값이 증가하면서 회귀 계수가 지속적으로 작아지고 있다.
    - 하지만 릿지 회귀의 경우 회귀 계수를 0으로 만들지는 않는다.

# 회귀 평가 지표

## MAE

- Mean Absolute Error
- 실제 값과 예측값의 차이를 절댓값으로 변환해 평균

## MSE

- Mean Squared Error
- 실제 값과 예측값의 차이를 제곱해 평균

## RMSE

- MSE 값은 오류의 제곱을 구하므로 실제 오류 평균보다 더 커지는 특성이 있으므로 MSE에 루트를 씌운 것이 RMSE

## R²

- 분산 기반으로 예측 성능 평가
- 실제 값의 분산 대비 예측값의 분산 비율
- 1에 가까울수록 예측 정확도가 높다.