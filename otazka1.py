import pandas as pd
import matplotlib.pyplot as plt

from cleverminer import cleverminer

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

subset = data1[data1['Time Category'].isin(['Afternoon', 'Forenoon']) 
               & data1['Arrest'].isin(['False']) & data1['Domestic'].isin(['False'])]

# Count crimes for each day of the week
counts = subset['Day'].value_counts()
# total of counts
print(counts.sum()) #prints 80399

days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
# Sort counts by the days of the week
counts = counts.loc[days_order]

counts.plot(kind='bar')
plt.title("Title")
plt.xlabel("Day of the Week")
plt.ylabel("Number of Crimes")
plt.show()
