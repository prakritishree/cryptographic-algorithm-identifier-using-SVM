import pandas as pd

# Load the CSV file
df = pd.read_csv('hindi_english_parallel.csv')

# Drop the first column
df.drop(df.columns[0], axis=1, inplace=True)

# Save the changes back to the original file
df.to_csv('input.csv', index=False)
