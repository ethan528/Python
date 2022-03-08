# Coding



- mean() == 평균값 구하기, string은 안됨

- inplace=True == 연결된 데이터프레임이 바뀜 False의 경우 새로운 객체에 할당해야 함

- fillna(x) == 결측값을 x로 바꿈

- df['column'].value_counts() == 데이터프레임의 열의 값별로 세기, 내림차순, 특정 컬럼 내용을 구성하는 값과 각 값의 빈도를 보여줌

- count() == 문자열의 개수를 세는 함수

- min_samples_split=2 == 분할할 수 있는 샘플 수 지정, 샘플이 2개 이상일 경우에 분할

- min_samples_leaf=2 == 분할해서 leaf가 될 수 있는 샘플 수를 지정, 다음에 생성될 노드들의 샘플 수가 모두 2이상이어야 분할

- max depth=3 == 뿌리 마디 이후 자식마디부터 끝마디까지의 깊이가 3일때까지만 분할

- .best_params_ == 최적의 파라미터

- .best_score_ == 최고의 점수

- .best_estimator_ == 최적의 파라미터로 모델 생성

- cumcount() == 몇번째 중복된 데이터인지 확인하기, cumcount가 0인 경우 중복되지 않음

- pd.merge() == 데이터프레임, left_on='', right_on='', how=''가 괄호안에 들어감, 두 데이터프레임을 합쳐줌

- how='inner' == 교집합

- how='outer' == 합집합

- how='left' == 중복의 경우 왼쪽 데이터프레임의 데이터로 적용

- how='right' == 중복의 경우 오른쪽 데이터프레임의 데이터로 적용

- sep='' == 문자간 구분자를 정의하거나 지정

- header=None == 열 이름으로 사용할 행 번호 및 데이터 시작, 입력하지 않으면 header=0과 동일, 이 때 0은 첫번째 줄이 아니라 첫번째 데이터 줄, header=None은 열 이름이 없다는 것, 행 위치를 지정하는 정수 목록일 수 있다.

- names= == 사용할 열 이름 목록

- groupby('column') == column을 기준으로 데이터프레임의 데이터를 그룹으로 바꿔줌

- info() == 데이터의 전반적인 정보 출력,  데이터프레임의 행과 열의 크기, 컬럼명, 컬럼을 구성하는 값의 자료형 등을 출력

- %matplotlib inline == 브라우저에서 바로 그림보기

- plt.pie() == 파이 차트를 그릴 함수

- plt.hist() == 히스토그램, 수치형 데이터의 분포 확인

- plt.boxplot() == 상자그림

- xticks() == x축의 표시하는 눈금 지정 함수

- plt.bar() == 막대그래프

- .loc[행 인덱싱, 열 인덱싱]='x' == 특정 위치의 값을 찾아 변경하고 싶을 때, 조건이나 이름을 넣어 특정 행을 찾을 때, 특정 값이 x로 변경됨

- .pivot_table() == 데이터를 원하는 기준으로 요약 정리

- .melt() == pivot에 의해 요악한 테이블을 요약 전으로 만듬

- .reset_index() == 행 인덱스 초기화, 기존의 인덱스는 첫번째 열로 자동 삽입, 괄호 안에 drop=True 옵션을 인자로 넣어줄 경우 기존 인덱스를 버리고 재배열

- .fit(x_train, y_train) == 주어진 학습 데이터로 학습

- .predict(x_test) == 해당 테스트 데이터로 예측

- filled = True == class별 노드에 color 채우기

- impurity=True == 불순도 표시

- np.sqrt() == 제곱근 출력

- scoring="neg_mean_squared_error" == mse의 negative 값을 반환

- df.corr() == 상관계수 출력

- sns.heatmap() == 히트맵 그리기

- annot=True == 각셀의 숫자 입력

- compile() == 모델을 학습시키기 위한 학습과정을 설정

- loss='' == 훈련과정에서 네트워크 예측이 실제 값에서 얼마나 멀리 떨어져 있는지 계산하기 위해 사용하는 방법 지정

- optimizer='' == 훈련과정 설정

- metrics=[''] == 모델의 성능을 판단할 때 사용하는 함수 지정

- loss='binary_crossentropy' == 클래스가 두 개인 이진 분류 문제에서 사용, label이 0 또는 1을 값으로 가질 때 사용, 모델의 마지막 레이어의 활성화 함수는 시그모이드 함수

- loss='categorical_crossentropy' == 클래스가 여러 개인 다중 분류 문제에서 사용, label이 원-핫 인코딩 된 형태 즉 label이 class를 나타내는 one-hot vector를 값으로 가질 때 사용, 모델의 마지막 레이어의 활성화 함수는 소프트맥스 함수

- model=Sequential() == 층을 차례대로 쌓은 모델 생성

- input_dim=1 == 입력 차원 및 입력노드가 1, x배열의 데이터의 개수랑 동일하게 지정, 맨 처음 입력층에서만 사용

- activation='' == 활성화함수 설정

- relu == 은닉 층으로 학습, 역전파를 통해 좋은 성능이 나오기 때문에 마지막 층이 아닌 경우 대부분 사용

- sigmond == 이진 분류 문제

- softmax == 확률 값을 이용해 다양한 클래스를 분류하기 위한 문제

- epchs=100 == 100번 훈련

- batch_size=10 == 작업단위, 100번 훈련할 때 전체 데이터를 10개로 나누어 훈련, 명시하지 않을 경우 디폴트값인 32로 진행

- model.evaluate() == 모델 평가

- LabelEncoder() == 문자형을 정수형으로 바꿔줌

- OneHotEncoder() == LabelEncoding 후에 숫자의 크고 작은 특성을 없애기 위해 사용

