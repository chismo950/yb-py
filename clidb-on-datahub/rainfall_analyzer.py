import pandas as pd
import os

class RainfallAnalyzer:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = pd.read_csv(csv_path)

    def data_preview(self):
        # print first 5 rows
        return self.df.head(5)
    
    def data_info(self):
        # print the info of data frame, include colunm names, nun-empty data amount, data type, etc
        return self.df.info()

    def rainfall_statistics(self):
        # calc the amount, average, std, etc of RAINFALL10 column data
        return self.df['RAINFALL10'].describe()

    def rainfall_by_date(self):
        rainfall_by_date = {}
        # .iterrows returns index and row, we only need row, so use _ to be a placeholder
        for _, row in self.df.iterrows():
            # use to_datetime to convert date string to Timestamp, use .date to get year, month and day, omit the hour, minute and second
            date = pd.to_datetime(row['OBS_DATE']).date()
            # .get(date, 0) means get value by key(date), if not found, return 0
            rainfall_by_date[date] = rainfall_by_date.get(date, 0) + row['RAINFALL10']
        return rainfall_by_date

def main():
    BASE_DIR = os.path.dirname(__file__)
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