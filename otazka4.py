import pandas as pd
import matplotlib.pyplot as plt

from cleverminer import cleverminer

# Load the dataset
data1 = pd.read_csv('Merged_data.csv')

days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days_order_type = pd.CategoricalDtype(categories=days_order, ordered=True)
data1['Day'] = data1['Day'].astype('category').cat.reorder_categories(days_order,ordered=True) 


clm = cleverminer(df=data1, proc='SD4ftMiner',
                  quantifiers={'FrstRelBase': 0.005, 'ScndRelBase': 0.005, 'Ratioconf': 1.1},
                  ante={
                      'attributes': [
                          {'name': 'Domestic', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                          {'name': 'Area Category', 'type': 'subset', 'minlen': 1, 'maxlen': 2},
                          {'name': 'Primary Type', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                      ], 'minlen': 1, 'maxlen': 2, 'type': 'con'},
                  succ={
                      'attributes': [
                        {'name': 'Arrest', 'type': 'one', 'value': 'True'},
                      ], 'minlen': 1, 'maxlen': 1, 'type': 'con'},
                  frst ={
                      'attributes':[
                          {'name': 'Temperature Category', 'type': 'one', 'value': 'medium'},
                      ], 'minlen': 1, 'maxlen': 1, 'type':'con'},
                  scnd ={
                      'attributes':[
                          {'name': 'Temperature Category', 'type': 'one', 'value': 'high'},
                      ], 'minlen': 1, 'maxlen': 1, 'type':'con'}    
                  )


clm.print_rulelist()
clm.print_rule(2)
