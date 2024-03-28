import pandas as pd
import sys
import numpy as np

filename = sys.argv[1]

data = pd.read_csv(filename)

if filename.startswith("Crimes"):

    # Drop these columns: ID, case Number, IUCR, Beat, Disctrict, Ward, FBI Code,
    # X Coor, Y Coor, Updated on, Latitude, Longtitude, Location, year
    data = data.drop(['ID', 'Case Number', 'IUCR', 'Beat', 'District', 
                    'Ward', 'FBI Code', 'X Coordinate', 'Y Coordinate',
                    'Updated On', 'Latitude', 'Longitude', 'Location',
                    "Year"], axis=1)
    data = data.dropna()
    data['Date'] = pd.to_datetime(data['Date'])
    data['Time'] = data['Date'].dt.time
    data['Date'] = data['Date'].dt.date

    # Categorize 'Time' into 'Morning' 05:01-09:00, 'Forenoon': 09:01-12:00, 'Afternoon': 12:01-18:00, 'Evening': 18:01-00:00, 'Night': 00:01-05:00
    # Extract hour from time
    data['Hour'] = data['Time'].apply(lambda x: x.hour)

    # Define bins and labels for categorization
    bins = [0, 5, 9, 12, 18, 24]
    labels = ['Night', 'Morning', 'Forenoon', 'Afternoon', 'Evening']

    # Categorize time based on hour
    data['Time Category'] = pd.cut(data['Hour'], bins=bins, labels=labels, right=False)

    # Add column 'Day' to categorize the day of the week
    data['Day'] = data['Date'].apply(lambda x: x.weekday())

    # Map the day of the week to the actual day
    days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    data['Day'] = data['Day'].map(days)

    area_categories = {
        "Central": [8, 32, 33],
        "Far North Side": [1, 2, 3, 4, 9, 10, 11, 12, 13, 14, 76, 77],
        "Far Southeast Side": list(range(44, 56)),
        "Far Southwest Side": list(range(70, 76)),
        "North Side": [5, 6, 7, 21, 22],
        "Northwest Side": list(range(15, 21)),
        "South Side": list(range(34, 44)) + [60, 69],
        "Southwest Side": list(range(56, 60)) + list(range(61, 69)),
        "West Side": list(range(23, 32)),
    }

    data['Area Category'] = data['Community Area'].apply(lambda x: next((k for k, v in area_categories.items() if x in v), None))

    data.to_csv('Crimes_clean_2016.csv', index=False)

if filename.startswith("Beach"):

    # Drop these columns: maximum wind speed, heading, battery life,
    # Measurement Timestamp Label, Measurement ID
    data = data.drop(['Maximum Wind Speed', 'Heading', 'Battery Life', 
                    'Measurement Timestamp Label', 'Measurement ID'], axis=1)
    
    # Drop rows that begin with 63rd in column "station name"
    data = data[~data['Station Name'].str.startswith('63rd')]
    
    data = data.dropna()
    # Convert 'Measurement Timestamp' column to datetime
    data['Measurement Timestamp'] = pd.to_datetime(data['Measurement Timestamp'])

    # Splitting 'Measurement Timestamp' into 'Date' and 'Time' columns
    data['Date'] = data['Measurement Timestamp'].dt.date
    data['Time'] = data['Measurement Timestamp'].dt.time
    data = data.drop(['Measurement Timestamp'], axis=1)

    data = data.drop(['Interval Rain'], axis=1)

    # Drop rows where 'Station' isn't equal to 'Oak Street Weather Station'
    data = data[data['Station Name'] == 'Oak Street Weather Station']

    # Drop column 'Station Name'
    data = data.drop(['Station Name'], axis=1)

    # Drop column 'Wet Bulb Temperature'
    data = data.drop(['Wet Bulb Temperature'], axis=1)

    # Categorize 'Time' into 'Morning' 05:01-09:00, 'Forenoon': 09:01-12:00, 
    # 'Afternoon': 12:01-18:00, 'Evening': 18:01-00:00, 'Night': 00:01-05:00

    # Extract hour from time
    data['Hour'] = data['Time'].apply(lambda x: x.hour)

    # Define bins and labels for categorization
    bins = [0, 5, 9, 12, 18, 24]
    labels = ['Night', 'Morning', 'Forenoon', 'Afternoon', 'Evening']

    # Categorize time based on hour
    data['Time Category'] = pd.cut(data['Hour'], bins=bins, labels=labels, right=False)

    # Drop rows that don't contain 2016 as years in column "Date"
    data = data[data['Date'].astype(str).str.contains('2016')]

    # Categorize 'Air Temperature' into 5 bins: "very low", "low", "medium", "high", "very high"
    data['Temperature Category'] = pd.qcut(data['Air Temperature'], 5, labels=["very low", "low", "medium", "high", "very high"])

    # Categorize 'humidity' into 3 bins: "low", "medium", "high"
    data['Humidity Category'] = pd.qcut(data['Humidity'], 3, labels=["low", "medium", "high"])

    # Categorize 'Wind Speed' into bins based on the Beaufort scale
    bins = [0, 1, 3, 6, 10, 15, 20, 26, 33, 40, 47, 55, 63, np.inf]
    labels = ["Calm", "Light Air", "Light Breeze", "Gentle Breeze", "Moderate Breeze", "Fresh Breeze", "Strong Breeze", "High Wind", "Gale", "Strong Gale", "Storm", "Violent Storm", "Hurricane"]
    data['Wind Speed Category'] = pd.cut(data['Wind Speed'], bins=bins, labels=labels, right=False)

    # Categorize 'Barometric Pressure' into 3 bins: "low", "medium", "high"
    data['Pressure Category'] = pd.qcut(data['Barometric Pressure'], 3, labels=["low", "medium", "high"])

    # Categorize 'Solar Radiation' into 3 bins: "low", "medium", "high"
    data['Solar Radiation Category'] = pd.qcut(data['Solar Radiation'], 3, labels=["low", "medium", "high"])

    # Categorize 'Rain Intensity' into 5 bins: "none", "light", "moderate", "heavy", "very heavy"
    bins = [0, 0.1, 1, 5, 10, np.inf]
    labels = ["none", "light", "moderate", "heavy", "very heavy"]
    data['Rain Category'] = pd.cut(data['Rain Intensity'], bins=bins, labels=labels, right=False)

    # Categorize 'Total Rain' into 6 bins: "No rain", "Light", "Moderate", "Heavy", "Very heavy", "Extremely heavy"
    bins = [0, 1, 10, 30, 70, 150, np.inf]
    labels = ["No rain", "Light", "Moderate", "Heavy", "Very heavy", "Extremely heavy"]
    data['TotalRain Category'] = pd.cut(data['Total Rain'], bins=bins, labels=labels, right=False)

    # Wind direction categories
    wind_direction = {
        "N": list(range(0, 23)) + list(range(338, 361)),
        "NE": list(range(23, 68)),
        "E": list(range(68, 113)),
        "SE": list(range(113, 158)),
        "S": list(range(158, 203)),
        "SW": list(range(203, 248)),
        "W": list(range(248, 293)),
        "NW": list(range(293, 338))
    }

    data['Wind Direction Category'] = data['Wind Direction'].apply(lambda x: next((k for k, v in wind_direction.items() if x in v), None))

    data.to_csv('Weather_clean.csv', index=False)
