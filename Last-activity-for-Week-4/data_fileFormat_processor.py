import pandas as pd
import math

class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self.value = float(input("Please input a number to calc sin/cos: "))
        self.diameter = float(input("Please input a diameter to calc area of circle: "))

    def load_data(self):
        if self.file_path.endswith('.csv'):
            self.data = pd.read_csv(self.file_path)
        elif self.file_path.endswith('.parquet'):
            self.data = pd.read_parquet(self.file_path)
        else:
            raise ValueError("Unsupported file format. Please use CSV or Parquet.")
        print(f"Data loaded successfully from {self.file_path}")

    def initial_processing(self):
        if self.data is None:
            raise ValueError("No data loaded.")
        
        print("Initial Data Summary:")
        print(self.data.info())
        print("\nMissing Values:")
        print(self.data.isnull().sum())
        print("\nDescriptive Statistics:")
        print(self.data.describe())
    
    def sin(self):
        print("sin of", self.value, ": ", math.sin(self.value))
    
    def cos(self):
        print("cos of ", self.value, ": ", math.cos(self.value))
    
    def diameterOfCircle(self):
        radius = self.diameter / 2
        area = math.pi * radius ** 2
        print(f"circle area for diameter {self.diameter} is: ", area)

def main():
    # Replace the file path below with your actual file path
    file_path = 'your_data_file.csv'  # or 'your_data_file.parquet'
    processor = DataProcessor(file_path)
    processor.load_data()
    processor.initial_processing()
    processor.sin()
    processor.cos()

if __name__ == "__main__":
    main()