- pd.DataFrame() == 데이터프레임 만들기

- ' '.join() = 문자열을 가지고 있는 리스트를 문자열로 변환

- np.zeros() == 0으로 가득 찬 array 생성

- df.shape == 행과 열의 개수를 튜플로 반환

- df.dtypes == 열을 기준으로 데이터 형태 반환

- df.columns=[''] == 데이터프레이 열 이름 변경 

- dict.items() == 딕셔너리의 키와 값을 반환

- stats.levene() == pvalue가 0.05보다 크면 등분산

- stats.ttest_ind() == pvalue 가 e-05일 경우 0.05보다 작다고 볼 수 있다

- equal_var=True == 등분산일 경우 True로 설정

- stats.bartlett() == 모든 그룹의 분산이 같다는 가정하에 진행, pvalue가 0.05보다 크면 등분산

- stats.f_oneway() ==  pvalue가 유의수준보다 낮을 경우 귀무가설 기각, 기각의 경우 모든 그룹의 평균이 같지않다

- showfliers=False == Outlier를 표시하지 않음 

- hsd=pairwise_tukeyhsd() 

  hsd.summary(hsd) == 어떤 그룹의 평균이 같은지 검정 및 결과 요약, p-adj의 값이 0.05 보다 크면 reject의 값이 True, 아니면 False로 나옴

- crosstab=pd.crosstab()

  result=chi2_contingency(crosstab)

  print('Chis statistic:{},p-value:{}'.format(result[0],result[1])) == 두 범주형 데이터 사이의 관련성을 확인, p-value가 유의 수준보다 낮을 경우 연관성이 있다

- plt.scatter(df1, df2) == 산점도 그리기

- stats.pearsonr(df1, df2) == 상관계수와 p-value 반환

- .isalnum() == 문자열이 영어, 한글 혹은 숫자이면 True 아니면 False

- sorted(list, reverse = False) ==오름차순으로 정렬, reverse가 True일 경우 내림차순, False가 기본값

- .replace('old', 'new') == 문자열 내의 'old'를 'new'로 변환

- cv2.imread('./data/image.jpg', cv2.IMREAD_GRAYSCALE) == 이미지 로드, 흑백으로 로드

  - cv2.IMREAD_UNCHANGED == 원본 사용
  - cv2.IMREAD_GRAYSCALE == 1 채널, 그레이스케일 적용
  - cv2.IMREAD_COLOR == 3 채널, BGR 이미지 사용
  - cv2.IMREAD_ANYDEPTH == 이미지에 따라 정밀도를 16/32비트 또는 8비트로 사용
  - cv2.IMREAD_ANYCOLOR == 가능한 3 채널, 색상 이미지로 사용
  - cv2.IMREAD_REDUCED_GRAYSCALE_2 ==: 1 채널, 1/2 크기, 그레이스케일 적용
  - cv2.IMREAD_REDUCED_GRAYSCALE_4 == 1 채널, 1/4 크기, 그레이스케일 적용
  - cv2.IMREAD_REDUCED_GRAYSCALE_8 == 1 채널, 1/8 크기, 그레이스케일 적용
  - cv2.IMREAD_REDUCED_COLOR_2 == 3 채널, 1/2 크기, BGR 이미지 사용
  - cv2.IMREAD_REDUCED_COLOR_4 == 3 채널, 1/4 크기, BGR 이미지 사용
  - cv2.IMREAD_REDUCED_COLOR_8 == 3 채널, 1/8 크기, BGR 이미지 사용

- cv2.imwrite('./data/image.jpg', image) == 이미지 저장

- cv2.imshow('이미지', image) == 이미지 표시

- cv2.waitKey() == 키 입력 대기, 사용하지 않을 경우 윈도우 창이 유지되지 않고 종료됨

- cv2.destroyAllWindows() == 모든 윈도우 창 제거, 키 입력 이후 사용

- cv2.VideoCapture('./data/video.mp4') == 동영상 파일 로드

- capture.isOpened() == 동영상 파일 열기 성공 여부 확인

- capture.open(filename) == 동영상 파일 열기

- capture.set(propid, value) == 동영상 속성 설정

- capture.get(propid) == 동영상 속성 반환

- capture.release() == 동영상 파일을 닫고 메모리 해제

- cv2.CAP_PROP_FRAME_WIDTH == 프레임의 너비

- cv2.CAP_PROP_FRAME_HEIGHT == 프레임의 높이

- cv2.CAP_PROP_FRAME_COUNT == 총 프레임 수

- cv2.CAP_PROP_FPS == 프레임 속도

- cv2.CAP_PROP_FOURCC == 코덱 코드

- df.drop() == 열이나 행 지우기

- aixs=0 == 행을 따라 동작

- aixs=1 == 열을 따라 동작

- df.isnull() == 결측값이 있을 경우 True로 나타냄

- verbose=1 == 0 아무런 표시를 하지 않음,  1 에포크별 진행 사항을 알려줌,  2 에포크별 학습 결과를 알려줌

- cmap='gray' == 색상 설정

- Flatten() == 2차원 데이터를 1차원 데이터로 바꾸는 역할

- input_shape=( 행, 열, 채널 수 ) == 샘플 수를 제외한 입력 형태를 정의

- to_categorical() == 정수 인코딩된 결과를 입력으로 받아 원-핫 인코딩 과정을 수행

- .history[''] == fit 함수의 반환 값

  - 매 에포크 마다의 훈련 손실값 (loss)
  - 매 에포크 마다의 훈련 정확도 (acc)
  - 매 에포크 마다의 검증 손실값 (val_loss)
  - 매 에포크 마다의 검증 정확도 (val_acc)

- np.expand_dims() ==

- np.argmax() == 

- np.squeeze() == 

- 
