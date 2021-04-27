import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns
from scipy.stats.stats import pearsonr
from statsmodels.tsa.arima.model import ARIMA
from random import random

# Read original file
total=pd.read_csv('./total.csv')

countries_list = ['World', "East Asia & Pacific", 'China', "Hong Kong", 'Japan', 'Macau', 'Mongolia', "Korea, Dem. People’s Rep.", "North Korea", "South Korea", 'Taiwan', 'Brunei', 'Cambodia', 'Indonesia', 'Malaysia', 'Myanmar', 'Philippines', 'Singapore', 'Thailand', 'Vietnam']

## First get the variables that I want to use in regression and forecast them
years = list(map(lambda y: str(y), list(range(1977,2016))))
all_years = []
indicators = [
    "GDP per capita (current US$)",
    # "GDP per capita, PPP (current international $)", 
    # "GNI (current US$)", 
    # "GNI, PPP (current international $)",
    # "Literacy rate, population 25-64 years, both sexes (%)",
    # "Adult literacy rate, population 15+ years, both sexes (%)",
    # "Youth literacy rate, population 15-24 years, both sexes (%)",
    "Unemployment, total (% of total labor force)",
    # "Internet users (per 100 people)",
    # "Personal computers (per 100 people)",
    # "Pupil-teacher ratio in tertiary education (headcount basis)",
    # "School life expectancy, tertiary, both sexes (years)",
    "Labor force with advanced education (% of total)"
    ]

countries_macro = ['World', 'East Asia & Pacific']

final_dict = {}
for indicator in indicators:

    countries = total[total['IndicatorName'].isin([indicator]) & ~total['CountryName'].isin(countries_macro)]
    top_5_countries = countries.nlargest(5, 'sum')
    bottom_5_countries = countries.nsmallest(5, 'sum')
    all_countries = top_5_countries['CountryName'].tolist() + bottom_5_countries['CountryName'].tolist() + countries_macro
    all_years = list(map(lambda y: str(y), list(range(1977,2031))))

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
            data_list = data_country.iloc[:,0].tolist()
            model = ARIMA(data_list, order=(1,1,1))
            model_fit = model.fit()
            data_predicted = model_fit.predict(start = len(data_list), end = len(data_list) + 14, typ='levels')
            
            all_data = data_list + data_predicted.tolist()

            df_forecast = pd.DataFrame([all_data], columns=all_years)

            df_forecast['Country'] = country
            df_record = df_record.append(df_forecast, ignore_index=True)

    final_dict[indicator] = df_record


