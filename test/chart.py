# [데이터 시각화]

import csv
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

file_path = "test.csv"

date = np.dates = []
wt = np.winter_temps = []
st = np.summer_temps = []
avgt = np.avg_temps = []

with open(file_path,mode='r') as file :
    reader = csv.reader(file)

    header = next(reader)

    i=0
    for row in reader :
        a = row[-4]
        b = row[-2]
        c = row[5]
        
        date.append(a)

        print(a, b)
        np.winter_temps.append(float(b))
        
        print(a, c)
        np.summer_temps.append(float(c))

        d = (np.summer_temps[i]-np.winter_temps[i])/2
        print(a, d)
        np.avg_temps.append(float(d))
        
        i= i+1
        if i==50:
            break
plt.plot(date,wt,marker='o',color='b',markersize=5)
plt.plot(date,st,marker='o',color='r',markersize=5)
plt.plot(date,avgt,marker='o',color='g',markersize=5)


plt.title("Temperature in December", fontsize=15)

plt.xlabel("Date", fontsize=10)
plt.ylabel("Temperature", fontsize=10)

plt.show()







            
