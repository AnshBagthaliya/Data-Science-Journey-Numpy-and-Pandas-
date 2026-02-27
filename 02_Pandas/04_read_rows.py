# Method1 -head()
# Method2 -tail()
#head() 5 # Staring
#tail() 5 # Ending

import pandas as pd
df = pd.read_json("sample_Data.json")

print("Display 10 rows of Start ")
print(df.head(10))

print("Display 10 rows of End ")
print(df.tail(10))
 