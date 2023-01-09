



def main():
    pass

if __name__ == '__main__':
    main()

# import dataset from github pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import time

# import dataset from github pandas
df = pd.read_csv('https://raw.githubusercontent.com/ifood/ifood-data-business-analyst-test/master/ml_project1_data.csv', sep=',')

# view NaN values of dataframe column
df.isnull().sum()


# Map a sqlalchemy model to dataframe column

# remove rows with NaN values
df = df.dropna()

# get 5 rows with column = 1 and 5 rows with column = 0 sorted by column = 1


df = df.groupby('column').head(5)

# move column position to begin of dataframe
# move column to begin of dataframe
cols = df.columns.tolist()
cols = cols[-1:] + cols[:-1]
df = df[cols]

# get mean of a column group by another column
df.groupby('column').mean()


# quero saber a media de column1 quando coluna2 = 1
df.groupby('column2').mean()