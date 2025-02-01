import pandas as pd

# Create a DataFrame
data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'C', 'C', 'B', 'C'],
    'Values': [10, 20, 30, 40, 50, 60, 70, 80, 90]
}
df = pd.DataFrame(data)

# Group by 'Category' and compute the sum
grouped_df = df.groupby('Category').sum()

# Print the result
print(grouped_df)
