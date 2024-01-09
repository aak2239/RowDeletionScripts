import pandas as pd

# Load the CSV file
file_path = '/Users/abdkahhaleh/Downloads/Generated_Conversions5.csv'
df = pd.read_csv(file_path)

# Filter out the rows where the last column equals '""=1.0/1.0"'
df = df[df.iloc[:, -1] != '=1.0/1.0']

# Save the filtered DataFrame back to the same CSV file
df.to_csv(file_path, index=False)

print("Rows where the Conversion Formula was '=1.0/1.0' have been removed.")
