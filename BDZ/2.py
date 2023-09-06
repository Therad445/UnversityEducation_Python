import pandas as pd
data = pd.read_csv('train.csv')
males = data[data.Sex == 'male']
females = data[data.Sex == 'female']

print(' Male\n\n')
print(males.describe())
print(' Female\n\n')
print(females.describe())
