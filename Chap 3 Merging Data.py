# Merge revenue with managers on 'city': merge_by_city
merge_by_city = pd.merge(revenue,managers,on='city')

# Print merge_by_city
print(merge_by_city)

# Merge revenue with managers on 'branch_id': merge_by_id
merge_by_id = pd.merge(revenue,managers,on='branch_id')

# Print merge_by_id
print(merge_by_id)
#.........................................
<script.py> output:
       branch_id_x         city  revenue  branch_id_y  manager
    0           10       Austin      100           10  Charles
    1           20       Denver       83           20     Joel
    2           30  Springfield        4           31    Sally
    3           47    Mendocino      200           47    Brett
       branch_id     city_x  revenue     city_y  manager
    0         10     Austin      100     Austin  Charles
    1         20     Denver       83     Denver     Joel
    2         47  Mendocino      200  Mendocino    Brett

##  Notice that when you merge on 'city', the resulting DataFrame has a peculiar result: In row 2, the city Springfield has two different branch IDs. This is because there are actually two different cities named Springfield - one in the State of Illinois, and the other in Missouri. The revenue DataFrame has the one from Illinois, and the managers DataFrame has the one from Missouri. Consequently, when you merge on 'branch_id', both of these get dropped from the merged DataFrame.
##########

# Merge revenue & managers on 'city' & 'branch': combined
combined = pd.merge(revenue,managers, left_on='city', right_on='branch')

# Print combined
print(combined)
#..............................................
<script.py> output:
       branch_id_x         city  revenue state_x       branch  branch_id_y  \
    0           10       Austin      100      TX       Austin           10   
    1           20       Denver       83      CO       Denver           20   
    2           30  Springfield        4      IL  Springfield           31   
    3           47    Mendocino      200      CA    Mendocino           47   
    
        manager state_y  
    0  Charlers      TX  
    1      Joel      CO  
    2     Sally      MO  
    3     Brett      CA
######

# Add 'state' column to revenue: revenue['state']
revenue['state'] = ['TX','CO','IL','CA']

# Add 'state' column to managers: managers['state']
managers['state'] = ['TX','CO','CA','MO']

# Merge revenue & managers on 'branch_id', 'city', & 'state': combined
combined = pd.merge(revenue,managers,on=['branch_id','city','state'])

# Print combined
print(combined)
#........................
<script.py> output:
       branch_id       city  revenue state   manager
    0         10     Austin      100    TX  Charlers
    1         20     Denver       83    CO      Joel
    2         47  Mendocino      200    CA     Brett
######

# Merge revenue and sales: revenue_and_sales
revenue_and_sales = pd.merge(revenue,sales,how='right',on=['city', 'state'])

# Print revenue_and_sales
print(revenue_and_sales)

# Merge sales and managers: sales_and_managers
sales_and_managers = pd.merge(sales,managers,how='left',right_on=['branch', 'state'],left_on=['city', 'state'])

# Print sales_and_managers
print(sales_and_managers)
#...................................................
   branch_id         city  revenue state  units
0       10.0       Austin    100.0    TX      2
1       20.0       Denver     83.0    CO      4
2       30.0  Springfield      4.0    IL      1
3       47.0    Mendocino    200.0    CA      1
4        NaN  Springfield      NaN    MO      5
          city state  units       branch  branch_id   manager
0    Mendocino    CA      1    Mendocino       47.0     Brett
1       Denver    CO      4       Denver       20.0      Joel
2       Austin    TX      2       Austin       10.0  Charlers
3  Springfield    MO      5  Springfield       31.0     Sally
4  Springfield    IL      1          NaN        NaN       NaN

