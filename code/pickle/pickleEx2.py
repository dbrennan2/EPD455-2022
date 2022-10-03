import pandas as pd
import pickle

#load dataframe from pickle file
df = pd.read_pickle("movieRating.pkl")
print(df)