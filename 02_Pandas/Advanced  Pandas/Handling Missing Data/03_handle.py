# remove
#dropna()

# df.dropna(axis = 0, inplace = True)
import pandas as pd

data = {
    "Name":['Ram',None,'Samir','Kaya','Suresh','Vansh','Utsav','Jeet'],
    "Age": [28,None,24,40,36,25,20,27],
    "Salary":[50000,None,45000,35000,70000,80000,48000,52000],
    "Performance Score":[85,None,70,92,88,71,89,87]
}

df = pd.DataFrame(data)
print(df)

df.dropna(inplace=True)
print(df)