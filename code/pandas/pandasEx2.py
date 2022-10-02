import pandas as pd

# this data can also be from a csv file or any other file
movieData = {
    # Each column name is given by the key
    'Jason' : [4,4,3,2], 
    'Harry' : [2,1,4,4],
    'Bibi'  : [5,5,5,5],
    'Thomas': [1,5,5,3]
}
titles = ['Rogue One','Guardians of the Galaxy','Manchester by the Sea','La La Land']
# create a dataframe from the data
df = pd.DataFrame(data = movieData, index = titles)

# print the data
print(df)