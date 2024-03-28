import pandas as pd
import matplotlib.pyplot as plt

from cleverminer import cleverminer

# Load the dataset
data1 = pd.read_csv('Merged_data.csv')

clm = cleverminer(df=data1,proc='4ftMiner',
               quantifiers= {'Base': 5000, 'conf': 0.35},
               ante ={
                    'attributes':[
                        {'name': 'Area Category', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                        {'name': 'Temperature Category', 'type': 'subset', 'minlen': 1, 'maxlen': 1}
                    ], 'minlen':1, 'maxlen':1, 'type':'con'},
               succ ={
                    'attributes':[
                        {'name': 'Primary Type', 'type': 'subset', 'minlen': 1, 'maxlen': 1}
                    ], 'minlen':1, 'maxlen':1, 'type':'con'},
               )


clm.print_rulelist()

