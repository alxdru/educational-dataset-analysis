import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns
from scipy.stats.stats import pearsonr 

# Read original file
total=pd.read_csv('./total.csv')

# Correlations
gdp = total[total['IndicatorName']=='GDP per capita (current US$)']
gni = total[total['IndicatorName']=='GNI per capita, Atlas method (current US$)']

population_by_education_ntertiary = total[total['IndicatorName']=='Population of the official age for post-secondary non-tertiary education, both sexes (number)']
population_by_education_ntertiary.head()

population_by_education_tertiary = total[total['IndicatorName']=='Population of the official age for tertiary education, both sexes (number)']
population_by_education_tertiary.head()

enrolment_tertiary = total[total['IndicatorName']=='Enrolment in tertiary education, all programmes, both sexes (number)']
enrolment_tertiary.head()


# Pivot table for teachers on the 3 levels of education
teachers_all_levels = total[total['IndicatorName'].str.contains('Teachers in') & total['IndicatorName'].str.contains('both sexes')]
teachers_all_levels_pt=pd.pivot_table(teachers_all_levels, index='CountryCode', columns='IndicatorName', values=['2010'], dropna=True)

teachers_all_levels_pt['sum'] = teachers_all_levels_pt.sum(axis=1)
teachers_all_levels_pt = teachers_all_levels_pt[teachers_all_levels_pt['sum']!=0]

teachers_all_levels_pt=teachers_all_levels_pt.drop('sum',axis=1)

# Bar plots for all education levels per each country
teachers_all_levels_pt=teachers_all_levels_pt[::-1]
pal=sns.cubehelix_palette(8)
teachers_graph=teachers_all_levels_pt.plot(kind='barh', stacked=True, figsize=(20,36), color=pal, title='Teachers by level of education: Lower Secondary (both), Pre-Primary (both), Primary (both), Secondary (both), Secondary General (both), Secondary Vocational (both), tertiary ISCED 5 (both), tertiary programmes (both), upper education (both)', legend=False, xlim=(0,10000000))
teachers_graph

# Pivot table for Populations of the official ages per levels of education
population_all_levels = total[total['IndicatorName'].str.contains('Population of the official age for') & total['IndicatorName'].str.contains('both sexes')]
population_all_levels_pt = pd.pivot_table(population_all_levels, index='CountryCode', columns='IndicatorName', values=['2010'], dropna=True)

population_all_levels_pt['sum'] = population_all_levels_pt.sum(axis=1)
population_all_levels_pt = population_all_levels_pt[population_all_levels_pt['sum']!=0]

population_all_levels_pt = population_all_levels_pt.drop('sum', axis=1)

population_all_levels_pt=population_all_levels_pt[::-1]
pal=sns.cubehelix_palette(8, start=2, rot=0, dark=0, light=.95)
population_graph=population_all_levels_pt.plot(kind='barh', stacked=True, figsize=(20,36), color=pal, title='Population of the official age for: Lower Secondary, Post-secondary non-tertiary, Pre-Primary, Primary, Secondary, Tertiary, Last grade of primary education, Upper secondary education', legend=False, xlim=(0,10000000))
population_graph

# Evolutionary graph for GDP and GNI
import matplotlib.style as style
style.use('default')

years = list(map(lambda y: str(y), list(range(1996,2015))))

indicators = [
    "GDP per capita (current US$)",
    "GDP per capita, PPP (current international $)", 
    "GNI (current US$)", 
    "GNI, PPP (current international $)",
    "Literacy rate, population 25-64 years, both sexes (%)",
    "Adult literacy rate, population 15+ years, both sexes (%)",
    "Youth literacy rate, population 15-24 years, both sexes (%)",
    "Unemployment, total (% of total labor force)",
    "Internet users (per 100 people)",
    "Personal computers (per 100 people)",
    "Pupil-teacher ratio in tertiary education (headcount basis)",
    "School life expectancy, tertiary, both sexes (years)",
    "Labor force with advanced education (% of total)"
    ]

countries_macro = ['World', 'East Asia & Pacific']

########## Plotting list of indicators

for indicator in indicators:

    countries = total[total['IndicatorName'].isin([indicator]) & ~total['CountryName'].isin(countries_macro)]
    top_5_countries = countries.nlargest(5, 'sum')
    bottom_5_countries = countries.nsmallest(5, 'sum')

    ## Top 5
    world_vs_asia = total[total['IndicatorName'].isin([indicator])]

    world_region_and_highest = countries_macro + top_5_countries['CountryName'].tolist()
    fig, ax = plt.subplots()
    world_vs_asia = world_vs_asia[world_vs_asia['CountryName'].isin(world_region_and_highest)]
    for c in ['CountryName', 'CountryCode', 'IndicatorName', 'Unnamed: 0']:
        del world_vs_asia[c]
    world_vs_asia = world_vs_asia[years]
    world_vs_asia = world_vs_asia.T
    world_vs_asia.plot(lw=2, ax=ax, colormap='jet', marker='.', markersize=10, title="{0} with top 5 countries".format(indicator))
    ax.legend(world_region_and_highest)

    ## Bottom 5
    world_vs_asia = total[total['IndicatorName'].isin([indicator])]

    world_region_and_lowest = countries_macro + bottom_5_countries['CountryName'].tolist()
    fig2, ax2 = plt.subplots()
    world_vs_asia = world_vs_asia[world_vs_asia['CountryName'].isin(world_region_and_lowest)]
    for c in ['CountryName', 'CountryCode', 'IndicatorName', 'Unnamed: 0']:
        del world_vs_asia[c]
    world_vs_asia = world_vs_asia[years]
    world_vs_asia = world_vs_asia.T
    world_vs_asia.plot(lw=2, ax=ax2, colormap='jet', marker='.', markersize=10, title="{0} with bottom 5 countries".format(indicator))
    ax2.legend(world_region_and_lowest)




