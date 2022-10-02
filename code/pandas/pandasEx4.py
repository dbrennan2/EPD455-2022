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

# ilocate 'Rogue One' row
print(df.iloc[0])
# ilocate 'Jason' column
print(df.iloc[:,0])
# ilocate 'Rogue One' row and jason column
print(df.iloc[0, 0])
# ilocate 'Rogue One' and 'La la land' row for 'Jason
print(df.iloc[[0,-1], 0])
