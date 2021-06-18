import pandas as pd
import plotly.express as px

data = pd.read_csv("./datasets/kc_house_data.csv")

data['date'] = pd.to_datetime(data['date'])

# data['house_age'] = 'new_house';

data.loc[data['date'] < '2015-01-01', 'house_age'] = 'old_house'
data.loc[data['date'] >= '2015-01-01', 'house_age'] = 'new_house'

data.loc[data['bedrooms'] == 1, 'dormitory_type'] = 'studio'
data.loc[data['bedrooms'] == 2, 'dormitory_type'] = 'apartment'
data.loc[data['bedrooms'] > 2, 'dormitory_type'] = 'house'

data.loc[data['condition'] <= 2, 'condition_type'] = 'bad'
data.loc[(data['condition'] == 3) | (data['condition'] == 4), 'condition_type'] = 'regular'
data.loc[data['condition'] >= 5, 'condition_type'] = 'good'

data['condition'] = data['condition'].astype(str)

data = data.drop(['sqft_living15', 'sqft_lot15'], axis=1)

data['yr_built'] = pd.to_datetime(data['yr_built'].astype(str), format='%Y')
data['yr_renovated'] = pd.to_datetime(data.loc[data['yr_renovated'] != 0, 'yr_renovated'].astype(str), format='%Y')

oldest_construction = data[['yr_built']].sort_values('yr_built')
oldest_renovation = data[['yr_renovated']].sort_values('yr_renovated')

houses_with_two_floors = data[data['floors'] == 2]

houses_with_two_floors.to_csv('./datasets/report_aula02.csv', index=False)

regular_houses = data[data['condition_type'] == 'regular'].count()[0]

bad_houses_with_waterfront = data[(data['condition_type'] == 'bad') & (data['waterfront'] == 1)].count()[0]

good_and_new_houses = data[(data['condition_type'] == 'good') & (data['house_age'] == 'new_house')].count()[0]

most_expensive_studio = data[['id', 'dormitory_type', 'price']][data['dormitory_type'] == 'studio']\
       .sort_values('price', ascending=False)

apartments_renovated_in_2015 = data[(data['dormitory_type'] == 'apartment') & (data['yr_renovated'] == '2015-01-01')].count()[0]

house_with_more_bedrooms = data[['id', 'dormitory_type', 'bedrooms']][(data['dormitory_type'] == 'house')]\
       .sort_values('bedrooms', ascending=False)

get_by_column_name = data[['id', 'date', 'price', 'floors', 'zipcode']]
get_by_index = data.iloc[:, 0:3]
get_by_index2 = data.iloc[:, 7]
get_by_index3 = data.iloc[:, 16]

get_by_index_and_name = data.loc[:, ['id', 'date', 'price', 'floors', 'zipcode']]

get_by_boolean = data.loc[:, [True, True, True, False, False, False,
       False, True, False, False, False, False,
       False, False, False, False, True,
       False, False, False, False, False]]

data_mapa = data[['id', 'lat', 'long', 'price']]

mapa = px.scatter_mapbox(data_mapa, lat='lat', lon='long', hover_name='id', hover_data=['price'], color_discrete_sequence=['fuchsia'], zoom=300,
               height=300)
mapa.update_layout(mapbox_style='open-street-map')
mapa.update_layout(height=600, margin={'r':0, 't':0, 'l':0, 'b':0})

mapa.show()

mapa.write_html('./datasets/mapa_house_rocket.html')

# print(get_by_boolean)