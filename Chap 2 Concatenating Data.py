# Import pandas
import pandas as pd

# Load 'sales-jan-2015.csv' into a DataFrame: jan
jan = pd.read_csv('sales-jan-2015.csv',parse_dates=True,index_col='Date')

# Load 'sales-feb-2015.csv' into a DataFrame: feb
feb = pd.read_csv('sales-feb-2015.csv',parse_dates=True,index_col='Date')

# Load 'sales-mar-2015.csv' into a DataFrame: mar
mar = pd.read_csv('sales-mar-2015.csv',parse_dates=True,index_col='Date')

# Extract the 'Units' column from jan: jan_units
jan_units = jan['Units']

# Extract the 'Units' column from feb: feb_units
feb_units = feb['Units']

# Extract the 'Units' column from mar: mar_units
mar_units = mar['Units']

# Append feb_units and then mar_units to jan_units: quarter1
quarter1 = jan_units.append(feb_units).append(mar_units)

# Print the first slice from quarter1
print(quarter1.loc['jan 27, 2015':'feb 2, 2015'])

# Print the second slice from quarter1
print(quarter1.loc['feb 26, 2015' : 'mar 7, 2015'])

# Compute & print total sales in quarter1
print(quarter1.sum())
#.......................................
<script.py> output:
    Date
    2015-01-27 07:11:55    18
    2015-02-02 08:33:01     3
    2015-02-02 20:54:49     9
    Name: Units, dtype: int64
    Date
    2015-02-26 08:57:45     4
    2015-02-26 08:58:51     1
    2015-03-06 10:11:45    17
    2015-03-06 02:03:56    17
    Name: Units, dtype: int64
    642
######

# Initialize empty list: units
units = []

# Build the list of Series
for month in [jan, feb, mar]:
    units.append(month['Units'])

# Concatenate the list: quarter1
quarter1 = pd.concat(units,axis='rows')

# Print slices from quarter1
print(quarter1.loc['jan 27, 2015':'feb 2, 2015'])
print(quarter1.loc['feb 26, 2015':'mar 7, 2015'])
#.......................................
<script.py> output:
    Date
    2015-01-27 07:11:55    18
    2015-02-02 08:33:01     3
    2015-02-02 20:54:49     9
    Name: Units, dtype: int64
    Date
    2015-02-26 08:57:45     4
    2015-02-26 08:58:51     1
    2015-03-06 10:11:45    17
    2015-03-06 02:03:56    17
    Name: Units, dtype: int64
######

# Add 'year' column to names_1881 and names_1981
names_1881['year'] = 1881
names_1981['year'] = 1981

# Append names_1981 after names_1881 with ignore_index=True: combined_names
combined_names = names_1881.append(names_1981,ignore_index=True)

# Print shapes of names_1981, names_1881, and combined_names
print(names_1981.shape)
print(names_1881.shape)
print(combined_names.shape)

# Print all rows that contain the name 'Morgan'
print(combined_names.loc[combined_names['name']=='Morgan'])
#...............................
(19455, 4)
(1935, 4)
(21390, 4)
         name gender  count  year
1283   Morgan      M     23  1881
2096   Morgan      F   1769  1981
14390  Morgan      M    766  1981
######

# Concatenate weather_max and weather_mean horizontally: weather
weather = pd.concat([weather_max,weather_mean],axis=1)

# Print weather
print(weather)
#..................
     Max TemperatureF  Mean TemperatureF
Apr              89.0          53.100000
Aug               NaN          70.000000
Dec               NaN          34.935484
Feb               NaN          28.714286
Jan              68.0          32.354839
Jul              91.0          72.870968
Jun               NaN          70.133333
Mar               NaN          35.000000
May               NaN          62.612903
Nov               NaN          39.800000
Oct              84.0          55.451613
Sep               NaN          63.766667
######

for medal in medal_types:

    # Create the file name: file_name
    file_name = "%s_top5.csv" % medal
    
    # Create list of column names: columns
    columns = ['Country', medal]
    
    # Read file_name into a DataFrame: df
    medal_df = pd.read_csv(file_name,header=0,index_col='Country',names=columns)

    # Append medal_df to medals
    medals.append(medal_df)

# Concatenate medals horizontally: medals
medals = pd.concat(medals,axis='columns')

# Print medals
print(medals)
#..........................
        print(medals)
                bronze  silver    gold
France           475.0   461.0     NaN
Germany          454.0     NaN   407.0
Italy              NaN   394.0   460.0
Soviet Union     584.0   627.0   838.0
United Kingdom   505.0   591.0   498.0
United States   1052.0  1195.0  2088.0
######

for medal in medal_types:

    file_name = "%s_top5.csv" % medal
    
    # Read file_name into a DataFrame: medal_df
    medal_df = pd.read_csv(file_name, index_col='Country')
    
    # Append medal_df to medals
    medals.append(medal_df)
    
