library(ggplot2)

data_df <- read.csv('./dataset/EdStatsData.csv')

data_df <- data_df[data_df$ï..CountryName == 'East Asia & Pacific',]

data_df <- data_df[!is.na(data_df$X1976) & !is.na(data_df$X1977) & !is.na(data_df$X1978) & !is.na(data_df$X1979) & !is.na(data_df$X1980) & !is.na(data_df$X1981) & !is.na(data_df$X1982) & !is.na(data_df$X1983) & !is.na(data_df$X1984) & !is.na(data_df$X1985) & !is.na(data_df$X1986) & !is.na(data_df$X1987) & !is.na(data_df$X1988) & !is.na(data_df$X1989) & !is.na(data_df$X1990) & !is.na(data_df$X1991) & !is.na(data_df$X1992) & !is.na(data_df$X1993) & !is.na(data_df$X1994) & !is.na(data_df$X1995) & !is.na(data_df$X1996) & !is.na(data_df$X1997) & !is.na(data_df$X1998) & !is.na(data_df$X1999) & !is.na(data_df$X2000) & !is.na(data_df$X2001) & !is.na(data_df$X2002) & !is.na(data_df$X2003) & !is.na(data_df$X2004) & !is.na(data_df$X2005) & !is.na(data_df$X2006) & !is.na(data_df$X2007) & !is.na(data_df$X2008) & !is.na(data_df$X2009) & !is.na(data_df$X2010) & !is.na(data_df$X2011) & !is.na(data_df$X2012) & !is.na(data_df$X2013) & !is.na(data_df$X2014),]

print(colnames(data_df))

print(head(data_df))

print('Indicatorii cu date sunt urmatorii: ')
print(data_df$IndicatorName)