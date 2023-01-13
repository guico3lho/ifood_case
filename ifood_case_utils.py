

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

# for column in df.columns():


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

# remove rows with missing values

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split



models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
results = []
names = []
for name, model in models:
    kfold = model_selection.KFold(n_splits=10, random_state=7)
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std  ())




