# Today I Learned



- mean() == 평균값 구하기, string은 안됨
- inplace=True == 연결된 데이터프레임이 바뀜 False의 경우 새로운 객체에 할당해야 함
- fillna(x) == 결측값을 x로 바꿈
- df['열'].value_counts() == 데이터프레임의 열의 값별로 세기, 내림차순
- count() == 문자열의 개수를 세는 함수
- min_samples_split=2 == 분할할 수 있는 샘플 수 지정, 샘플이 2개 이상일 경우에 분할
- min_samples_leaf=2 == 분할해서 leaf가 될 수 있는 샘플 수를 지정, 다음에 생성될 노드들의 샘플 수가 모두 2이상이어야 분할
- max depth=3 == 뿌리 마디 이후 자식마디부터 끝마디까지의 깊이가 3일때까지만 분할
- .best_params_ == 최적의 파라미터
- .best_score_ == 최고의 점수
- .best_estimator_ == 최적의 파라미터로 모델 생성