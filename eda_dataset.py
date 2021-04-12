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
population_by_education_tertiary = total[total['IndicatorName']=='Population of the official age for tertiary education, both sexes (number)']

enrolment_tertiary = total[total['IndicatorName']=='Enrolment in tertiary education, all programmes, both sexes (number)']

teachers_primary = total[total['IndicatorName']=='Teachers in primary education, both sexes (number)']
teachers_secondary = total[total['IndicatorName']=='Teachers in secondary education, both sexes (number)']
teachers_tertiary = total[total['IndicatorName']=='Teachers in tertiary education programmes, both sexes (number)']
teachers_upper_secondary = total[total['IndicatorName']=='Teachers in upper secondary education, both sexes (number)']

years = ['1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2020']

########################

x = np.array(gdp[years])
x = np.nan_to_num(x[0])
print(x)
y = np.array(population_by_education_ntertiary[years])
y = np.nan_to_num(y[0])
print(y)
# pearson_num = cov(x, y, use="complete.obs")
# pearson_den = c(sd(results_summary$D_in), sd(results_summary$D_ex))
corr = np.corrcoef(x,y)

f = plt.figure(figsize=(19, 15))
plt.matshow(corr, fignum=f.number)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
plt.title('Correlation Matrix', fontsize=16)
plt.show()


######################

x = np.array(gdp[years])
x = np.nan_to_num(x[0])
print(x)
y = np.array(population_by_education_tertiary[years])
y = np.nan_to_num(y[0])
print(y)
# pearson_num = cov(x, y, use="complete.obs")
# pearson_den = c(sd(results_summary$D_in), sd(results_summary$D_ex))
corr = np.corrcoef(x,y)

f = plt.figure(figsize=(19, 15))
plt.matshow(corr, fignum=f.number)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
plt.title('Correlation Matrix', fontsize=16)
plt.show()

##########################

x = np.array(gdp[years])
x = np.nan_to_num(x[0])
print(x)
y = np.array(enrolment_tertiary[years])
y = np.nan_to_num(y[0])
print(y)
# pearson_num = cov(x, y, use="complete.obs")
# pearson_den = c(sd(results_summary$D_in), sd(results_summary$D_ex))
corr = np.corrcoef(x,y)

f = plt.figure(figsize=(19, 15))
plt.matshow(corr, fignum=f.number)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
plt.title('Correlation Matrix', fontsize=16)
plt.show()

##########################

x = np.array(gdp[years])
x = np.nan_to_num(x[0])
print(x)
y = np.array(teachers_primary[years])
y = np.nan_to_num(y[0])
print(y)
# pearson_num = cov(x, y, use="complete.obs")
# pearson_den = c(sd(results_summary$D_in), sd(results_summary$D_ex))
corr = np.corrcoef(x,y)

f = plt.figure(figsize=(19, 15))
plt.matshow(corr, fignum=f.number)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
plt.title('Correlation Matrix', fontsize=16)
plt.show()

##########################

x = np.array(gdp[years])
x = np.nan_to_num(x[0])
print(x)
y = np.array(teachers_secondary[years])
y = np.nan_to_num(y[0])
print(y)
# pearson_num = cov(x, y, use="complete.obs")
# pearson_den = c(sd(results_summary$D_in), sd(results_summary$D_ex))
corr = np.corrcoef(x,y)

f = plt.figure(figsize=(19, 15))
plt.matshow(corr, fignum=f.number)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
plt.title('Correlation Matrix', fontsize=16)
plt.show()


##########################

x = np.array(gdp[years])
x = np.nan_to_num(x[0])
print(x)
y = np.array(teachers_tertiary[years])
y = np.nan_to_num(y[0])
print(y)
# pearson_num = cov(x, y, use="complete.obs")
# pearson_den = c(sd(results_summary$D_in), sd(results_summary$D_ex))
corr = np.corrcoef(x,y)

f = plt.figure(figsize=(19, 15))
plt.matshow(corr, fignum=f.number)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
plt.title('Correlation Matrix', fontsize=16)
plt.show()


##########################

x = np.array(gdp[years])
x = np.nan_to_num(x[0])
print(x)
y = np.array(teachers_upper_secondary[years])
y = np.nan_to_num(y[0])
print(y)
# pearson_num = cov(x, y, use="complete.obs")
# pearson_den = c(sd(results_summary$D_in), sd(results_summary$D_ex))
corr = np.corrcoef(x,y)

f = plt.figure(figsize=(19, 15))
plt.matshow(corr, fignum=f.number)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
plt.title('Correlation Matrix', fontsize=16)
plt.show()


