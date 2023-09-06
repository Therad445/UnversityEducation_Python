import pandas as pd
data = pd.read_csv('train.csv')
ports = ['C', 'Q', 'S']
# people = { port : [dead, alive] }
people = {'C': [0, 0], 'Q': [0, 0], 'S': [0, 0]}
for row in data.iterrows():
    row = row[1]
    if row.Embarked not in ports: # is NaN
        continue
    if row.Survived:
        people[row.Embarked][1] += 1
    else:
        people[row.Embarked][0] += 1
sum_dead = 0
for v in people.values():
    sum_dead += v[0]
for k,v in people.items():
    print(k, ':')
    print('\tdead - %s' % v[0])
    print('\talive - %s' % v[1])
    print('\tdead from all from this port %.2f%%' % (v[0] / (v[0] + v[1]) * 100))