import pandas as pd

# Load raw data
df = pd.read_csv("raw_sales.csv")

# Remove null values
df = df.dropna()

# Convert column names to lowercase
df.columns = df.columns.str.lower()

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned data
df.to_csv("cleaned_sales.csv", index=False)

print("Data cleaning completed successfully!")
