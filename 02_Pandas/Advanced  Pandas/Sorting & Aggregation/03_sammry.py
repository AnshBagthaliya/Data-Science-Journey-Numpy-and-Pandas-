'''df["ColumnName"].mean()
   df["ColumnName"].sum()
   df["ColumnName"].min()
   df["ColumnName"].max()'''

import pandas as pd

data = {
    "Name":["Ansh","Vansh","Kans"],
    "Age":[22,34,26],
    "Salary":[10000,20000,30000]
}

df = pd.DataFrame(data)

avg = df['Salary'].mean()
print(avg)