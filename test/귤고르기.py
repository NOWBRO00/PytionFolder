k = 6
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]

def solution(k, tangerine):
    tang = list(set(tangerine))  
    temp = []  
    result = 0  
    answer = 0
    
    for i in tang:
        cnt = tangerine.count(i)
        temp.append(cnt)
        
    temp.sort(reverse=True)
    
    for i in temp:
        result += i
        answer += 1 
        if result >= k:
            return answer
        
    return answer

print(solution(k, tangerine))
