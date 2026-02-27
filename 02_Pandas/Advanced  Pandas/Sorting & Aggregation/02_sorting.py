#sorting datas
# Sorting in 1 column sort_value()
# df.sort_values (by="ColumnName",True/False,inplace = True)

import pandas as pd

data = {
    "Name":["Ansh","Vansh","Kans"],
    "Age":[22,34,26],
    "Salary":[70000,48000,60000]
}

df = pd.DataFrame(data)

# df.sort_values(by="Age",ascending=False,inplace=True)
df.sort_values(by=["Age","Salary"],ascending=[True,False],inplace=True)

print("Sorted Age by Descending")
print(df)