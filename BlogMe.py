#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 21:50:23 2023

@author: fed
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#reading excel or xlsx file

data=pd.read_excel('articles.xlsx')

#describe data


#summary of the data
data.describe()

#summary of the columns
data.info()

#counting the number of articles by  source_name
# format of group by: df.groupby(['column_name'])['column_count'].count()

data.groupby(['source_id'])['article_id'].count()

#let's visualize the number of reactions (sum)

data.groupby(['source_id'])['engagement_reaction_count'].sum()


#visualize unique values within a column
unique_author=data['author'].unique()
print(unique_author)
#add this as column to the data as authors_list

#dropping a column

data=data.drop('engagement_comment_plugin_count', axis=1)

#creating a keyword column

keyword='crash'

#let's create a for loop to isolate each title row

#crearting a keyword flag
keyword='crash'



# #create a for loop to isolate each title row

# length=len(data)
# keyword_flag=[] #create a flag_column to be populated with the output

# for x in range (0,length):
#     header=data['title'][x]
#     if keyword in header:
#         flag=1
#     else:
#         flag=0
#     keyword_flag.append(flag)
    
# #creating a function *** TypeError: argument of type 'float' is not iterable

# def keywordflag(keyword):
#     length=len(data)
#     keyword_flag=[]

#     for x in range (0,length): #x at row 3181 there is nan
#         header=data['title'][x]
#         if keyword in header:
#             flag=1
#         else:
#             flag=0
#         keyword_flag.append(flag)
#     return keyword_flag
# k = keywordflag('support')


#option 2: correct the previous code *** TypeError: argument of type 'float' is not iterable
# def keywordflag(keyword, data):
#     length = len(data)
#     keyword_flag = []

#     for x in range(0, length):
#         header = str(data['title'][x])  # Convert to string
#         if keyword in header:
#             flag = 1
#         else:
#             flag = 0
#         keyword_flag.append(flag)
#     return keyword_flag
# k=keywordflag("support",data)

# #create a new column in data dataframe

# data['keyword_flag']=pd.Series(keywordflag)



#option 2 with try: correct the previous code *** TypeError: argument of type 'float' is not iterable


def keywordflag(keyword):  # Define a function named keywordflag that takes a 'keyword' argument
    length = len(data)  # Calculate the length of the 'data' object (assuming 'data' is accessible in this scope)
    keyword_flag = []  # Create an empty list to store flags

    for x in range(0, length):  # Iterate through a range of numbers from 0 to 'length - 1'
        heading = data['title'][x]  # Get the value of the 'title' column for the current row
        try:  # Start a try/except block for error handling
            if keyword in heading:  # Check if the 'keyword' is in the 'heading'
                flag = 1  # If it is, set 'flag' to 1
            else:
                flag = 0  # If not, set 'flag' to 0
        except:  # Handle any exceptions (errors) that occur in the try block
            flag = 0  # Set 'flag' to 0 in case of an exception

        keyword_flag.append(flag)  # Append the 'flag' value to the 'keyword_flag' list
    return keyword_flag  # Return the list of flags as the result of the function

# Assuming 'data' is defined elsewhere in your code
k = keywordflag('crash')  # Pass the keyword as an argument, not with append

#create a column in data dataframe

data['keyword_flag']=pd.Series(k)


#SentimentIntensityAnalyzer

sent_int=SentimentIntensityAnalyzer()
text=data['title'][16]
sent=sent_int.polarity_scores(text)

neg=sent['neg']
pos=sent['pos']
neu=sent['neu']


#adding a full loop to extract sentiment per title

title_neg_sent=[]
title_pos_sent=[]
title_neu_sent=[]


length=len(data)
for x in range(0, length):
    try:
        text=data['title'][x]
        sent_int=SentimentIntensityAnalyzer()
        sent=sent_int.polarity_scores(text)
        neg=sent['neg']
        pos=sent['pos']
        neu=sent['neu']
    except:
       neg=0
       pos=0
       neu=0
          
    title_neg_sent.append(neg)
    title_pos_sent.append(pos)
    title_neu_sent.append(neu)
    
#create columns in data dataframe

data['title_neg_sent']=pd.Series(title_neg_sent)
data['title_pos_sent']=pd.Series(title_pos_sent)
data['title_neu_sent']=pd.Series(title_neu_sent)

#writing the data

data.to_excel('blogMedata_clean.xlsx', sheet_name='BlogMe', index=False)
    





