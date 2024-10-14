from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, Date, text
import csv
from datetime import datetime

# Create an engine and metadata
engine = create_engine('sqlite:///weather_data.db', echo=True)
meta = MetaData()

# Define the 'stations' table
stations = Table(
    'stations', meta,
    Column('station', String, primary_key=True),
    Column('latitude', Float),
    Column('longitude', Float),
    Column('elevation', Float),
    Column('name', String),
    Column('country', String),
    Column('state', String),
)

# Define the 'measurements' table
measurements = Table(
    'measurements', meta,
    Column('station', String),
    Column('date', Date),
    Column('precip', Float),
    Column('tobs', Integer),
)

# Create the tables in the database
meta.create_all(engine)

# Insert data from clean_stations.csv into the 'stations' table
with open('clean_stations.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    with engine.connect() as conn:
        for row in reader:
            # Ensure correct types for latitude, longitude, elevation
            ins = stations.insert().values(
                station=row['station'],
                latitude=float(row['latitude']),
                longitude=float(row['longitude']),
                elevation=float(row['elevation']),
                name=row['name'],
                country=row['country'],
                state=row['state']
            )
            conn.execute(ins)

# Insert data from clean_measure.csv into the 'measurements' table
with open('clean_measure.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    with engine.connect() as conn:
        for row in reader:
            # Ensure correct types for date, precip, and tobs
            ins = measurements.insert().values(
                station=row['station'],
                date=datetime.strptime(row['date'], '%Y-%m-%d').date(),  # Convert string to date
                precip=float(row['precip']) if row['precip'] else None,  # Handle possible nulls
                tobs=int(row['tobs']) if row['tobs'] else None  # Handle possible nulls
            )
            conn.execute(ins)

# Query the database using text() function
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM stations LIMIT 5")).fetchall()
    # Print the result
    for row in result:
        print(row)