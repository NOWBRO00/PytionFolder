import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates

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

# 2x2 형태로 서브플롯 생성
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

# 첫 번째 그래프: 2021년 검색량과 강수량을 함께 표시
ax1 = axs[0, 0]
ax1.plot(search_2021['period'], search_2021['searchVolume'], color='b', label='2021 Search Volume', marker='o', linestyle='-', alpha=0.7)
ax1.set_xlabel('Date')
ax1.set_ylabel('Search Volume', color='b')
ax1.tick_params(axis='y', labelcolor='b')
ax1.legend(loc='upper left')

# x축 레이블을 "일"만 표시 (1일, 2일, 3일 ...)
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d'))
# x축에 모든 날짜 (1일부터 30일까지) 표시하도록 간격 설정
ax1.xaxis.set_major_locator(mdates.DayLocator(bymonthday=range(1, 31))) 

# 강수량 막대그래프
ax2 = ax1.twinx()  # y축을 공유하는 또 다른 축 생성
year_2021_rain = search_rain[search_rain['period'].dt.year == 2021]
ax2.bar(year_2021_rain['period'], year_2021_rain['rain'], color='blue', alpha=0.3, label='2021 Rainfall')
ax2.set_ylabel('Rainfall (mm)', color='blue')
ax2.tick_params(axis='y', labelcolor='blue')
ax1.set_title('2021 Search Volume and Rainfall')
ax2.legend(loc='upper left')

# 두 번째 그래프: 2022년 검색량과 강수량을 함께 표시
ax3 = axs[0, 1]
ax3.plot(search_2022['period'], search_2022['searchVolume'], color='r', label='2022 Search Volume', marker='o', linestyle='-', alpha=0.7)
ax3.set_xlabel('Date')
ax3.set_ylabel('Search Volume', color='r')
ax3.tick_params(axis='y', labelcolor='r')
ax3.legend(loc='upper left')

# x축 레이블을 "일"만 표시 (1일, 2일, 3일 ...)
ax3.xaxis.set_major_formatter(mdates.DateFormatter('%d'))
# x축에 모든 날짜 (1일부터 30일까지) 표시하도록 간격 설정
ax3.xaxis.set_major_locator(mdates.DayLocator(bymonthday=range(1, 31))) 

# 강수량 막대그래프
ax4 = ax3.twinx()  # y축을 공유하는 또 다른 축 생성
year_2022_rain = search_rain[search_rain['period'].dt.year == 2022]
ax4.bar(year_2022_rain['period'], year_2022_rain['rain'], color='red', alpha=0.3, label='2022 Rainfall')
ax4.set_ylabel('Rainfall (mm)', color='red')
ax4.tick_params(axis='y', labelcolor='red')
ax3.set_title('2022 Search Volume and Rainfall')

# 세 번째 그래프: 2023년 검색량과 강수량을 함께 표시
ax5 = axs[1, 0]
ax5.plot(search_2023['period'], search_2023['searchVolume'], color='y', label='2023 Search Volume', marker='o', linestyle='-', alpha=0.7)
ax5.set_xlabel('Date')
ax5.set_ylabel('Search Volume', color='y')
ax5.tick_params(axis='y', labelcolor='y')
ax5.legend(loc='upper left')

# x축 레이블을 "일"만 표시 (1일, 2일, 3일 ...)
ax5.xaxis.set_major_formatter(mdates.DateFormatter('%d'))
# x축에 모든 날짜 (1일부터 30일까지) 표시하도록 간격 설정
ax5.xaxis.set_major_locator(mdates.DayLocator(bymonthday=range(1, 31))) 

# 강수량 막대그래프
ax6 = ax5.twinx()  # y축을 공유하는 또 다른 축 생성
year_2023_rain = search_rain[search_rain['period'].dt.year == 2023]
ax6.bar(year_2023_rain['period'], year_2023_rain['rain'], color='yellow', alpha=0.3, label='2023 Rainfall')
ax6.set_ylabel('Rainfall (mm)', color='yellow')
ax6.tick_params(axis='y', labelcolor='yellow')
ax5.set_title('2023 Search Volume and Rainfall')

# 네 번째 그래프: 2024년 검색량과 강수량을 함께 표시
ax7 = axs[1, 1]
ax7.plot(search_2024['period'], search_2024['searchVolume'], color='g', label='2024 Search Volume', marker='o', linestyle='-', alpha=0.7)
ax7.set_xlabel('Date')
ax7.set_ylabel('Search Volume', color='g')
ax7.tick_params(axis='y', labelcolor='g')
ax7.legend(loc='upper left')

# x축 레이블을 "일"만 표시 (1일, 2일, 3일 ...)
ax7.xaxis.set_major_formatter(mdates.DateFormatter('%d'))
# x축에 모든 날짜 (1일부터 30일까지) 표시하도록 간격 설정
ax7.xaxis.set_major_locator(mdates.DayLocator(bymonthday=range(1, 31))) 

# 강수량 막대그래프
ax8 = ax7.twinx()  # y축을 공유하는 또 다른 축 생성
year_2024_rain = search_rain[search_rain['period'].dt.year == 2024]
ax8.bar(year_2024_rain['period'], year_2024_rain['rain'], color='green', alpha=0.3, label='2024 Rainfall')
ax8.set_ylabel('Rainfall (mm)', color='green')
ax8.tick_params(axis='y', labelcolor='green')
ax7.set_title('2024 Search Volume and Rainfall')

# 전체 제목 설정
plt.suptitle("Search Volume and Rainfall Trends (2021-2024)", fontsize=16)
plt.tight_layout()
plt.subplots_adjust(top=0.9)  # 제목과 서브플롯 간격 조정

# 그래프 출력
plt.show()
