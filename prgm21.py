import pandas as pd
data = {'Name': ['John', 'Alice', 'Bob', 'Eve'],
        'City': ['New York', 'Los Angeles', 'Chicago', 'San Francisco']}
df = pd.DataFrame(data)
column_to_swap = 'Name'
df[column_to_swap] = df[column_to_swap].str.swapcase()
print(df)