<script.py> output:
       branch_id         city  revenue state  units
    0       10.0       Austin    100.0    TX      2
    1       20.0       Denver     83.0    CO      4
    2       30.0  Springfield      4.0    IL      1
    3       47.0    Mendocino    200.0    CA      1
    4        NaN  Springfield      NaN    MO      5
              city state  units       branch  branch_id   manager
    0    Mendocino    CA      1    Mendocino       47.0     Brett
    1       Denver    CO      4       Denver       20.0      Joel
    2       Austin    TX      2       Austin       10.0  Charlers
    3  Springfield    MO      5  Springfield       31.0     Sally
    4  Springfield    IL      1          NaN        NaN       NaN
##############

# Perform the first merge: merge_default
merge_default = pd.merge(sales_and_managers, revenue_and_sales)

# Print merge_default
print(merge_default)

# Perform the second merge: merge_outer
merge_outer = pd.merge(sales_and_managers, revenue_and_sales, how='outer')

# Print merge_outer
print(merge_outer)

# Perform the third merge: merge_outer_on
merge_outer_on = pd.merge(sales_and_managers, revenue_and_sales, on=['city','state'], how='outer')

# Print merge_outer_on
print(merge_outer_on)
#........................................................
        city state  units     branch  branch_id   manager  revenue
0  Mendocino    CA      1  Mendocino       47.0     Brett    200.0
1     Denver    CO      4     Denver       20.0      Joel     83.0
2     Austin    TX      2     Austin       10.0  Charlers    100.0

          city state  units       branch  branch_id   manager  revenue
0    Mendocino    CA      1    Mendocino       47.0     Brett    200.0
1       Denver    CO      4       Denver       20.0      Joel     83.0
2       Austin    TX      2       Austin       10.0  Charlers    100.0
3  Springfield    MO      5  Springfield       31.0     Sally      NaN
4  Springfield    IL      1          NaN        NaN       NaN      NaN
5  Springfield    IL      1          NaN       30.0       NaN      4.0
6  Springfield    MO      5          NaN        NaN       NaN      NaN

          city state  units_x       branch  branch_id_x   manager  \
0    Mendocino    CA        1    Mendocino         47.0     Brett   
1       Denver    CO        4       Denver         20.0      Joel   
2       Austin    TX        2       Austin         10.0  Charlers   
3  Springfield    MO        5  Springfield         31.0     Sally   
4  Springfield    IL        1          NaN          NaN       NaN   

   branch_id_y  revenue  units_y  
0         47.0    200.0        1  
1         20.0     83.0        4  
2         10.0    100.0        2  
3          NaN      NaN        5  
4         30.0      4.0        1
#################3

# Perform the first ordered merge: tx_weather
tx_weather = pd.merge_ordered(austin,houston)

# Print tx_weather
print(tx_weather)

# Perform the second ordered merge: tx_weather_suff
tx_weather_suff = pd.merge_ordered(austin,houston,on='date',suffixes=['_aus','_hus'])

# Print tx_weather_suff
print(tx_weather_suff)

# Perform the third ordered merge: tx_weather_ffill
tx_weather_ffill = pd.merge_ordered(austin,houston,on='date',suffixes=['_aus','_hus'],fill_method='ffill')

# Print tx_weather_ffill
print(tx_weather_ffill)
#..............................................
        date ratings
0 2016-01-01  Cloudy
1 2016-01-04   Rainy
2 2016-01-17   Sunny
3 2016-02-08  Cloudy
4 2016-03-01   Sunny
        date ratings_aus ratings_hus
0 2016-01-01      Cloudy      Cloudy
1 2016-01-04         NaN       Rainy
2 2016-01-17       Sunny         NaN
3 2016-02-08      Cloudy         NaN
4 2016-03-01         NaN       Sunny
        date ratings_aus ratings_hus
0 2016-01-01      Cloudy      Cloudy
1 2016-01-04      Cloudy       Rainy
2 2016-01-17       Sunny       Rainy
3 2016-02-08      Cloudy       Rainy
4 2016-03-01      Cloudy       Sunny

