# Weather Data Manager

The Weather Data Manager is designed to store and handle weather data, specifically station information and measurement records. It manages two main tables in a SQLite database: stations and measurements.

## Features

- Stations Management: Stores and manages information about weather stations, including details such as latitude, longitude, elevation, name, country, and state.
- Measurements Management: Records daily weather measurements, including precipitation and temperature observations.
- Data Ingestion: Imports data from CSV files (clean_stations.csv and clean_measure.csv) into the database.
- Data Retrieval: Executes SQL queries to fetch and display stored station information.

## Installation

Clone this repository to your local machine:
    `git clone https://github.com/andy111223/06.3_ORM-SQLAlchemy`

Navigate to the project directory:
    `cd 06.3_ORM-SQLAlchemy`

Install the required dependencies (if not already installed):
    `pip install sqlalchemy`

Run the script:
    `python3 main.py`

## Usage

1. Ensure that the CSV files (clean_stations.csv and clean_measure.csv) are present in the project directory.
2. The script will create a SQLite database named weather_data.db and populate it with data from the CSV files.
3. After execution, it will display the records from the stations table.

## Requirements

- Python 3 (tested on Python 3.12)
- SQLAlchemy library