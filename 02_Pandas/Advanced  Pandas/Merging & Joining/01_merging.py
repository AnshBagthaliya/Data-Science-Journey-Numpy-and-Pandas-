#pd.merge(df1,df2, on=("Column_Name", how="type of join"))
import pandas as pd

df_Customers = pd.DataFrame({
    "CustomerID":[1,2,3],
    "Name":["Ramesh","Suresh","Kalpesh"]
})

#order dataframe

df_Orders = pd.DataFrame({
    "CustomerID":[1,2,4],
    "OrderAmount":[250,450,350]
})

#merge
df_merged = pd.merge(df_Customers,df_Orders, on="CustomerID", how="right")
print("right join")
print(df_merged)

'''
cross join:
1df = m rows
2df = n rows
m * n

🔹1. Inner Join
Definition: Returns only the rows that have matching values in both DataFrames.

🔹2. Left Join
Definition: Returns all rows from the left DataFrame and matching rows from the right DataFrame. Non-matching rows from the right will have NaN.

🔹3. Right Join
Definition: Returns all rows from the right DataFrame and matching rows from the left DataFrame. Non-matching rows from the left will have NaN.

🔹4. Outer Join (Full Outer Join)
Definition: Returns all rows from both DataFrames. Missing values are filled with NaN.

🔹5. Cross Join (Cartesian Product)
Definition: Returns the Cartesian product of both DataFrames – every row of df1 is paired with every row of df2.

'''