<script.py> output:
            date ratings
    0 2016-01-01  Cloudy
    1 2016-01-04   Rainy
    2 2016-01-17   Sunny
    3 2016-02-08  Cloudy
    4 2016-03-01   Sunny
            date ratings_aus ratings_hus
    0 2016-01-01      Cloudy      Cloudy
    1 2016-01-04         NaN       Rainy
    2 2016-01-17       Sunny         NaN
    3 2016-02-08      Cloudy         NaN
    4 2016-03-01         NaN       Sunny
            date ratings_aus ratings_hus
    0 2016-01-01      Cloudy      Cloudy
    1 2016-01-04      Cloudy       Rainy
    2 2016-01-17       Sunny       Rainy
    3 2016-02-08      Cloudy       Rainy
    4 2016-03-01      Cloudy       Sunny
############################

# Merge auto and oil: merged
merged = pd.merge_asof(auto,oil,left_on='yr',right_on='Date')

# Print the tail of merged
print(merged.tail())

# Resample merged: yearly
yearly = merged.resample('A',on='Date')[['mpg','Price']].mean()

# Print yearly
print(yearly)

# print yearly.corr()
print(yearly.corr())
#.............................
      mpg  cyl  displ  hp  weight  accel         yr  origin             name  \
387  27.0    4  140.0  86    2790   15.6 1982-01-01      US  ford mustang gl   
388  44.0    4   97.0  52    2130   24.6 1982-01-01  Europe        vw pickup   
389  32.0    4  135.0  84    2295   11.6 1982-01-01      US    dodge rampage   
390  28.0    4  120.0  79    2625   18.6 1982-01-01      US      ford ranger   
391  31.0    4  119.0  82    2720   19.4 1982-01-01      US       chevy s-10   

          Date  Price  
387 1982-01-01  33.85  
388 1982-01-01  33.85  
389 1982-01-01  33.85  
390 1982-01-01  33.85  
391 1982-01-01  33.85  
                  mpg  Price
Date                        
1970-12-31  17.689655   3.35
1971-12-31  21.111111   3.56
1972-12-31  18.714286   3.56
1973-12-31  17.100000   3.56
1974-12-31  22.769231  10.11
1975-12-31  20.266667  11.16
1976-12-31  21.573529  11.16
1977-12-31  23.375000  13.90
1978-12-31  24.061111  14.85
1979-12-31  25.093103  14.85
1980-12-31  33.803704  32.50
1981-12-31  30.185714  38.00
1982-12-31  32.000000  33.85
            mpg     Price
mpg    1.000000  0.948677
Price  0.948677  1.000000

<script.py> output:
          mpg  cyl  displ  hp  weight  accel         yr  origin             name  \
    387  27.0    4  140.0  86    2790   15.6 1982-01-01      US  ford mustang gl   
    388  44.0    4   97.0  52    2130   24.6 1982-01-01  Europe        vw pickup   
    389  32.0    4  135.0  84    2295   11.6 1982-01-01      US    dodge rampage   
    390  28.0    4  120.0  79    2625   18.6 1982-01-01      US      ford ranger   
    391  31.0    4  119.0  82    2720   19.4 1982-01-01      US       chevy s-10   
    
              Date  Price  
    387 1982-01-01  33.85  
    388 1982-01-01  33.85  
    389 1982-01-01  33.85  
    390 1982-01-01  33.85  
    391 1982-01-01  33.85  
                      mpg  Price
    Date                        
    1970-12-31  17.689655   3.35
    1971-12-31  21.111111   3.56
    1972-12-31  18.714286   3.56
    1973-12-31  17.100000   3.56
    1974-12-31  22.769231  10.11
    1975-12-31  20.266667  11.16
    1976-12-31  21.573529  11.16
    1977-12-31  23.375000  13.90
    1978-12-31  24.061111  14.85
    1979-12-31  25.093103  14.85
    1980-12-31  33.803704  32.50
    1981-12-31  30.185714  38.00
    1982-12-31  32.000000  33.85
                mpg     Price
    mpg    1.000000  0.948677
    Price  0.948677  1.000000
#################################################
