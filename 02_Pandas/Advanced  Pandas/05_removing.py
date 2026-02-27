import pandas as pd

data = {
    "Name":['Ram','Manish','Samir','Kaya','Suresh','Vansh','Utsav','Jeet'],
    "Age": [28,34,24,40,36,25,20,27],
    "Salary":[50000,60000,45000,35000,70000,80000,48000,52000],
    "Performance Score":[85,90,70,92,88,71,89,87]
}

df = pd.DataFrame(data)
print(df)

# df.drop(columns = ["ColumnName"],inplace=True)
print("Modified Data")
df.drop(columns = ["Performance Score"], inplace=True)
# df.drop(columns = ["Performance Score","Age"], inplace=True)
print(df)