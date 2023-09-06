import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

pd.options.mode.chained_assignment = None
data = pd.read_csv('train.csv')
data['Age'] = data['Age'].fillna(data['Age'].median())
data_to_train = data[['Pclass', 'Age', 'Sex']]
data_to_train['Sex'] = np.where(data_to_train['Sex'] == 'female', 0, 1)
test = pd.read_csv('test.csv')
test['Age'] = test['Age'].fillna(test['Age'].median())
data_to_test = test[['Pclass', 'Age', 'Sex']]
data_to_test['Sex'] = np.where(data_to_test['Sex'] == 'female', 0, 1)
expected_data = data['Survived']
rf = RandomForestClassifier(n_estimators=100)
rf.fit(data_to_train, expected_data)
pred = rf.predict(data_to_test)
with open('output.txt', 'w') as f:
    for p in pred:
        f.write(str(p) + '\n')