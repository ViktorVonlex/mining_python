import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Merged_data.csv')

# WEATHER
# ----------------------------

# Temperature Category
data['Temperature Category'] = pd.Categorical(data['Temperature Category'], categories=['low', 'medium', 'high'], ordered=True)

data['Temperature Category'].value_counts().sort_index().plot(kind='bar')
plt.title("Temperature Category")
plt.xlabel("Temperature")
plt.xticks(rotation=0)
plt.ylabel("Frequency")
plt.show()

# Humidity Category
data['Humidity Category'] = pd.Categorical(data['Humidity Category'], categories=['low', 'medium', 'high'], ordered=True)

data['Humidity Category'].value_counts().sort_index().plot(kind='bar')
plt.title("Humidity Category")
plt.xlabel("Humidity")
plt.xticks(rotation=0)
plt.ylabel("Frequency")
plt.show()

# Wind Speed Category

data['Wind Speed Category'].value_counts().sort_index().plot(kind='bar')
plt.title("Wind Speed Category")
plt.xlabel("Wind Speed")
plt.xticks(rotation=0)
plt.ylabel("Frequency")
plt.show()

# Pressure Category
data['Pressure Category'] = pd.Categorical(data['Pressure Category'], categories=['low', 'medium', 'high'], ordered=True)

data['Pressure Category'].value_counts().sort_index().plot(kind='bar')
plt.title("Pressure Category")
plt.xlabel("Pressure")
plt.xticks(rotation=0)
plt.ylabel("Frequency")
plt.ylim([0, 90000])  # Set y-axis limits
plt.show()

# Solar Radiation Category
data['Solar Radiation Category'] = pd.Categorical(data['Solar Radiation Category'], categories=['low', 'medium', 'high'], ordered=True)

data['Solar Radiation Category'].value_counts().sort_index().plot(kind='bar')
plt.title("Solar Radiation Category")
plt.xlabel("Solar Radiation")
plt.xticks(rotation=0)
plt.ylabel("Frequency")
plt.show()

# Rain Category
data['Rain Category'] = pd.Categorical(data['Rain Category'], categories=['none', 'light', 'moderate', 'heavy', 'very heavy'], ordered=True)

data['Rain Category'].value_counts().sort_index().plot(kind='bar')
plt.title("Rain Category")
plt.xlabel("Rain Intensity")
plt.xticks(rotation=0)
plt.ylabel("Frequency")
plt.show()

# Wind Direction Category
data['Wind Direction Category'] = pd.Categorical(data['Wind Direction Category'], categories=['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'], ordered=True)

data['Wind Direction Category'].value_counts().sort_index().plot(kind='bar')
plt.title("Wind Direction Category")
plt.xlabel("Wind Direction")
plt.xticks(rotation=0)
plt.ylabel("Frequency")
plt.show()

# CRIME
# ----------------------------
# Area Category
data['Area Category'] = pd.Categorical(data['Area Category'], categories=['Central', 'Far North Side', 'Far Southeast Side', 'Far Southwest Side', 'North Side', ' Northwest Side', 'South Side', 'Southwest Side', 'West Side'], ordered=True)

data['Area Category'].value_counts().sort_index().plot(kind='bar')
plt.title("Area Category")
plt.xlabel("Area")
plt.xticks(rotation=90)
plt.ylabel("Frequency")
plt.show()

# Primary Type
# data['Primary Type'] = pd.Categorical(data['Primary Type'], categories=['BATTERY', 'THEFT', 'CRIMINAL DAMAGE', 'NARCOTICS', 'ASSAULT', 'OTHER OFFENSE', 'BURGLARY', 'MOTOR VEHICLE THEFT', 'DECEPTIVE PRACTICE', 'ROBBERY'], ordered=True)

data['Primary Type'].value_counts().sort_index().plot(kind='bar')
plt.title("Primary Type")
plt.xlabel("Type")
plt.xticks(rotation=90)
plt.ylabel("Frequency")
plt.show()

# Arrest 
data['Arrest'] = pd.Categorical(data['Arrest'], categories=[True, False], ordered=True)

data['Arrest'].value_counts().sort_index().plot(kind='bar')
plt.title("Arrest")
plt.xlabel("Arrest")
plt.xticks(rotation=0)
plt.ylabel("Frequency")
plt.show()

# Domestic
data['Domestic'] = pd.Categorical(data['Domestic'], categories=[True, False], ordered=True)

data['Domestic'].value_counts().sort_index().plot(kind='bar')
plt.title("Domestic")
plt.xlabel("Domestic")
plt.xticks(rotation=0)
plt.ylabel("Frequency")
plt.show()

# Time Category
data['Time Category'] = pd.Categorical(data['Time Category'], categories=['Morning', 'Forenoon', 'Afternoon', 'Evening', 'Night', ], ordered=True)

data['Time Category'].value_counts().sort_index().plot(kind='bar')
plt.title("Time Category")
plt.xlabel("Time")
plt.xticks(rotation=0)
plt.ylabel("Frequency")
plt.show()
