import csv
import pandas as pd
from pandas import Series,DataFrame
from bs4 import BeautifulSoup
import html5lib
import string
import time
from urllib import parse
from sys import argv
import os
import google
from openpyxl import Workbook, load_workbook

#Take in excel sheet of companies to a dataframe
job_file = pd.read_excel('jobs.xlsx', sheetname=0, parse_cols=1) #opens jobs excel file into dataframe
web_list = list()


#Search the term + "careers" on google, append to web_list
for each in job_file.iloc[:10,0]:
    search = each
    search_term = each + " careers"
    for url in google.search(search_term, tld='com', lang='en', num=1,start=1,stop=2,pause=10.0): #only grabbing one url, but this returns an iterator so:
        #job_file.iloc[[job_file.iloc[:,0]== search],1] = url[0]
        web_list.append(url)

web_list = DataFrame(web_list, columns='Websites')
full_df = pd.concat([job_file,web_list], axis=0, join='outer', copy=False)

#Write to excel sheet
full_df.to_excel('jobs.xlsx', sheet_name='Sheet1')
