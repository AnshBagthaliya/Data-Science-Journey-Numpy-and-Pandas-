import pandas as pd

data = {
    "Name":['Ram','Ramu','Ramesh'],
    "Age":[10,20,30],
    "City":['Nagpur','Rajkot','Mumbai']
}

df = pd.DataFrame(data)

# df = pd.read_json("sample_Data.json")

print('Dispaly The info of data set :')
print(df.info())

