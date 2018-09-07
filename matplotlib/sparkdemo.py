# -*- coding: utf-8 -*-
# @Time    : 2018/8/15 12:09
# @Author  : Lsp

import pandas as pd
from pyspark.sql import SparkSession

userDF = pd.read_csv(r"WeatherData/asti_270615.csv")

# 启动spark
spark = SparkSession \
	.builder \
	.appName("Python Spark SQL Hive integration example") \
	.enableHiveSupport() \
	.getOrCreate()

# spark读取pandas dataframe,形成spark dataframe
sparkDF = spark.createDataFrame(userDF)
sparkDF.show()
