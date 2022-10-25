# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 13:44:48 2022

@author: andre
"""
import pandas as pd

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

df = createDataFrameCSV()
df2 = createDFwithSpecficColumns(df)
print (df2["AVG_Speed"])
