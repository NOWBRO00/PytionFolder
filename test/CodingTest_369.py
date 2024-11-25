## 프로젝트 소개
print('369게임을 진행하는 프로그램입니다.')

## 클라이언트 값 입력
order=input('숫자를 입력해주세요 : ')

## 결과 변수 선언
result=0

## 369가 들어있는지 확인
result += (str(order).count('3'))
result += (str(order).count('6'))
result += (str(order).count('9'))


## 결과출력
print("3,6,9의 개수 : "+str(result))

''' 코테용 제출용 코드
def solution(order):
    answer = 0
    answer = (str(order).count('3'))+ (str(order).count('6'))+(str(order).count('9'))
    return answer
    실습용
    
'''






