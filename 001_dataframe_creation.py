# DataFrame Creation & Optimization
import pandas as pd
import numpy as np

# Create DataFrames using different methods
df_list = pd.DataFrame([[1, 2], [3, 4]], columns=['A', 'B'])
df_dict = pd.DataFrame({'A': [1, 3], 'B': [2, 4]})
df_array = pd.DataFrame(np.array([[5, 6], [7, 8]]), columns=['A', 'B'])

# Check memory usage
print(df_list.info())
print(df_dict.info())
print(df_array.info())

# Convert data types to optimize memory usage
df_optimized = df_dict.astype({'A': 'int8', 'B': 'int8'})
print(df_optimized.info())