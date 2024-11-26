import math

N=3
words=["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]

def solution(n, words):
    cnt = 1
    n = -1
    sit=0
    stack=[]
    ## 조건시작
    ## 순서대로 진행
    for i in range(0,len(words)):
        ## 중복 체크용 스택배열
        stack.append(words[i])
        ## 중복체크
        if stack.count(words[i])>1: 
            print("중복체크")
            cnt=math.ceil(cnt/N)
            answer = [sit+1,cnt]
            return answer
        
        ## 순서 세팅
        if(i%N==0 and i>=N):
            n=n+N
        sit = i-n
        print("틀릴예정인 사람의 번호 :"+str(sit))

        ## 실패조건
        ## 끝말잇기 실패
        if i < len(words) - 1 and words[i].strip()[-1] != words[i+1].strip()[0]:
            print("끝말잇기 실패")
            cnt=math.ceil(cnt/N)
            answer = [sit+1,cnt]
            return answer

        ## 한글자인 단어
        if len(words[i])==1:
            print("한글자인 단어")
            cnt=math.ceil(cnt/N)
            answer = [sit+1,cnt]
            return answer
        cnt=cnt+1
    ## 맞춘개수 구하기
    answer = [0,0]
    print(cnt)
    return answer

print(solution(N,words))