# Concatenate medals: medals
medals = pd.concat(medals, keys=['bronze', 'silver', 'gold'])

# Print medals in entirety
print(medals)
#......................

<script.py> output:
                            Total
           Country               
    bronze United States   1052.0
           Soviet Union     584.0
           United Kingdom   505.0
           France           475.0
           Germany          454.0
    silver United States   1195.0
           Soviet Union     627.0
           United Kingdom   591.0
           France           461.0
           Italy            394.0
    gold   United States   2088.0
           Soviet Union     838.0
           United Kingdom   498.0
           Italy            460.0
           Germany          407.0
######

# Sort the entries of medals: medals_sorted
medals_sorted = medals.sort_index(level=0)

# Print the number of Bronze medals won by Germany
print(medals_sorted.loc[('bronze','Germany')])

# Print data about silver medals
print(medals_sorted.loc['silver'])

# Create alias for pd.IndexSlice: idx
idx = pd.IndexSlice

# Print all the data on medals won by the United Kingdom
print(medals_sorted.loc[idx[:,'United Kingdom'],:])
#..............................
Total    454.0
Name: (bronze, Germany), dtype: float64
                 Total
Country               
France           461.0
Italy            394.0
Soviet Union     627.0
United Kingdom   591.0
United States   1195.0
                       Total
       Country              
bronze United Kingdom  505.0
silver United Kingdom  591.0
gold   United Kingdom  498.0

<script.py> output:
    Total    454.0
    Name: (bronze, Germany), dtype: float64
                     Total
    Country               
    France           461.0
    Italy            394.0
    Soviet Union     627.0
    United Kingdom   591.0
    United States   1195.0
                           Total
           Country              
    bronze United Kingdom  505.0
    silver United Kingdom  591.0
    gold   United Kingdom  498.0
######

# Concatenate dataframes: february
february = pd.concat(dataframes,axis=1,keys=['Hardware', 'Software', 'Service'])

# Print february.info()
print(february.info())

# Assign pd.IndexSlice: idx
idx = pd.IndexSlice

# Create the slice: slice_2_8
slice_2_8 = february.loc['2015-2-2':'2015-2-8', idx[:, 'Company']]

# Print slice_2_8
print(slice_2_8)
#..............................
<class 'pandas.core.frame.DataFrame'>
DatetimeIndex: 20 entries, 2015-02-02 08:33:01 to 2015-02-26 08:58:51
Data columns (total 9 columns):
(Hardware, Company)    5 non-null object
(Hardware, Product)    5 non-null object
(Hardware, Units)      5 non-null float64
(Software, Company)    9 non-null object
(Software, Product)    9 non-null object
(Software, Units)      9 non-null float64
(Service, Company)     6 non-null object
(Service, Product)     6 non-null object
(Service, Units)       6 non-null float64
dtypes: float64(3), object(6)
memory usage: 1.6+ KB
None
                            Hardware         Software Service
                             Company          Company Company
Date                                                         
2015-02-02 08:33:01              NaN            Hooli     NaN
2015-02-02 20:54:49        Mediacore              NaN     NaN
2015-02-03 14:14:18              NaN          Initech     NaN
2015-02-04 15:36:29              NaN        Streeplex     NaN
2015-02-04 21:52:45  Acme Coporation              NaN     NaN
2015-02-05 01:53:06              NaN  Acme Coporation     NaN
2015-02-05 22:05:03              NaN              NaN   Hooli
2015-02-07 22:58:10  Acme Coporation              NaN     NaN
########

# Make the list of tuples: month_list
month_list = [('january', jan), ('february', feb), ('march', mar)]

# Create an empty dictionary: month_dict
month_dict = {}

for month_name, month_data in month_list:

    # Group month_data: month_dict[month_name]
    month_dict[month_name] = month_data.groupby('Company').sum()

# Concatenate data in month_dict: sales
sales = pd.concat(month_dict)

# Print sales
print(sales)

# Print all sales by Mediacore
idx = pd.IndexSlice
print(sales.loc[idx[:, 'Mediacore'], :])
#........................
                          Units
         Company               
february Acme Coporation     34
         Hooli               30
         Initech             30
         Mediacore           45
         Streeplex           37
january  Acme Coporation     76
         Hooli               70
         Initech             37
         Mediacore           15
         Streeplex           50
march    Acme Coporation      5
         Hooli               37
         Initech             68
         Mediacore           68
         Streeplex           40
                    Units
         Company         
february Mediacore     45
january  Mediacore     15
march    Mediacore     68

<script.py> output:
                              Units
             Company               
    february Acme Coporation     34
             Hooli               30
             Initech             30
             Mediacore           45
             Streeplex           37
    january  Acme Coporation     76
             Hooli               70
             Initech             37
             Mediacore           15
             Streeplex           50
    march    Acme Coporation      5
             Hooli               37
             Initech             68
             Mediacore           68
             Streeplex           40
                        Units
             Company         
    february Mediacore     45
    january  Mediacore     15
    march    Mediacore     68
