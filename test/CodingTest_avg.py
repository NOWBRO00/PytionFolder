## 예시데이터
numbers=[1,2,3,4,5,6,7,8,9,10,11]

## 결과 변수 선언
answer=0

## 총합 변수 선언
sum=0

## 0번부터 차례대로 값을 더하기
for val in numbers:
    sum += val
## 총합/전체수 = 총합/전체길이
answer=sum/len(numbers)

## 결과 출력
print(answer)

'''코테 제출용 코드
def solution(numbers):
    answer = 0
    sum=0
    for val in numbers:
        sum += val
    answer=sum/len(numbers)
    return answer
    실습용
'''