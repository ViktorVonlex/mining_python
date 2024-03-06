import pandas as pd
import sys

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
    data.to_csv('Crimes_clean_2016.csv', index=False)

if filename.startswith("Beach"):

    # Drop these columns: maximum wind speed, heading, battery life,
    # Measurement Timestamp Label, Measurement ID
    data = data.drop(['Maximum Wind Speed', 'Heading', 'Battery Life', 
                    'Measurement Timestamp Label', 'Measurement ID'], axis=1)
    
    
    data = data.dropna()
    # Convert 'Measurement Timestamp' column to datetime
    data['Measurement Timestamp'] = pd.to_datetime(data['Measurement Timestamp'])

    # Splitting 'Measurement Timestamp' into 'Date' and 'Time' columns
    data['Date'] = data['Measurement Timestamp'].dt.date
    data['Time'] = data['Measurement Timestamp'].dt.time
    data.to_csv('Weather_clean.csv', index=False)
