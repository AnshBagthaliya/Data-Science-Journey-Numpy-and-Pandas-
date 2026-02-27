'''
Combine two DataFrames
verticaliy(row-wise)
horizontally(column wise)

pd.concate([df1,df2], axis=0, ignore_index=True)

[df1,df2] =
axis=1

ignore_index = True
'''
#verticaliy()
import pandas as pd

region1 = pd.DataFrame({
    "CustomerID":[1,2],
    "Name":["Shyam","Raju"]
})

region2 = pd.DataFrame({
    "CustomerID":[3,4],
    "Name":["Gopal","Baburav"]
})

# concat  = pd.concat([region1,region2],ignore_index=True)
# concat  = pd.concat([region1,region2],axis=0,ignore_index=True)
concat  = pd.concat([region1,region2],axis=1,ignore_index=True)
print(concat)
