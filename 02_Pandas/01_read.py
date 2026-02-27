import pandas as pd
#read data from CSV file into a dataframe

# rid = pd.read_csv("sales_data_sample.csv") # UnicodeDecodeError
# rid = pd.read_csv("sales_data_sample.csv",encoding="latin1")# Display Data
 
# print(rid) 

# df = pd.read_excel("SampleSuperstore.xlsx")
# print (df)

df = pd.read_json("sample_Data.json")
print(df)