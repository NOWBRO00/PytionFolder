## 예시 데이터
array=[1,1,2,3,3,3,4,5]
n=3

## 결과 변수 선언
answer = 0

## 반복을 통해 요소비교
for val in array :
    ## 요소와 n이 같은경우 +1
    if(val==n):
        answer=answer+1
print(answer)

''' 코테용 제출용 코드
def solution(array, n):
    answer=0
    for val in array :
        if(val==n):
            print('if 시작')
            answer=answer+1
    return answer
    실습용
'''