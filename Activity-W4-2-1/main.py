import os
import pandas as pd

baseDir = os.path.dirname(os.path.abspath(__file__))

# 1- load the text file and find the number of __ in the txt file
txtPath = baseDir + "/sample_text.txt"
txtFile = open(txtPath)
txtContent = txtFile.read()
numOfDoubleUnderScore = txtContent.count("__")
print('numOfDoubleUnderScore: ', numOfDoubleUnderScore)

# 2- load the parquet file and print out the number of features
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
parquetPath = baseDir + "/Sample_data_2.parquet"
df = pd.read_parquet(parquetPath)
num_features = len(df.columns)
# print(df.head()) # print all columns
print("num_features: ", num_features)