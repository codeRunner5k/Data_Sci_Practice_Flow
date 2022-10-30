# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 13:44:48 2022

@author: andre
"""
import pandas as pd
import statistics
from datetime import datetime, timedelta
#createDataFrameCSV(...) is used to create a data frame from a given csv
#If not given a data frame uses the runningData.csv file
#returns a df off of runningData.csv
def createDataFrameCSV(df='runningData.csv'):
    return pd.read_csv(df)
  
#createDFwithSpecficColumns(...) creates a data frame with specfic columns. 
#If not given a data frame columns uses the runningData.csv data frame columns
#returns a df based off the runningData.csv columns  
def createDFwithSpecficColumns(df,colWanted=["Distance_Miles","AVG_Pace","Date","Time","AVG_Speed","Duration","Calories","Fastest_Mile","Slowest_Mile"]):
    return df[colWanted]

#getDataFrameInfo(...) gets generally information regarding data frames number of columns, data type, etc
#returns df information wanted 
def getDataFrameInfo(df):
    return df.info()


#for col in ("Gun_time", "Net_time", "Pace"):
#    df[col] = pd.to_timedelta(df[col])
def convertTimeInfo(df):
    convertTimeLst = []
    for col in range(len(df)):
        convertTimeLst.append(pd.to_timedelta(df[col]))
    return convertTimeLst


df = createDataFrameCSV()
df2 = createDFwithSpecficColumns(df)
dfDuration = df2["Duration"]
print (df[8])

print("Mean of Distance ran is " + str(statistics.mean(df2["Distance_Miles"])) + " miles")
print("Mode of Distance ran is "+ str(statistics.mode(df2["Distance_Miles"])) + " miles")
print("Median of Distance ran is " + str(statistics.median(df2["Distance_Miles"]))+ " miles")
#dfDuration = convertTimeInfo(dfDuration)

#print("Mean of Distance ran is " + str(dfDuration.mean()) + " miles")
#print("Mode of Distance ran is "+ str(statistics.mode(dfDuration)) + " miles")
#print("Median of Distance ran is " + str(statistics.median(dfDuration))+ " miles")
#print (getDataFrameInfo(df2))
