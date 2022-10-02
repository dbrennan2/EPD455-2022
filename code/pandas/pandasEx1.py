import pandas as pd

# data could also be from csv or other format file
movieData = {
    # Each column name is given by the key
    'Jason' : [4,4,3,2], 
    'Harry' : [2,1,4,4],
    'Bibi'  : [5,5,5,5],
    'Thomas': [1,5,5,3]
}

# create a dataframe from the data
df = pd.DataFrame(data = movieData)

# print the data
print(df)