##############################

# Create the list of DataFrames: medal_list
medal_list = [bronze, silver, gold]

# Concatenate medal_list horizontally using an inner join: medals
medals = pd.concat(medal_list,keys=['bronze', 'silver', 'gold'],axis=1,join='inner')

# Print medals
print(medals)
#..........................
                bronze  silver    gold
                 Total   Total   Total
Country                               
United States   1052.0  1195.0  2088.0
Soviet Union     584.0   627.0   838.0
United Kingdom   505.0   591.0   498.0
######################

# Resample and tidy china: china_annual
china_annual = china.resample('A').pct_change(10).dropna()

# Resample and tidy us: us_annual
us_annual = us.resample('A').pct_change(10).dropna()

# Concatenate china_annual and us_annual: gdp
gdp = pd.concat([china_annual,us_annual],join='inner',axis=1)

# Resample gdp and print
print(gdp.resample('10A').last())
#.........................
(               China
 Year                
 1971-12-31  0.988860
 1972-12-31  1.402472
 1973-12-31  1.730085
 1974-12-31  1.408556
 1975-12-31  1.311927
 1976-12-31  0.998271
 1977-12-31  1.391842
 1978-12-31  1.119941
 1979-12-31  1.246687
 1980-12-31  1.072537
 1981-12-31  0.972048
 1982-12-31  0.814818
 1983-12-31  0.673981
 1984-12-31  0.814225
 1985-12-31  0.907886
 1986-12-31  0.970655
 1987-12-31  0.574420
 1988-12-31  1.094068
 1989-12-31  0.956148
 1990-12-31  0.892820
 1991-12-31  0.962528
 1992-12-31  1.087619
 1993-12-31  0.934371
 1994-12-31  1.178613
 1995-12-31  1.380750
 1996-12-31  1.880948
 1997-12-31  2.531086
 1998-12-31  2.299658
 1999-12-31  2.149078
 2000-12-31  2.357522
 2001-12-31  2.492511
 2002-12-31  2.440314
 2003-12-31  2.725499
 2004-12-31  2.453459
 2005-12-31  2.099043
 2006-12-31  2.171055
 2007-12-31  2.676940
 2008-12-31  3.446049
 2009-12-31  3.644025
 2010-12-31  4.011081
 2011-12-31  4.623958
 2012-12-31  4.788074
 2013-12-31  4.752129
 2014-12-31  4.330828
 2015-12-31  3.789936,                   US
 Year                
 1957-12-31  0.882582
 1958-12-31  0.754116
 1959-12-31  0.914788
 1960-12-31  0.809861
 1961-12-31  0.621752
 1962-12-31  0.645591
 1963-12-31  0.638422
 1964-12-31  0.753340
 1965-12-31  0.745116
 1966-12-31  0.810619
 1967-12-31  0.814731
 1968-12-31  0.954986
 1969-12-31  0.952101
 1970-12-31  0.980397
 1971-12-31  1.073188
 1972-12-31  1.119273
 1973-12-31  1.237090
 1974-12-31  1.258503
 1975-12-31  1.270900
 1976-12-31  1.303632
 1977-12-31  1.420668
 1978-12-31  1.500504
 1979-12-31  1.580855
 1980-12-31  1.660540
 1981-12-31  1.749631
 1982-12-31  1.608340
 1983-12-31  1.546726
 1984-12-31  1.608881
 1985-12-31  1.573679
 1986-12-31  1.444709
 1987-12-31  1.334776
 1988-12-31  1.228900
 1989-12-31  1.149460
 1990-12-31  1.088953
 1991-12-31  0.922811
 1992-12-31  0.954948
 1993-12-31  0.890727
 1994-12-31  0.808789
 1995-12-31  0.763168
 1996-12-31  0.764696
 1997-12-31  0.767583
 1998-12-31  0.730401
 1999-12-31  0.707518
 2000-12-31  0.719980
 2001-12-31  0.720398
 2002-12-31  0.678700
 2003-12-31  0.673379
 2004-12-31  0.679478
 2005-12-31  0.708457
 2006-12-31  0.710568
 2007-12-31  0.681778
 2008-12-31  0.619357
 2009-12-31  0.492525
 2010-12-31  0.455009
 2011-12-31  0.460947
 2012-12-31  0.471666
 2013-12-31  0.450089
 2014-12-31  0.416962
 2015-12-31  0.377506
 2016-12-31  0.324999)

<script.py> output:
                   China        US
    Year                          
    1971-12-31  0.988860  1.073188
    1981-12-31  0.972048  1.749631
    1991-12-31  0.962528  0.922811
    2001-12-31  2.492511  0.720398
    2011-12-31  4.623958  0.460947
    2021-12-31  3.789936  0.377506

################################################
