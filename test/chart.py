import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime

# 파일 경로 설정
file_path_2021 = "C:/Users/wogud/OneDrive/바탕 화면/토이 프로젝트/2021_부침개_네이버_일간검색트렌드.csv"
file_path_2022 = "C:/Users/wogud/OneDrive/바탕 화면/토이 프로젝트/2022_부침개_네이버_일간검색트렌드.csv"
file_path_2023 = "C:/Users/wogud/OneDrive/바탕 화면/토이 프로젝트/2023_부침개_네이버_일간검색트렌드.csv"
file_path_2024 = "C:/Users/wogud/OneDrive/바탕 화면/토이 프로젝트/2024_부침개_네이버_일간검색트렌드.csv"
file_path_rain = "C:/Users/wogud/OneDrive/바탕 화면/토이 프로젝트/기상청_강수량.csv"

# CSV 파일 읽기
search_2021 = pd.read_csv(file_path_2021)
search_2022 = pd.read_csv(file_path_2022)
search_2023 = pd.read_csv(file_path_2023)
search_2024 = pd.read_csv(file_path_2024)
search_rain = pd.read_csv(file_path_rain, encoding='ISO-8859-1')

# 'period' 컬럼을 날짜 형식으로 변환
search_2021['period'] = pd.to_datetime(search_2021['period'])
search_2022['period'] = pd.to_datetime(search_2022['period'])
search_2023['period'] = pd.to_datetime(search_2023['period'])
search_2024['period'] = pd.to_datetime(search_2024['period'])
search_rain['period'] = pd.to_datetime(search_rain['period'])

# 그래프 출력
plt.figure(figsize=(15, 10))

# 첫 번째 서브플롯: 2021년 검색량과 강수량을 함께 표시
plt.subplot(2, 2, 1)
plt.plot(search_2021['period'], search_2021['searchVolume'], marker='o', linestyle='-', color='b', label='2021 Search Volume')
plt.xlabel('Date')
plt.ylabel('Search Volume')
plt.legend(loc='upper left')

# 두 번째 서브플롯: 2022년 검색량 표시
plt.subplot(2, 2, 2)
plt.plot(search_2022['period'], search_2022['searchVolume'], marker='o', linestyle='-', color='r', label='2022 Search Volume')
plt.xlabel('Date')
plt.ylabel('Search Volume')
plt.legend(loc='upper left')

# 세 번째 서브플롯: 2023년 검색량 표시
plt.subplot(2, 2, 3)
plt.plot(search_2023['period'], search_2023['searchVolume'], marker='o', linestyle='-', color='y', label='2023 Search Volume')
plt.xlabel('Date')
plt.ylabel('Search Volume')
plt.legend(loc='upper left')

# 네 번째 서브플롯: 2024년 검색량 표시
plt.subplot(2, 2, 4)
plt.plot(search_2024['period'], search_2024['searchVolume'], marker='o', linestyle='-', color='g', label='2024 Search Volume')
plt.xlabel('Date')
plt.ylabel('Search Volume')
plt.legend(loc='upper left')

# 전체 제목 설정
plt.suptitle("Search Volume and Rainfall Trends (2021-2024)", fontsize=15)
plt.tight_layout()
plt.show()

