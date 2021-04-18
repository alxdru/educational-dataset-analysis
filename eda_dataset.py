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


indicators = ['GDP per capita (current US$)', 'GNI per capita, Atlas method (current US$)']
countries = ['World', 'East Asia & Pacific']

world_vs_asia_GDP = total[total['IndicatorName'].isin([indicators[0]]) & total['CountryName'].isin(countries)]

fig, ax = plt.subplots()
for c in ['CountryName', 'CountryCode', 'IndicatorName', 'Unnamed: 0']:
    del world_vs_asia_GDP[c]
world_vs_asia_GDP = world_vs_asia_GDP.T
world_vs_asia_GDP.plot(lw=2, ax=ax, colormap='jet', marker='.', markersize=10, title="World GDP vs East Asia & Pacific")
ax.legend(countries)

fig, ax = plt.subplots()
world_vs_asia_GNI = total[total['IndicatorName'].isin([indicators[1]]) & total['CountryName'].isin(countries)]
for c in ['CountryName', 'CountryCode', 'IndicatorName', 'Unnamed: 0']:
    del world_vs_asia_GNI[c]
world_vs_asia_GNI = world_vs_asia_GNI.T
world_vs_asia_GNI.plot(lw=2, ax=ax, colormap='jet', marker='.', markersize=10, title="World GNI vs East Asia & Pacific")
ax.legend(countries)


print(world_vs_asia_GDP.iloc)


