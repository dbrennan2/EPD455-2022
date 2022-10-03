import pandas as pd
import pickle
movieData = {
    'Jason' : [4,4,3,2], 
    'Harry' : [2,1,4,4],
    'Bibi'  : [5,5,5,5],
    'Thomas': [1,5,5,3]
}
titles = ['Rogue One','Guardians of the Galaxy','Manchester by the Sea','La La Land']
df = pd.DataFrame(data = movieData, index = titles)

df.loc[:, 'Movie - Avg. rating'] = df.mean(axis=1)

df.loc['Person - Avg. rating'] = df.mean(axis=0)

df.iloc[-1, -1] = None

# pickle the data frame
df.to_pickle('movieRating.pkl')
