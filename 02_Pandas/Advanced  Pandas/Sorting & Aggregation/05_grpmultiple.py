import pandas as pd

data = {
    "Name":["Ansh","Priya","Vansh","Param","Yasvi"],
    "Age": [22,28,25,28,22,],
    "Salary":[50000,60000,45000,52000,48000]
}

df = pd.DataFrame(data)
grouped = df.groupby(["Age","Name"])["Salary"].sum()
print(grouped)