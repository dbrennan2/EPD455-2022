import pandas as pd

data = {
    'Jason' : [4,4,3,2], 
    'Harry' : [2,1,4,4],
    'Bibi'  : [5,5,5,5],
    'Thomas': [1,5,5,3]
}
index = ['Rogue One','Guardians of the Galaxy',\
    'Manchester by the Sea','La La Land']
    
df = pd.DataFrame(data = data, index = index)

df.loc[:,'Movie - Avg. rating'] = df.mean(axis=1)

df.loc['Person - Avg. rating'] = df.mean(axis=0)

df.iloc[-1,-1] = 0

df.to_csv('movieRating.csv')