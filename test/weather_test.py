## 3번째 일시
## 4번째 평균기온
'''
from csv import reader

file_path = "test.csv"

with open(file_path,mode='r',encoding= "UTF-8")as file :
    reader = reader(file)
'''
from csv import reader

file_path = "test.csv"

with open(file_path,mode='r') as file :
    reader = reader(file) # 자바에서는 패키지, 파이썬에서는 모듈

    # 첫줄을 읽어버리고
    header = next(reader)

    # 시작해~~
    for row in reader :
        a= row[2] ## 12월인 데이터만 출력하고 싶어~~
        b= row[-2]
        if a.startswith("Dec"):
            print(a,b)








