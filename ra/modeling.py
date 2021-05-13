import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns
from scipy.stats.stats import pearsonr
from statsmodels.tsa.arima.model import ARIMA
from random import random
import math

# Read original file
total=pd.read_csv('./total.csv')

countries_list = ['World', "East Asia & Pacific", 'China', "Hong Kong", 'Japan', 'Macau', 'Mongolia', "Korea, Dem. People’s Rep.", "North Korea", "South Korea", 'Taiwan', 'Brunei', 'Cambodia', 'Indonesia', 'Malaysia', 'Myanmar', 'Philippines', 'Singapore', 'Thailand', 'Vietnam']

## First get the variables that I want to use in regression and forecast them
years = list(map(lambda y: str(y), list(range(1990,2016))))
all_years = []
indicators = [
    "GDP per capita (current US$)",
    "Unemployment total (% of total labor force)",
    "Labor force total",
    "Population total"
]

countries_macro = ['World', 'East Asia & Pacific']

final_dict = {}
for indicator in indicators:

    all_countries = countries_list
    all_years = list(map(lambda y: str(y), list(range(1990,2016))))

    df_record = pd.DataFrame([], columns=['Country'] + all_years)
    world_vs_asia = total[total['IndicatorName'].isin([indicator])]
    for country in all_countries: 
        
        data_country = world_vs_asia[world_vs_asia['CountryName'].isin([country])]
        # print(data_country)
        for c in ['CountryName', 'CountryCode', 'IndicatorName', 'Unnamed: 0', 'sum']:
            del data_country[c]
        data_country = data_country[years]
        data_country = data_country.T
        if not data_country.empty:
            
            ## Forecasting additional 15 years as variable candidates for regression
            all_data = data_country.iloc[:,0].tolist()

            df_forecast = pd.DataFrame([all_data], columns= list(map(lambda y: str(y), list(range(1990,2016)))))

            df_forecast['Country'] = country
            df_record = df_record.append(df_forecast, ignore_index=True)

    final_dict[indicator] = df_record

final_dict['Labor force (% of total)'] = final_dict['Labor force total'].select_dtypes(exclude='object').div(final_dict['Population total'].select_dtypes(exclude='object'))

print(final_dict)