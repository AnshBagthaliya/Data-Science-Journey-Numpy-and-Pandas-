import pandas as pd

data = {
    "Name":['Ram','Manish','Samir','Kaya','Suresh','Vansh','Utsav','Jeet'],
    "Age": [28,34,24,40,36,25,20,27],
    "Salary":[50000,60000,45000,35000,70000,80000,48000,52000],
    "Performance Score":[85,90,70,92,88,71,89,87]
}

df = pd.DataFrame(data)
print(df)

# square Brakecets df("Column_Name") = some_data
df["Bonus"] = df["Salary"] * 0.1
print(df)

# Using Insert()
#df.insert(location,"Column_Name",some_data)

df.insert(0,"Employee ID",[10,20,30,40,50,60,70,80])
print(df)