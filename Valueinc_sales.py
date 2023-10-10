#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 09:03:40 2023

@author: fed
"""

import pandas as pd

#file_name =pd.read_csv('file.csv')<---- format of read_csv

data=pd.read_csv('transaction_valueinc.csv')


#Change the delimiter to properly visualize the information in the column. 
data=pd.read_csv('transaction_valueinc.csv',sep=';')

#Quick overview of the DataFrame
 
data.info() 

#Playing around with variables

var={'name':'federico', 'location':'genoa'}

#Working woth calculations

#Defining variables

CostPerItem=11.73
SellingPricePerItem=21.11
NumberOfitemsPurchased=6

#Mathematical operations

ProfitPerItem= 21.11-11.73

ProfitPerItem= SellingPricePerItem-CostPerItem

ProfitPerTransaction=ProfitPerItem*NumberOfitemsPurchased

CostPerTransaction=CostPerItem*NumberOfitemsPurchased

SellingPrice=NumberOfitemsPurchased*SellingPricePerItem

#CostPerTransaction column calcolation
#CostPerTransaction=CostPerItem*numberOfItemsPurchased
#variable=dataframe['column_name']

CostPerItem=data['CostPerItem']

NumberOfItemsPurchased=data['NumberOfItemsPurchased']

CostPerTransaction=NumberOfItemsPurchased*CostPerItem

#Adding a new column to df: method 1

data['CostPerTransaction']=CostPerTransaction

# Adding a new column to df: method 2.
#Syntax: data['CostPerTransaction']=data['CostPerItem']*data['NumberOfItemsPurchased']

data['SalesPerTransaction']=data['SellingPricePerItem']*data['NumberOfItemsPurchased']

#Calculate Profit (sales-cost) and Markup (sales-cost)/cost

data['Profit']=data['SalesPerTransaction']- data['CostPerTransaction']
data['Markup']=data['Profit']/data['CostPerTransaction']

#Utilizziamo la funzione 'round' su perceentuale Markup (EX. 2 DECIMAL PLACES MAXIMUM)
roundmarkup=round(data['Markup'],2)
data['roundmarkup']= roundmarkup


#Combining data fields (voglio unire i tre campi data yy, mm, dd)--concatenate fields 
#Date_str=  'Day' + '-' 
#Checking colum datatype

print(data['Day'].dtype)

#Change columns type 'astype'

day=data['Day'].astype(str)

print(day.dtype)

data.info()

Date_str=day+'-'+data['Month']

year=data['Year'].astype(str)

Date_str=day+'-'+data['Month']+'-'+year

print(year.dtype)

data['date']=Date_str

#Use iloc to view specific columns/rows
#visulizziamo per esempio la prima riga del nostro df

data.iloc[0]



data.iloc[0]#view of the row with index=0

data.iloc[0:3]#view of the first 3 rows

data.iloc[-5]#view the last 5 rows

data.head(5)#Brings in first 5 rows

data.iloc[:,2]#Brings in all rows on the 2nd column

data.iloc[:,:2]#Brings in all rows on the first 2 columns


#Function 'split' to split the column keyword
#new_var=column.str.split('sep', expand=true)

data.info()

split_column=data['ClientKeywords'].str.split(',', expand=True)

#Dopo lo split della colonna client keyword, otteniamo tre nuove colonne 

data['ClientAge']=split_column[0]

data['ClientType']=split_column[1]

data['ClientLengthofContract']=split_column[1]

#Using the 'REPLACE' function: Eliminiamo la parentesi dalla colonna ClientAge

data['ClientAge']=data['ClientAge'].str.replace('[', '')

data['ClientLengthofContract']=data['ClientLengthofContract'].str.replace (']','')


#Using the lowercase function to change item lowercase

data['ItemDescription']=data['ItemDescription'].str.lower()

#How to merge files
#Joining function (MERGING); creo colonna che prende dati da altro file.. in questo caso informazione high, medium, low season
#Bringing in a new dataset

seasons=pd.read_csv ('value_inc_seasons.csv')

seasons=pd.read_csv ('value_inc_seasons.csv', sep=';')

#merging files: merge_file=pd.merge (df_old, df_new, on='key')

merged_data=pd.merge(data, seasons, on='Month')

#Dropping fields
#df=df.drop('columnname', axis=1)

merged_data=merged_data.drop('ClientKeywords', axis=1)

merged_data=merged_data.drop('Day', axis=1)

#Drop multiple columns;use brackets []

merged_data=merged_data.drop(['Year', 'Month'], axis=1)

#Quando il file è stato pulito lo esportiamo in csv per poi essere elaborato in Tableau
#Export file to into a .csv format

merged_data.to_csv('ValueInc_cleaned.csv', index=False)


