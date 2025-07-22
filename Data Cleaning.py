import pandas as pd

# Load the dataset
df = pd.read_csv("Mall_Customers.csv.csv")

# Clean the data
df.columns = df.columns.str.lower().str.replace(" ", "_")
df.drop_duplicates(inplace=True)
df['gender'] = df['gender'].str.lower().str.strip()
df['age'] = df['age'].astype(int)

# Save cleaned data
df.to_csv("cleaned_dataset.csv", index=False)
print(" Cleaned data saved as 'cleaned_dataset.csv'")
