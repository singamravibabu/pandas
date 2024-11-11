# pandas Tutorial

> This guide covers the pandas library in Python, from the basics to intermediate functionalities.

**Table of Contents**
1. [Introduction to pandas](#introduction-to-pandas)
2. [Installing pandas](#installing-pandas)
3. [Importing pandas](#importing-pandas)
4. [Creating Series](#creating-series)
5. [Creating DataFrame](#creating-dataframe)
6. [Reading Data from CSV](#reading-data-from-csv)
7. [Data Exploration](#data-exploration)
8. [Data Cleaning](#data-cleaning)
9. [Data Manipulation](#data-manipulation)
10. [Data Visualization](#data-visualization)

## Introduction to pandas
**pandas** is a powerful open-source data analysis and manipulation library for Python. It provides data structures like Series and DataFrame to work with structured data easily.

**Key Features:**
- Data alignment and handling of missing data.
- Label-based slicing, indexing, and subsetting.
- Data merging and joining.
- Time series functionality.

## Installing pandas
To install pandas, use the following command:

```bash
pip install pandas
```

You can also update pandas to the latest version using:

```bash
pip install --upgrade pandas
```

## Importing pandas
Start by importing the pandas library:

```python
import pandas as pd
```

## Creating Series
A Series is a one-dimensional array-like object that can hold any data type.

**Example:**
```python
import pandas as pd

# Creating a Series
data = [10, 20, 30, 40]
s = pd.Series(data)
print(s)
```

**Output:**
```go
0    10
1    20
2    30
3    40
dtype: int64
```

### Adding Labels:
```python
s = pd.Series(data, index=['a', 'b', 'c', 'd'])
print(s)
```

**Output:**
```css
a    10
b    20
c    30
d    40
dtype: int64
```

## Creating DataFrame
A DataFrame is a two-dimensional, size-mutable, and heterogeneous tabular data structure with labeled axes.

**Example:**
```python
# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}
df = pd.DataFrame(data)
print(df)
```

Output:

```markdown
      Name  Age           City
0    Alice   25      New York
1      Bob   30  San Francisco
2  Charlie   35   Los Angeles
```

## Reading Data from CSV
You can easily read data from CSV files using pandas.read_csv().

**Example:**
```python
# Reading a CSV file
df = pd.read_csv('data.csv')
print(df.head())
```

## Data Exploration
Let's explore some common methods to understand the data:

### 1. Display the first few rows:

```python
print(df.head(5))  # First 5 rows
```

### 2. Get basic information:

```python
print(df.info())
```

### 3. Get summary statistics:

```python
print(df.describe())
```

### 4. Check for missing values:

```python
print(df.isnull().sum())
```

## Data Cleaning

### 1. Handling Missing Values

```python
# Fill missing values with the mean
df['column_name'].fillna(df['column_name'].mean(), inplace=True)

# Drop rows with any missing values
df.dropna(inplace=True)
```

### 2. Renaming Columns

```python
df.rename(columns={'OldName': 'NewName'}, inplace=True)
```

### 3. Changing Data Types

```python
df['column_name'] = df['column_name'].astype('float')
```

## Data Manipulation

### 1. Filtering Data

```python
# Filter rows where Age > 30
filtered_df = df[df['Age'] > 30]
print(filtered_df)
```

### 2. Sorting Data

```python
# Sort by Age in descending order
df.sort_values(by='Age', ascending=False, inplace=True)
```

### 3. Grouping Data

```python
# Group by 'City' and calculate the mean Age
grouped = df.groupby('City')['Age'].mean()
print(grouped)
```

## Data Visualization
To visualize data, you can use the built-in plotting functionality in pandas, which is based on Matplotlib.

**Example:**
```python
import matplotlib.pyplot as plt

# Plot a bar chart of Ages
df['Age'].plot(kind='bar')
plt.title('Age Distribution')
plt.xlabel('Index')
plt.ylabel('Age')
plt.show()
```