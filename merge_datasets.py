import pandas as pd

# Load the datasets

data1 = pd.read_csv('Crimes_clean_2016.csv')
data2 = pd.read_csv('Weather_clean.csv')

data2 = data2.drop(['Time'], axis=1)
data2 = data2.drop(['Time Category'], axis=1)

# Merge the datasets on 'Date' and 'Time'
result = pd.merge(data1, data2, on=['Date', 'Hour'])

# Save the merged dataset
result.to_csv('Merged_data.csv', index=False)