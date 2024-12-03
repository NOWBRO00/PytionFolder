import matplotlib.pyplot as plt
import pandas as pd

# 파일 경로 설정
file_path_rain = "C:/Users/wogud/OneDrive/바탕 화면/토이 프로젝트/기상청_강수량.csv"

# CSV 파일 읽기
search_rain = pd.read_csv(file_path_rain, encoding='ISO-8859-1')

# 'period' 컬럼을 날짜 형식으로 변환
search_rain['period'] = pd.to_datetime(search_rain['period'])

# 막대그래프 그리기
plt.figure(figsize=(10, 6))  # 그래프 크기 설정
plt.bar(search_rain['period'], search_rain['rain'], color='blue', alpha=0.7)  # 막대그래프

# 그래프 제목 및 레이블 설정
plt.title('Rainfall Over Time', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Rainfall (mm)', fontsize=12)

# 날짜가 겹치지 않게 x축 레이블 회전
plt.xticks(rotation=45)

# 그래프 출력
plt.tight_layout()  # 레이아웃 조정
plt.show()
