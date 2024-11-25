def test(N,tower):
    result=[0]*N
    stack=[]

    for i in range(N):
        while stack and stack[-1][0] < tower[i]:
            stack.pop()

        if stack :
            result[i]=stack[-1][1]+1
        else :
            result[i]=0

        stack.append([tower[i],i])

    return result



N=5
tower=[6,9,5,7,4]
result=test(N,tower)
print(result)
'''코딩 테스트 타워 실습용'''
