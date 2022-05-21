<class 'pandas.core.frame.DataFrame'>
RangeIndex: 275960 entries, 0 to 275959
Data columns (total 3 columns):
 #   Column    Non-Null Count   Dtype 
---  ------    --------------   ----- 
 0   index     275960 non-null  int64 
 1   comments  275960 non-null  object # 전처리 후 데이터(특수문자제거, 이모지 제거 등), 빈 행 제거
 2   likes     275960 non-null  int64  
dtypes: int64(2), object(1)
memory usage: 6.3+ MB

# konlpy, hannanum, okt, komoran, kkma, re를 활용하여 텍스트 전처리
#