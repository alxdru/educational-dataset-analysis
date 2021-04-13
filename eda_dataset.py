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


teachers_all_levels = total[total['IndicatorName'].str.contains('Teachers in')]


# Pivot table for teachers on the 3 levels of education

teachers_all_levels_pt=pd.pivot_table(teachers_all_levels, index='CountryCode', columns='IndicatorName', values=['2010'], dropna=True)

teachers_all_levels_pt['sum'] = teachers_all_levels_pt.sum(axis=1)
teachers_all_levels_pt = teachers_all_levels_pt[teachers_all_levels_pt['sum']!=0]

teachers_all_levels_pt=teachers_all_levels_pt.drop('sum',axis=1)

teachers_all_levels_pt=teachers_all_levels_pt[::-1]
pal=sns.cubehelix_palette(8)
teachers_graph=teachers_all_levels_pt.plot(kind='barh', stacked=True, figsize=(20,36), color=pal, title='Teachers by level of education: Lower Secondary (both), Pre-Primary (both), Pre-Primary (female), Primary (both), Primary (female), Secondary (both), Secondary (female), Secondary General (both), Secondary Vocational (both), tertiary ISCED 5 (both), tertiary programmes (both), tertiary programmes (female), upper education (both)', legend=False, xlim=(0,10000000))
teachers_graph

years = ['1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2020']

