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

# print the data
print(df)