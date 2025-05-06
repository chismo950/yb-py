import pandas as pd
import os
from rainfall_analyzer import RainfallAnalyzer

def main():
    BASE_DIR = os.path.dirname(__file__)
    # the csv is downloaded from https://data.niwa.co.nz
    csv_path = os.path.join(BASE_DIR, '12430_rain.csv')
    rainfall_analyzer = RainfallAnalyzer(csv_path)

    print("Data preview:")
    print(rainfall_analyzer.data_preview())

    print("\nData info:")
    print(rainfall_analyzer.data_info())

    print("\nRainfall statistics:")
    print(rainfall_analyzer.rainfall_statistics())

    print("\nTotal rainfall by date:")
    # .items() will return date, total, the total is value of the key(date)
    for date, total in rainfall_analyzer.rainfall_by_date().items():
        print(f"{date}: {total}")

if __name__ == "__main__":
    main()