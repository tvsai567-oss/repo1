import pandas as pd
import pandas as np
data = {
    'property_id': [1,2,3,4,5],
    'price':[250000,300000,150000,400000,350000],
    'size_sqft': [1500,2000,1200,2500,1800], 
    'date_listed': ['2023-01-15','2023-02-20','2023-03-10','2023-04-05','2023-05-01'],
    'year_built':[1990,2005,1980,2010,2000]
}
df = pd.DataFrame(data)
print(df)

df[ 'price_per_sqft']= df['price']/ df['size_sqft']

df[ 'price_per_sqft']= df['price_per_sqft'].round(2)

print(df)

df['date_listed']= pd.to_datetime(df['date_listed'])

df[ 'date_listed'] = df['date_listed'].dt.month

print(df)

df[ 'is_new_construction']= np.where(df['year_built']>= 2020,1, 0)

print(df)