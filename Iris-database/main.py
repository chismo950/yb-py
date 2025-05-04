from ucimlrepo import fetch_ucirepo

def main():
    # fetch Iris dataset from UCI ML Repository
    # ID 53 = Iris dataset
    # Other datasets have different IDs (e.g., Wine = 109)
    iris = fetch_ucirepo(id=53) 

    # get the target labels
    y = iris.data.targets

    print("name of flowers in the Iris dataset:")

    # .iloc is a pandas method that stands for “integer-location based indexing”. It’s used to select data from a DataFrame or Series by position, not by label
    # select all rows (:) from the first column (0)
    print(y.iloc[:, 0].unique())


# used to check if the Python file is being run directly (not imported as a module in another script). If true, the code inside this block will execute
# It allows the file to be both run as a script and imported as a module without running the script code on import
# It improves code modularity and maintainability
if __name__ == "__main__":
    main()