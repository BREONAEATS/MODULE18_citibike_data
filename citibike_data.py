import pandas as pd

# Number of Months
n = 12
citibike_full_data = pd.DataFrame()

# For Loop to read each month's CSV and add month's data to full dataframe

for x in range(1, n+1):
    
    if x < 10:
        month = f'0{x}'
    else:
        month = x
    
    df = pd.read_csv(f'citibike-data/2022/JC-2022{month}-JC-201708-citibike-tripdata.csv.zip')
    
    citibike_full_data = pd.concat([citibike_full_data, df])

citibike_full_data