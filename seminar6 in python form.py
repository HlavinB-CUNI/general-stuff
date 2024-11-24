import math
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats

#Task 1: Read data and understand it's structure
#1a. Load training dataset

    #data in 99_files/house-prices-kaggle.zip
    #load train.csv
    #and display 5 random rows

#Hint: Use .style attribute to display all columns

#Hint: See data_description.txt for documentation of variables

# necessary if in zip file
import zipfile

# Load the data
with zipfile.ZipFile('../99_files/house-prices-kaggle.zip') as z:
    print(z.namelist())

# formatting if in zip file
with zipfile.ZipFile('../99_files/house-prices-kaggle.zip') as z:
    with z.open('train.csv') as f:
        df = pd.read_csv(f)

df.head()
df.tail()
df.info()

# random sampling of 5 rows
df.sample(5).style

# formatting if in zip file
with zipfile.ZipFile('../99_files/house-prices-kaggle.zip') as z:
    with z.open('data_description.txt') as f:
        desc_data = f.read().decode('utf-8')
        print(desc_data)

# formatting if NOT in zip file (make sure to check what the data is separated by)
df = pd.read_csv('04_auxiliary/data_2017_zs.csv', sep = ';', on_bad_lines= 'skip')
df.head()

#1b. What is the distribution SalePrice variable?
#plot histogram (.hist() on pd.Series) with bin width $10,000
df.SalePrice.hist(bins=10)
df.SalePrice.hist(bins=range(0, df.SalePrice.max(), 10000))

#1c. Split columns between quantitative and qualitative variables
quantitative = [column for column in df.columns if df.dtypes[column] != 'object']
qualitative = [column for column in df.columns if df.dtypes[column] == 'object']

print(quantitative)
print(qualitative)


#1c* display df with only quantitative columns

df[quantitative]

#1d. Are dtypes correct?
df[qualitative].sample(5).style
df.isna().sum().sort_values(ascending=False).plot.bar(figsize=(15, 5))


#Task 2: Aggregation
#2.1 Calculate the average LotArea for each year (YrSold)

df.groupby('YrSold').first()
df.groupby('YrSold')[['LotArea']].mean()
df[['YrSold', 'LotArea']].groupby('YrSold').agg(["mean", "min", "max"]).reset_index()
df.groupby('YrSold').agg({"LotArea": ["mean", "min", "max"]})
df.groupby('Street').agg({"SalePrice": ["mean"]}).reset_index()

#2.2 Calculate the average SalePrice for Grvl street (Street)

df_gr = df.groupby('Street').agg({"SalePrice": ["mean"]}).reset_index()

df_gr[df_gr['Street'] == 'Grvl']

# average of sale price for street type "Grvl"
df[df['Street'] == 'Grvl']['SalePrice'].mean()

#2.3 Calculate the average SalePrice for Grvl street (Street) But! Take into account only flats which cost more than 300000

df_filtered = df[df['SalePrice'] > 300000]
df_filtered.groupby('Street').agg({"SalePrice": ["mean"]}).reset_index()

#Task 3 Filtering
#3.1 How many flats cost less than 200000 and have a 'Normal' condition (column SaleCondition)

df[(df['SalePrice'] < 200000) & (df['SaleCondition'] == 'Normal')].shape[0] # same thing
len(df[(df['SalePrice'] < 200000) & (df['SaleCondition'] == 'Normal')]) # same thing

#3.2 How many flats cost less than 200000 or have a 'Normal' condition (column SaleCondition)
df[(df['SalePrice'] < 200000) | (df['SaleCondition'] == 'Normal')].shape[0]

#3.3 How many flats cost have more areas on the second floor(2ndFlrSF) then on the first one(1stFlrSF)?
df[df['1stFlrSF'] < df['2ndFlrSF']].shape[0]

#What is the average cost (in thousands) for such type of the flats?

xk = round(df[df['1stFlrSF'] < df['2ndFlrSF']]['SalePrice'].mean()/10**3, 2)
print(f"Average sale price for houses with 1stFlrSF < 2ndFlrSF: {xk}k")

#BONUSES
#Task 1: Study relationships between variables
#1a. see correlation matrix

fig = plt.subplots(1, 1, figsize=(15, 12))
# correlation matrix
df_corr = df[quantitative].corr()
sns.heatmap(df_corr, vmin=-1, cmap="coolwarm", annot=True, fmt="0.1f") 
# annot=True to print values inside the square
# fmt="0.1f" to print one decimal place
# vmin=-1 to set the minimum value of the color scale to -1

#2b. Boxplots for categorical variables

df[qualitative].head()

# pick one categorical column and one quantitative column
sns.boxplot(data=df, x="MSZoning", y="SalePrice", hue='MSZoning') # 


