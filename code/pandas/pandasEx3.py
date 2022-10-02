import pandas as pd
movieData = {
    'Jason' : [4,4,3,2], 
    'Harry' : [2,1,4,4],
    'Bibi'  : [5,5,5,5],
    'Thomas': [1,5,5,3]
}
titles = ['Rogue One','Guardians of the Galaxy','Manchester by the Sea','La La Land']
df = pd.DataFrame(data = movieData, index = titles)
print(df)
# Locate 'Rogue One' row
print(df.loc['Rogue One'])
# locate 'Jason' column
print(df.loc[:,'Jason'])
#locate 'Rogue One' row and jason column
print(df.loc['Rogue One', 'Jason'])
print(f"Type returned by loc/iloc {type(df.loc['Rogue One'])}")
print(f"Locating multiple rows returns a DataFrame {type(df.loc[['Rogue One','La La Land']])}")
print(f"Locating a single row can also return a {type(df.loc[['Rogue One']])}")