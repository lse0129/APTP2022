# APTP 2022 - **{팀명}**
###### Asterisk Python Team Project 2022
구성원: 아스터 | 리스크 | 홍길동 | Change

## 1. 주제
x,y 좌표 평면에서 특정 조건과 함수 식이 주어지면, 해당 조건에 따라 그래프를 시각화하는 프로그램

## 2. 동기
대부분의 미적분학 문제는 그래프의 개형을 그리는 것에서 시작한다. 한마디로 미적분학 문제를 풀때, 함수를 좌표 평면에 나타낼 수 있다면 더욱 쉽게 문제에 접근할 수 있다. 따라서 본 프로젝트에서는 미적분학 문제와 더불어 그래프의 시각화가 필요한 각종 수학 문제를 풀이하는데 사용가능한 그래프 시각화 프로그램을 제작하고자 한다.

물론 울프럼 알파, 지오지브라 등 그래프를 시각화해주는 프로그램이 기존에 존재하긴 하나, 본 프로젝트에서는 그래프 시각화와 동시에 그래프 아래 면적 넓이 계산, 접선의 방정식 표시 등 다른 시각화 요소를 추가해서 수학 문제 풀이에 최적화된 그래프 시각화 프로그램을 설계하고자 한다. 


## 3. 프로그램 사용 대상
미적분학 문제 등 그래프의 시각화가 필요한 수학 문제를 풀어야 하는 사람

## 4. 목적
단순히 그래프를 그리는 것뿐만 아니라 여러 시각화 요소를 추가하여 수학 문제 풀이에 최적화된 그래프 시각화 프로그램을 설계하고자 한다.

## 5. 주요기능
1. 그래프 시각화 기능
→ 함수 식이 주어지면 이를 x,y 좌표평면에 그려주는 기능으로 tkinder모듈을 사용하여 구현하고자 한다.

2. 미분/적분 기능
→ 함수 식이 주어지면 이를 미분 또는 적분을 진행하는 기능으로 심볼릭 연산(symbolic operation)으로 계산을 진행하기 위해 sympy 모듈의 자동 미분/적분 기능을 사용하여 구현하고자 한다.

3. 미분/적분 활용 기능
→ 접선의 방정식 구하기, 그래프 면적 구하기 등 미분, 적분 결과값을 활용하는 기능으로, 마찬가지로 시각화를 진행하고자 한다.

## 6. 프로젝트 핵심
1. 기존의 그래프 시각화 프로그램과 어떤 차별점을 둘 것인가
→ 기존에 존재하는 그래프 시가고하 프로그램과 차별점을 두기 위해 미적분학을 통해 구현할 수 있는 기능 이외에도 다른 기능을 추가할 예정

2. 그래프 시각화의 이점을 최대로 활용할 수 있는 분야는 무엇이 있을까
→ 주로 미적분학에 초점을 맞추고 있는데, 이를 활용할 수 있는 다른 분야에 대해서도 추가할 예정

## 7. 구현에 필요한 라이브러리나 기술
GUI 구현 → tkinder 모듈

수식 연산 → sympy 모듈

## 8. **분업 계획**
그래프 시각화 구현/미적분 활용 기능 구현/미적분 이외 기능 구현

## 9. 기타
추가할 기능 찾아보다가 너무 생각이 안나면 다른 주제로 바꿀 수도 있습니다

<hr>

#### readme 작성관련 참고하기 [바로가기](https://heropy.blog/2017/09/30/markdown/)



