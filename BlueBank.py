#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 17:51:32 2023

@author: fed
"""

import json
import pandas as pd
import matplotlib.pyplot as plt

#method 1 to read json file (loaded as a list)
#open the file

json_file=open('loan_data_json.json')

#read the file

data=json.load(json_file)

#method 2 to read json file (loaded as a list)

with open('loan_data_json.json') as json_file:
    data=json.load(json_file)
    print(data)
 
    
#transform to dataframe
 
loandata=pd.DataFrame(data)
 
 
#finding unique values in a specific column: 'purpose'column

loandata['purpose'].unique()

#describe the data

loandata.describe()


#describe the data for a specific column

loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

# using EXP() to get the annual income

import numpy as np
income=np.exp(loandata['log.annual.inc'])

#create column 'annualincome

loandata['annual.income']=income

#drop column 'annual_income'
loandata=loandata.drop('annual_income' , axis=1)

#obtain a new column representing the fico category
# fico score

loandata.info()

fico=700

if fico>= 300 and fico<400 : 
    ficocat='Very poor'
elif fico>=400 and fico < 600 :
    ficocat='Poor'
elif fico>= 600 and fico < 660 :
    ficocat='Fair'
elif fico>=660 and fico< 700:
    ficocat='Good'
elif fico>= 700 : 
    ficocat='Excellent'
else :
    ficocat='Unknown'
print(ficocat)
    


#applying for loops to loan data

ficocat=[]

for x in range(0,len(loandata)):
    category=loandata['fico'][x]
    if category>=300 and category<400:
        cat='Very Poor'
    elif category>=400 and category<600:
        cat='Poor'
    elif category>=600 and category<660:
        cat='Fair'  
    elif category>=660 and category<700:
        cat='Good' 
    elif category>=700 :
        cat='Excellent'           
    else:
        cat='Unknown'
    ficocat.append(cat) 
           
loandata.describe()

 
 #Transform ficocatfrom a list to a serie which is a column in the DataFrame
 
ficocat=pd.Series(ficocat)
 
#Append the column ficocat into the DF to be renamed as fico.cat
 
loandata['fico.cat']=ficocat
 
#df.loc as conditional statements to create a column based on a certain condition
 
#df.loc[df[columnname], condition, new columnname]='value if the condition is met'
#for interest rates a new column is wanted. rate >0.12  then'high' else 'low'
 
 
loandata.info()
 
loandata.loc[loandata['int.rate']>0.12, 'int.rate.type']='High'
 
loandata.loc[loandata['int.rate']<=0.12, 'int.rate.type']='Low'
 
 
#number of loans/rows by fico.category
 
catplot=loandata.groupby(['fico.cat']).size()
 
catplot.plot.bar(color='green', width=0.3)
plt.show()
 
purposeplot=loandata.groupby(['purpose']).size()
 
purposeplot.plot.bar(color='pink', width=0.2)
plt.show()
 
 
#scatter plots
 
ypoint=loandata['annual.income']
xpoint=loandata['dti']
plt.scatter(xpoint, ypoint, color='red')
plt.show()
 
#writing to csv
 
loandata.to_csv('loan_cleaned.csv', index=True)

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 



