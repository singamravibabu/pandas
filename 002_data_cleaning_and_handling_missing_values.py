# Data Cleaning and Handling Missing Values

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