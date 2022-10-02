import pandas as pd
movieData = {
    'Jason' : [4,4,3,2], 
    'Harry' : [2,1,4,4],
    'Bibi'  : [5,5,5,5],
    'Thomas': [1,5,5,3]
}
titles = ['Rogue One','Guardians of the Galaxy','Manchester by the Sea','La La Land']
df = pd.DataFrame(data = movieData, index = titles)

# Get row wise average and store it in a column
df.loc[:,'Movie - Avg. rating'] = df.mean(axis=1)

# Get column wise average and store it in a row
df.loc['Person - Avg. rating'] = df.mean(axis=0)

# set the last element to None since it has no meaning
df.iloc[-1,-1] = None
df.to_csv('movieRating.csv')