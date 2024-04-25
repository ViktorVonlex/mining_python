import pandas as pd
import matplotlib.pyplot as plt

from cleverminer import cleverminer

# Load the dataset
data1 = pd.read_csv('Merged_data.csv')

days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days_order_type = pd.CategoricalDtype(categories=days_order, ordered=True)
data1['Day'] = data1['Day'].astype('category').cat.reorder_categories(days_order,ordered=True) 

clm = cleverminer(df=data1,proc='4ftMiner',
               quantifiers= {'Base': 5000, 'aad': 0.1},
               ante ={
                    'attributes':[
                        {'name': 'Day', 'type': 'rcut', 'minlen': 1, 'maxlen': 2}
                    ], 'minlen':1, 'maxlen':1, 'type':'con'},
               succ ={
                    'attributes':[
                        {'name': 'Primary Type', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                    ], 'minlen':1, 'maxlen':1, 'type':'con'},
               )


clm.print_rulelist()
clm.print_rule(1)
clm.print_rule(2)


