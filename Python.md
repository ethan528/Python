# Python

## 변수의 이해

변수의 값이 저장되는 공간을 메모리, 변수의 저장 위치를 메모리 주소라고 한다

변수에 들어가는 값은 반드시 어떤 특정 메모리 주소에 할당

변수를 선언하여 값을 저장할 때 운영체제 os 와 파이썬 인터프리터가 서로 협력하여 선언한 변수를 메모리 공간 어딘가에 저장하면서 메모리 주소를 공유

## 자료형과 기본 연산

### 기본 자료형
- 정수형 = 자연수를 포함해 값의 영역이 정수로 한정된 값
- 실수형 = 소수점이 포함된 값, 실제 값이 정수형이라도 9.0으로 입력하면 인터프리터는 실수형으로 해석
- 문자형 = 값이 문자로 출력되는 자료형, 따옴표에 들어간 정보를 문자형 데이터라고 함
- 불린형 = 논리형이라고도 하며, 참 또는 거짓을 표현할 때 사용, True=참=1, false=거짓=0

### 간단한 연산
- 더히기 = +
- 빼기 = -
- 곱하기 = *
- 나누기 = /
- 제곱승 = **
- 몫 = //
- 나머지 = %
- 증가 연산 = a += 1(a = a + 1)
- 감소 연산 = a -= 1(a = a - 1)

## 자료형 변환

### 정수형과 실수형 간 변환
- float(), 실수형으로 나누기
- int(), 소수점 이하의 내림 발생

### 숫자형과 문자형 간 변환
- str(), 문자형 간 덧셈은 단순 붙이기

### 자료형 확인하기
- type()

## 화면 입출력

입력 = input()

출력 = print()

## lab: 화씨온도 변환기

```python 
print("본 프로그램은 섭씨온도를 화씨온도로 변환하는 프로그램입니다.")
pirnt("변환하고 싶은 서비씨온도를 입력하세요.")

celsius = input()
fahrenheit = (float(clesius) * 1.8) + 32

print("섭씨온도:", celsius)
print("화씨온도:", fahrenheit)
```

## 리스트의 이해

리스트는 하나의 변수에 여러 값을 할당하는 자료형 = 시퀀스 자료형(여러자료를 순서대로 넣는다는 뜻)

### 인덱싱
- 리스트에 있는 값에 접근하기 위해, 이 값의 상대적인 주소를 사용하는 것
- 첫 번째 값을 0으로 했을 때 이와 얼마나 덜어져 있는지를 표현한 값, 일반적으로 인덱스 주소 또는 인덱스 값이라고 함
```python
colors = ['red', 'blue', 'green']
print(colors[0]) # red
print(colors[1]) # green
print(len(colors)) # 3
```

### 슬라이싱
- 리스트의 인덱스를 사용하여 전체 리스트에서 일부를 잘라내여 반환
```python
cities = ['서울', '부산', '인천', '대구', '대전', '광주', '울산', '수원']
print(cities[0:6]) # ['서울', '부산', '인천', '대구', '대전', '광주']

print(cities[-8:0]) # ['서울', '부산', '인천', '대구', '대전', '광주', '울산', '수원']
print(cities[-50:50])
# 범위를 넘어갈 경우 자동으로 최대 범위를 지정
#['서울', '부산', '인천', '대구', '대전', '광주', '울산', '수원']

print(cities[::2])
# 2칸 단위로
# ['서울', '인천', '대전', '울산']
print(cities[::-1])
# 역으로 슬라이싱
# ['수원', '울산', '광주', '대전', '대군', '인천', '부산', '서울']

color1 = ['red', 'blue', 'green']
color2 = ['orange', 'black', 'white']
print(color1 + color2) # ['red', 'blue', 'green', 'orange', 'black', 'white']
print(color1 * 2) # ['red', 'blue', 'green', 'red', 'blue', 'green']
print('blue' in color2) # False

color = ['red', 'blue', 'green']
color.append('white')
print(color) # ['red', 'blue', 'green', 'white']

color = ['red', 'blue', 'green']
color.extend(['black', 'purple']) # 리스트에 새로운 리스트 추가
print(color) # ['red', 'blue', 'green', 'black' 'purple']

color = ['red', 'blue', 'green']
color.insert(0, 'orange')
print(color) # ['orange', 'red, 'blue', 'green']

color = ['orange', 'red', 'blue', 'green']
color.remove('red')
print(color) # ['orange', 'blue', 'green']

color = ['red', 'blue', 'green']
color[0] = 'orange'
print(color) # ['orange', 'blue', 'green']
del color[0]
print(color) # ['blue', 'green']
```

### 패킹과 언패킹
- 시퀀스 자료형에서 일반적으로 사용할 수 있는 방법
```python
t = [1, 2, 3]
a, b, c = t
print(t, a, b, c) # [1, 2, 3] 1 2 3
```

### 이차원 리스트
- 행렬과 같은 개념
```python
kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]
print(midterm_score) # [[49, 79, 20, 100, 80], [43, 59, 85, 30, 90], [49, 79, 48, 60, 100]]
print(midterm_score[0][2]) # 20
```