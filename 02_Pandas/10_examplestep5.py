import pandas as pd

data = {
    "Name":['Ram','Manish','Samir','Kaya','Suresh','Vansh','Utsav','Jeet'],
    "Age": [28,34,24,40,36,25,20,27],
    "Salary":[50000,60000,45000,35000,70000,80000,48000,52000],
    "Performance Score":[85,90,70,92,88,71,89,87]
}

df = pd.DataFrame(data)

#Display the DataFrame
print("Smaple DatFrame")
print(df)

print("Name(Single Columns Return sries)")
name = df["Name"]
print(name)

#Silecting mltiple columns
subset = df[["Name","Salary"]]
print("\nSubset with Name and Salary")
print(subset)