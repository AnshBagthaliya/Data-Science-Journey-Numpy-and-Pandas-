import pandas as pd

# Customer Profile DataFrame
customer_df = pd.DataFrame({
    'customer_id': [101, 102, 103],
    'customer_name': ['Alice', 'Bob', 'Charlie']
})

# Transaction History DataFrame
transaction_df = pd.DataFrame({
    'customer_id': [101, 102, 104],
    'transaction_amount': [250, 150, 300]
})

# 1. Merge based on customer_id
merged_df = pd.merge(customer_df, transaction_df, on='customer_id', how='inner')
print("Merged DataFrame:")
print(merged_df)

# 2. Add a new customer record using concat
new_customer = pd.DataFrame({
    'customer_id': [105],
    'customer_name': ['David']
})

updated_customer_df = pd.concat([customer_df, new_customer], ignore_index=True)
print("\nUpdated Customer DataFrame after adding new record:")
print(updated_customer_df)
