import pandas as pd
import time
from langdetect import detect
import goslate
from matplotlib import dates

# read data
calendar = pd.read_csv('./Data/calendar1.csv', delimiter = ',')

# check data
calendar.head()

# get only available entries
available = calendar[calendar["available"] == 't']

# insert a column to store cleaned price
available.insert(3, 'price_cleaned', np.zeros((available.shape[0],1)))

# clean price
for idx in range(available.shape[0]):
    if math.isnan(available.iloc[idx]['etc']):
        price_str = available.iloc[idx]['price']
        available.iloc[idx, 3] = float(price_str[1:-1])
    else:
        price_str = available.iloc[idx]['price']
        price_str1 = available.iloc[idx]['etc']
        available.iloc[idx, 3] = float(price_str[1:-1])*1000 + float(price_str1)

