# -*- coding: utf-8 -*-
"""task1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1B_Tr5Xp_5hZUwW2xb-TMFswR1ZydvQRa
"""

#importing module
import pandas as pd

#This line of code is importing a specific tool for data analysis in Python called Pandas.

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#This code snippet imports three essential Python libraries commonly used in data science for numerical computations, plotting, and creating statistical visualizations

#importing the dataset by reading the csv file
data = pd.read_csv('/netflix_data.csv')

#displaying the first five rows of dataset
print(data.head())

#displayinf last five rows of dataset
data.tail()

data.shape

data.info()

data.describe()

data.isnull()

data.isna()

data.isna().any()

data.isna().sum()

data.isna().any().sum()

# Assuming your DataFrame is called 'data' and you want to drop the column 'column_name'
data = data.drop('director', axis=1)

data = data.drop('cast', axis=1)

data.isna().sum()

data.fillna(value=0, method=None, axis=None, inplace=False, limit=None, downcast=None)

data.duplicated()

data.duplicated().value_counts()

data.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)

data.duplicated().value_counts()

data.dtypes

# Ensure 'date_added' is in datetime format
data['date_added'] = pd.to_datetime(data['date_added'], errors='coerce')

# Convert to 'dd-mm-yyyy' format
data['date_added'] = data['date_added'].dt.strftime('%d-%m-%Y')

data.columns

list(data.columns)

# Rename specific columns using a dictionary
data = data.rename(columns={'listed_in': 'genre'})

list(data.columns)

#genre column has multiple values separated by commas which could mess up my reporting
#so i decided to split them into separate columns instead

data[['genre1', 'genre2', 'genre3']] = data['genre'].str.split(',', expand=True)

print(data.head())

#duration is in seasons and minutes which is not clear, and incorrect data type
data['duration'].value_counts()

#i will now drop the combined genre column as i have created the splitted columns which give a more organised look
data = data.drop('genre', axis=1)

#an issue i faced was tv shows and movies have been put into the same dataset and their durations are in seasons and minutes
#respectively, so i decided to assume that each season of a TV show has approximately 30 episodes and each episode's runtime
#is about 25 minutes so i'm doing the conversion into minutes accordingly

data['duration_numeric']=data['duration'].str.extract('(\d+)').astype(float)

#now converting durations into minutes based on their units
# Use na=False to handle missing values in 'duration' column
data.loc[data['duration'].str.contains('min', na=False),'duration_numeric']
 #no conversion needed for minutes
# Use na=False to handle missing values in 'duration' column
data.loc[data['duration'].str.contains('Season', na=False),'duration_numeric']*=30*25
#1 season, 30 episodes, 25 minutes each

print(data)

#I shall now drop the original duration column

data = data.drop('duration', axis=1)

data.head()

data.dtypes

# Convert multiple columns to string type
columns_to_convert = ['type', 'country', 'description', 'genre1', 'genre2', 'genre3']
data[columns_to_convert] = data[columns_to_convert].astype('string')

data.dtypes

data.to_csv('cleaned_netflix_data.csv', index=False)

import os
print(os.getcwd())

data.to_csv('/content/cleaned_netflix_data.csv', index=False)

from google.colab import drive

drive.mount('/content/drive')

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import os

filename = 'cleaned_netflix_data.csv'
# Save the file to your Google Drive in a folder called 'Netflix_Data'
# Create this folder in your Google Drive if it doesn't exist
folder_path = '/content/drive/My Drive/Netflix_Data/'

# Check if the folder exists, and create it if it doesn't
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

data.to_csv(os.path.join(folder_path, filename), index=False)

data.isna().any()

data.isna().sum()

data.fillna(value="unknown", method=None, axis=None, inplace=False, limit=None, downcast=None)

data.isna().sum()

data = data.fillna(method='ffill')

data.isna().sum()

data = data.fillna({'genre2': 'Unknown', 'genre3': 'Unknown'})

data.isna().sum()

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import os

filename = 'cleaned_netflix_data.csv'
# Save the file to your Google Drive in a folder called 'Netflix_Data'
# Create this folder in your Google Drive if it doesn't exist
folder_path = '/content/drive/My Drive/Netflix_Data/'

# Check if the folder exists, and create it if it doesn't
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

data.to_csv(os.path.join(folder_path, filename), index=False)