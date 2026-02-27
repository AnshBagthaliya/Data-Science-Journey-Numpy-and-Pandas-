import pandas as pd

data = {
    "Time":[1,2,3,4,5],
    "Value":[10,None,30,None,50]
}

df = pd.DataFrame(data)
print("Befor interpolation")
print(df)

df['Value'] = df['Value'].interpolate(method="linear")
print("After interpolation")
print(df)

'''
1- timer series data (Ex. stock market)
2- numeric data with trends
3- avoid droping rows(Advantages: dataset structured , estimated value fill out)
(Disadvantages:  not use for categorical data(Ex. Names,ID),It assumes a predictable pattern that might not always exist )
'''