import pandas as pd

from cleverminer import cleverminer

# Load the dataset
data1 = pd.read_csv('Crimes_clean_2016.csv')

clm = cleverminer(df=data1, target='Day', proc='CFMiner',
                      quantifiers={'Base': 50000, 'S_Up': 3},
                      cond={
                          'attributes': [
                              {'name': 'Area Category', 'type': 'subset', 'minlen': 1, 'maxlen': 2},
                              {'name': 'Arrest', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                              {'name': 'Domestic', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                              {'name': 'Time Category', 'type': 'subset', 'minlen': 1, 'maxlen': 2},
                              {'name': 'Primary Type', 'type': 'subset', 'minlen': 1, 'maxlen': 2},
                          ], 'minlen': 1, 'maxlen': 4, 'type': 'con'
                      })

clm.print_rulelist()