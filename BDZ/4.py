import pandas as pd
data = pd.read_csv('train.csv')
names = {}
for row in data.iterrows():
    row = row[1]
    name = row.Name.split(',')[0]
    names[name] = names.setdefault(name, 0) + 1
list_d = list(names.items())
list_d.sort(key=lambda i: i[1])
for i in range(10):
    print(list_d[-i - 1][0], ' - ', list_d[-i-1][1], ' times')