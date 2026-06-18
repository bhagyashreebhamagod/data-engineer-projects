import pandas as pd

# EXTRACT
df = pd.read_csv("raw_sales.csv")

# TRANSFORM
df = df.dropna()
df.columns = df.columns.str.lower()

# LOAD
df.to_csv("cleaned_sales.csv", index=False)

print("ETL pipeline executed successfully")
