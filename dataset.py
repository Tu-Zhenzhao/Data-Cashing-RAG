import pandas as pd
import numpy as np

# import dataset
def load_dataset(path):
    df = pd.read_csv(path)
    return df

#df = load_dataset('datasci.csv')
#print(df.shape)
