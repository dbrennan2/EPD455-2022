import cProfile
import pandas as pd
cProfile.run("pd.Series(list('ABCDEFG'))")