from collections import Counter

def solution(k, tangerine):
    # 귤크기 : 개수
    # 딕셔너리 객체 생성
    dic = Counter(tangerine)
    
    # 개수를 기준으로 내림차순 정렬
    # sorted() 사용 이유는 원본 보존하기 위함
    li = sorted(dic.values(), reverse=True)
    
    total = 0  # 선택한 귤 개수 총합
    kinds = 0  # 선택한 귤 종류 수
    
    for v in li:
        total += v
        kinds += 1
        if total >= k:  # 필요한 만큼의 귤을 선택한 경우 종료
            break
    
    return kinds