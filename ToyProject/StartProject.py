#=============== import 시작 =================
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.font_manager as fm
import ToyPtoject1
#=============== import 끝 =================

#================= csv 데이터 -> 배열 변환 시작 ===================
################### 검색량 csv 파일 주소 ##################
#월별 폴더 주소
file_path = "csvFile/07/"
koreanPancakeCSVArr07 = [file_path+"2021_부침개_네이버_일간검색트렌드.csv",file_path+"2022_부침개_네이버_일간검색트렌드.csv"
    ,file_path+"2023_부침개_네이버_일간검색트렌드.csv",file_path+"2024_부침개_네이버_일간검색트렌드.csv"]

#월별 폴더 주소
file_path = "csvFile/09/"
koreanPancakeCSVArr09 = [file_path+"2021_부침개_네이버_일간검색트렌드.csv",file_path+"2022_부침개_네이버_일간검색트렌드.csv"
    ,file_path+"2023_부침개_네이버_일간검색트렌드.csv",file_path+"2024_부침개_네이버_일간검색트렌드.csv"]


################### 기상청 csv 파일 주소 ###################
file_path_rain07 = file_path+"기상청_강수량.csv"
file_path_rain09 = file_path+"기상청_강수량.csv"

################### 기상청 dataFrame 데이터 생성 ###################
weatherArr07 = pd.DataFrame(pd.read_csv(file_path_rain07,encoding="cp949"))
weatherArr09 = pd.DataFrame(pd.read_csv(file_path_rain09,encoding="cp949"))
#================= csv 데이터 -> 배열 변환 끝 ===================

#================= 날짜 배열 생성 시작 =================
yearDate = [2021,2022,2023,2024]
#================= 날짜 배열 생성 끝 ===================

ToyPtoject1.plotKoreanPancake(koreanPancakeCSVArr07,weatherArr07,yearDate)
ToyPtoject1.plotKoreanPancake(koreanPancakeCSVArr09,weatherArr09,yearDate)

# 그래프 출력
plt.show()