import pandas as pd
import os
import time

BASE_DIR = os.path.dirname(__file__)

def main():
    start_time = time.time()
    df = pd.read_parquet(os.path.join(BASE_DIR, "Sample-1m.parquet"))
    end_time = time.time()
    time_loading_file = end_time - start_time
    print(f"time to load big file: {time_loading_file} seconds")
    num_records = len(df)
    print("records amount: ", num_records)

if __name__ == "__main__":
    main()