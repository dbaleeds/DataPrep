# -*- coding: utf-8 -*-
"""
Created on Thursday Dec 11 15:19:00 2018
@author: dbaleeds
A script to render data to acceptable thresholds for output
"""
import pandas as pd
import csv
import re

#set the threshold
threshold = 5

#set what the value should show if it falls below the threshold
placeholder = '<5'

#set the columns for which the outputs should be truncated
truncateColumns = ["question1","question2","question3","question4","question5","question6","question7","question8","question9","question10"]

data = pd.read_csv("Thresholds/thresholds.csv",usecols=truncateColumns)

for column in truncateColumns:
    print(column)
    data[column] = data[column].astype(str).str.replace(r'^[0-'+str(threshold)+']{1}$',placeholder)


print(data)
