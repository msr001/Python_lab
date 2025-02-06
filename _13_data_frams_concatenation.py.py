import pandas as pd

def concatenate_dataframes():
    # Creating first DataFrame
    data1 = {
        'ID': [1, 2, 3],
        'Name': ['Alice', 'Bob', 'Charlie']
        }
    df1 = pd.DataFrame(data1)
    
    # Creating second DataFrame
    data2 = {'ID': [4, 5, 6], 'Name': ['David', 'Eve', 'Frank']}
    df2 = pd.DataFrame(data2)
    
    # Concatenating DataFrames
    result = pd.concat([df1, df2], ignore_index=True)
    
    # Print the concatenated DataFrame
    print("Concatenated DataFrame:")
    print(result)

# Example usage
concatenate_dataframes()
