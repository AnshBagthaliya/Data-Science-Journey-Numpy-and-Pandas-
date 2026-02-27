import pandas as pd

data = {
    "Name":['Ram','Manish','Samir','Kaya','Suresh','Vansh','Utsav','Jeet'],
    "Age": [28,34,24,40,36,25,20,27],
    "Salary":[50000,60000,45000,35000,70000,80000,48000,52000],
    "Performance Score":[85,90,70,92,88,71,89,87]
}

df = pd.DataFrame(data)

# Single Condition
high_salary = df[df["Salary"] > 50000]
print("Employees with salary > 50000")
print(high_salary)

# Filterings rows salary >50k & age >30
# Multiple Condition

filtered = df[(df["Age"] > 30) & (df["Salary"]  > 50000 )]
print(" Employe list Age>30 & Salary>50000")
print(filtered)

# Using OR Condition (Any One Condition True)
filtered_or = df[(df["Age"] > 30) | (df["Performance Score"]  > 90)]
print("Employees with age > 35 or Performance Score > 90")
print(filtered_or)