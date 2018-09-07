# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 9:29
# @Author  : Lsp

import pandas as pd
import matplotlib.dates as mdates
from dateutil import parser
import matplotlib.pyplot as plt
from matplotlib import legend

df_ferrara = pd.read_csv('WeatherData/ferrara_270615.csv')
df_milano = pd.read_csv('WeatherData/milano_270615.csv')
df_mantova = pd.read_csv('WeatherData/mantova_270615.csv')
df_ravenna = pd.read_csv('WeatherData/ravenna_270615.csv')
df_torino = pd.read_csv('WeatherData/torino_270615.csv')
df_asti = pd.read_csv('WeatherData/asti_270615.csv')
df_bologna = pd.read_csv('WeatherData/bologna_270615.csv')
df_piacenza = pd.read_csv('WeatherData/piacenza_270615.csv')
df_cesena = pd.read_csv('WeatherData/cesena_270615.csv')
df_faenza = pd.read_csv('WeatherData/faenza_270615.csv')

temp_ferrara = df_ferrara['temp'].tolist()
temp_milano = df_milano['temp'].tolist()
temp_mantova = df_mantova['temp'].tolist()
temp_ravenna = df_ravenna['temp'].tolist()
temp_torino = df_torino['temp'].tolist()
temp_asti = df_asti['temp'].tolist()
temp_bologna = df_bologna['temp'].tolist()
temp_piacenza = df_piacenza['temp'].tolist()
temp_cesena = df_cesena['temp'].tolist()
temp_faenza = df_faenza['temp'].tolist()

day_ferrara = df_ferrara['day'].tolist()

day_ferrara = [parser.parse(x) for x in day_ferrara]
fig, ax = plt.subplots()

hours = mdates.DateFormatter('%H:%M')
ax.xaxis.set_major_formatter(hours)

ferrara=ax.plot(day_ferrara, temp_ferrara, '#FF4500',label="ferrara")
milano=ax.plot(day_ferrara, temp_milano, '#8B0000',label="milano")
mantova=ax.plot(day_ferrara, temp_mantova, '#2F4F4F',label="mantova")
ravenna=ax.plot(day_ferrara, temp_ravenna, '#191970',label="ravenna")
torino=ax.plot(day_ferrara, temp_torino, '#8470FF',label="torino")
asti=ax.plot(day_ferrara, temp_asti, '#00BFFF',label="asti")
bologna=ax.plot(day_ferrara, temp_bologna, '#00FF7F',label="bologna")
piacenza=ax.plot(day_ferrara, temp_piacenza, '#FFFF00',label="piacenza")
cesena=ax.plot(day_ferrara, temp_cesena, '#CD5C5C',label="cesena")
faenza=Er=ax.plot(day_ferrara, temp_faenza, '#FF1493',label="faenza")

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1])

plt.xlabel("Time")
plt.ylabel("Temperature")

plt.savefig('test', dpi=115)  # plt.savefig()将输出图形存储为文件，默认为png格式，可以通过dpi修改输出质量
plt.show()
