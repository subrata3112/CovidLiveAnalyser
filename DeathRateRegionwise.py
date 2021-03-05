import wget
import os

url = 'https://covid19.who.int/WHO-COVID-19-global-table-data.csv'

if os.path.exists('data.csv'):
	os.remove('data.csv')
	wget.download(url, 'data.csv')
else:
	wget.download(url, 'data.csv')	

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data_csv = pd.read_csv('data.csv')
data = data_csv.copy()
data.dropna(axis=0, inplace=True)
data = data.assign(DeathRate = data['Deaths - cumulative total']/data['Cases - cumulative total'])
data.dropna(axis=0, inplace=True)

sns.boxplot(x=data['WHO Region'],y=data['DeathRate'])

plt.show()