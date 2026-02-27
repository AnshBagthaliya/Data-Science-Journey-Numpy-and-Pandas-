import pandas as pd

data = {
    "Name":['Ram','Ramu','Ramesh'],
    "Age":[10,20,30],
    "City":['Nagpur','Rajkot','Mumbai']
}

df = pd.DataFrame(data)
print(df)

# df.to_csv("output.csv") # Save a csv file
# df.to_csv("output.csv",index=False) # Remove index in the file

# df.to_excel("output.xlsx",index=False) # to save in excel

df.to_json("output.json",index=False)