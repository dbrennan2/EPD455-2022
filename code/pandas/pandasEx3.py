import pandas as pd

# this data can also be from a csv file or any other file
data = {
    'Jason' : [4,4,3,2], # Each column name is given by the key
    'Harry' : [2,1,4,4],
    'Bibi'  : [5,5,5,5],
    'Thomas': [1,5,5,3]
}
index = ['Rogue One','Guardians of the Galaxy','Manchester by the Sea','La La Land']
# create a dataframe from the data
df = pd.DataFrame(data = data, index = index)

# Locate 'Rogue One' row
print(df.loc['Rogue One'])
# locate 'Jason' column
print(df.loc[:,'Jason'])
#locate 'Rogue One' row and jason column
print(df.loc['Rogue One', 'Jason'])
print(f"Type returned by loc/iloc {type(df.loc['Rogue One'])}")
print(f"Locating multiple rows returns a DataFrame {type(df.loc[['Rogue One','La La Land']])}")
print(f"Locating a single row can also return a {type(df.loc[['Rogue One']])}")