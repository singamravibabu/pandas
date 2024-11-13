# 10 Pandas Activities

### Activity 1: DataFrame Creation & Optimization

```python
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
```

### Activity 2: Data Cleaning & Handling Missing Values

```python
# Load dataset
df = pd.DataFrame({'Name': ['Alice', 'Bob', None], 'Age': [25, None, 30]})

# Identify missing data
print(df.isnull())

# Fill missing values
df_filled = df.fillna({'Name': 'Unknown', 'Age': df['Age'].mean()})
print(df_filled)

# Drop rows with missing values
df_dropped = df.dropna()
print(df_dropped)
```

### Activity 3: Data Selection & Filtering

```python
# Create sample DataFrame
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'David'],
                   'Age': [23, 35, 45, 29],
                   'City': ['NY', 'LA', 'NY', 'SF']})

# Selection using .loc[]
print(df.loc[df['City'] == 'NY'])

# Filtering using multiple conditions
print(df[(df['Age'] > 30) & (df['City'] == 'NY')])
```

### Activity 4: Vectorization & Avoiding Loops

```python
# Using loops (inefficient)
df = pd.DataFrame({'Value': range(1, 1000001)})
squares_loop = []
for i in df['Value']:
    squares_loop.append(i**2)
df['Squares_Loop'] = squares_loop

# Using vectorized operations (efficient)
df['Squares_Vectorized'] = df['Value'] ** 2

# Performance comparison
%timeit df['Value'] ** 2
```

### Activity 5: Data Aggregation & Grouping

```python
df = pd.DataFrame({'Region': ['North', 'South', 'North', 'West'],
                   'Sales': [200, 150, 400, 300]})

# Grouping data
grouped = df.groupby('Region').agg({'Sales': 'sum'})
print(grouped)

# Using pivot table
pivot_table = df.pivot_table(values='Sales', index='Region', aggfunc='sum')
print(pivot_table)
```

### Activity 6: Handling Large Datasets

```python
# Simulate large dataset
large_df = pd.DataFrame(np.random.randn(1000000, 5), columns=list('ABCDE'))

# Read dataset in chunks
chunk_iter = pd.read_csv('large_file.csv', chunksize=10000)

total_sum = 0
for chunk in chunk_iter:
    total_sum += chunk['Sales'].sum()
print(total_sum)
```

### Activity 7: Merging & Joining DataFrames

```python
# Create DataFrames
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Score': [90, 80, 85]})

# Merge DataFrames
merged_df = pd.merge(df1, df2, on='ID', how='inner')
print(merged_df)

# Join DataFrames
df1.set_index('ID', inplace=True)
df2.set_index('ID', inplace=True)
joined_df = df1.join(df2, how='outer')
print(joined_df)
```

### Activity 8: Data Visualization with Pandas

```python
import matplotlib.pyplot as plt

# Sample Data
df = pd.DataFrame({'Category': ['A', 'B', 'C', 'D'], 'Values': [4, 7, 1, 8]})

# Line Plot
df.plot(kind='line', x='Category', y='Values')
plt.title('Line Plot Example')
plt.show()

# Bar Plot
df.plot(kind='bar', x='Category', y='Values')
plt.title('Bar Plot Example')
plt.show()
```

### Activity 9: Using apply() vs. np.where() for Conditional Updates

```python
# Sample DataFrame
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 35, 45]})

# Using apply
df['Category'] = df['Age'].apply(lambda x: 'Senior' if x > 30 else 'Junior')

# Using np.where
df['Category_np'] = np.where(df['Age'] > 30, 'Senior', 'Junior')
print(df)
```

### Activity 10: Creating Efficient Pandas Pipelines

```python
# Method chaining example
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'David'],
                   'Age': [23, 35, 45, 29],
                   'City': ['NY', 'LA', 'NY', 'SF']})

result = (df.query('Age > 25')
            .groupby('City')
            .agg({'Age': 'mean'})
            .reset_index()
            .rename(columns={'Age': 'Avg_Age'}))
print(result)
```

### Activity 11: Exploring Pandas with Profiling Tools

```python
# Install pandas_profiling first: pip install pandas-profiling
from pandas_profiling import ProfileReport

# Sample Data
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, None, 6], 'C': ['foo', 'bar', 'baz']})

# Generate profiling report
profile = ProfileReport(df)
profile.to_file("output_report.html")
```