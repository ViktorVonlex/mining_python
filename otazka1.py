import pandas as pd
import matplotlib.pyplot as plt

from cleverminer import cleverminer

data1 = pd.read_csv('Crimes_clean_2016.csv')

days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days_order_type = pd.CategoricalDtype(categories=days_order, ordered=True)
data1['Day'] = data1['Day'].astype('category').cat.reorder_categories(days_order,ordered=True) 

clm = cleverminer(df=data1, target='Day', proc='CFMiner',
                      quantifiers={'Base': 50000, 'S_Up': 4},
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
clm.print_rule(30)

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
frequencies = [7588, 7651, 7823, 7957, 8375, 7649, 6767]

# Create the bar plot
plt.bar(days, frequencies)
plt.title("Days of the Week")
plt.xlabel("Day")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.show()