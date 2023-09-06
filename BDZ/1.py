import pandas as pd
data = pd.read_csv('train.csv')
# array of arrays
# stat[Pclass-1] = [dead_male, alive_male, dead_female, alive_female]
stat = [[0,0,0,0] for _ in range(3)]
for row in data.iterrows():
    row = row[1]
    if row.Sex == 'male':
        if row.Survived == 0:
            stat[row.Pclass-1][0] += 1
        else:
            stat[row.Pclass - 1][1] += 1
    else:
        if row.Survived == 0:
            stat[row.Pclass-1][2] += 1
        else:
            stat[row.Pclass - 1][3] += 1
for i in range(3):
    Pclass = stat[i]
    print('Pclass', i+1)
    print('Male:\n\tdead - %d\n\talive - %d' % (Pclass[0],
Pclass[1]))
    print('Female:\n\tdead - %d\n\talive - %d' % (Pclass[2],
Pclass[3]))