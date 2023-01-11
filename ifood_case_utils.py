



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


#
# ordinalEncoder = OrdinalEncoder(categories=categories)
# # df['Education_Cat'] = ordinalEncoder.fit_transform([df['Education'])
# # df['Education_Cat'] = labelencoder.fit_transform(df['Education'])
# #
# #
# ordinalEncoder.categories_

categories = [['Basic', '2n Cycle', 'Graduation', 'Master', 'PhD']]
ordinalEncoder = OrdinalEncoder(categories=categories)
df['Education_Cat'] = ordinalEncoder.fit_transform(df['Education'].values.reshape(-1, 1))
df['Education_Cat'] = df['Education_Cat'].astype(int)




