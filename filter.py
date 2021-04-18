import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns
from scipy.stats.stats import pearsonr 

# Read original file
original=pd.read_csv('./dataset/EdStatsData.csv')

# Arrange the original data
original=original.drop('IndicatorCode',axis=1)

# Delete rows that all values are NaN
original['sum']=original.sum(axis=1)

# The rows that their sum is not 0 remain
total=original[original['sum']!=0]

countries = ['World', 'East Asia & Pacific', 'China', 'Hong Kong', 'Japan', 'Macau', 'Mongolia', 'Korea, Dem. People’s Rep.', 'North Korea', 'South Korea', 'Taiwan', 'Brunei', 'Cambodia', 'Indonesia', 'Malaysia', 'Myanmar', 'Philippines', 'Singapore', 'Thailand', 'Vietnam']
# East Asia & Pacific filter
total = total[total['CountryName'].isin(countries)]

total.to_csv('total.csv')