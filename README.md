# pandas Tutorial

> This guide covers the pandas library in Python, from the basics to intermediate functionalities.

**Table of Contents**
1. [Introduction to pandas](#introduction-to-pandas)
2. Installing pandas
3. Importing pandas
4. Creating Series
5. Creating DataFrame
6. Reading Data from CSV
7. Data Exploration
8. Data Cleaning
9. Data Manipulation
10. Data Visualization

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