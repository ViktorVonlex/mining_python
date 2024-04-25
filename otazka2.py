import pandas as pd
import matplotlib.pyplot as plt

from cleverminer import cleverminer

data1 = pd.read_csv('Crimes_clean_2016.csv')

# Extract month from Date
data1['Month'] = pd.DatetimeIndex(data1['Date']).month

month_order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
month_order_type = pd.CategoricalDtype(categories=month_order, ordered=True)
data1['Month'] = data1['Month'].astype('category').cat.reorder_categories(month_order,ordered=True)

days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days_order_type = pd.CategoricalDtype(categories=days_order, ordered=True)
data1['Day'] = data1['Day'].astype('category').cat.reorder_categories(days_order,ordered=True) 


clm = cleverminer(df=data1, target='Month', proc='CFMiner',
                      quantifiers={'Base': 50000, 'S_Down': 6},
                      cond={
                          'attributes': [
                              {'name': 'Area Category', 'type': 'subset', 'minlen': 1, 'maxlen': 2},
                              {'name': 'Arrest', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                              {'name': 'Domestic', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                              {'name': 'Time Category', 'type': 'subset', 'minlen': 1, 'maxlen': 2},
                              {'name': 'Primary Type', 'type': 'subset', 'minlen': 1, 'maxlen': 2},
                              {'name': 'Day', 'type': 'lcut', 'minlen': 1, 'maxlen': 5}
                          ], 'minlen': 1, 'maxlen': 4, 'type': 'con'
                      })

clm.print_rulelist()
clm.print_rule(1)
clm.print_rule(2)

# Categories and their frequencies
categories = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
frequencies = [3932, 3634, 4318, 4178, 4640, 4808, 4711, 4694, 4176, 4171, 3800, 3727]

# Create the bar plot
plt.bar(categories, frequencies)
plt.title("Rule 1 histogram")
plt.xlabel("Month")
plt.ylabel("Frequency")
plt.xticks(rotation=0)
plt.show()