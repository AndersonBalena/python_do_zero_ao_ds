from numpy import heaviside
import pandas as pd
import streamlit as st
import numpy as np
import folium
from streamlit_folium import folium_static

st.set_page_config( layout='wide' )

@st.cache( allow_output_mutation=True )
def get_data( path ):
    data = pd.read_csv( path )

    return data

path = '.\datasets\kc_house_data.csv'
data = pd.read_csv( path )

# Add new features
data['price_m2'] = data['price'] / data['sqft_lot']

# ================================
# Data Overview
# ================================
f_attributes = st.sidebar.multiselect( 'Enter columns', data.columns )
f_zipcode = st.sidebar.multiselect( 'Enter zipcode', data['zipcode'].unique())

st.title('Data Overview')

if ( f_zipcode != [] ) & ( f_attributes != [] ):
    data = data.loc[data['zipcode'].isin( f_zipcode ), f_attributes]
elif ( f_zipcode != [] ) & ( f_attributes == [] ):
    data = data.loc[data['zipcode'].isin( f_zipcode ), :]
elif ( f_zipcode == [] ) & ( f_attributes != [] ):
    data = data.loc[:, f_attributes]

st.dataframe(data)

c1, c2 = st.beta_columns((1, 1))

# Average Metrics
df1 = data[['id', 'zipcode']].groupby('zipcode').count().reset_index()
df2 = data[['price', 'zipcode']].groupby('zipcode').mean().reset_index()
df3 = data[['sqft_living', 'zipcode']].groupby('zipcode').mean().reset_index()
df4 = data[['price_m2', 'zipcode']].groupby('zipcode').mean().reset_index()

#merge
m1 = pd.merge(df1, df2, on='zipcode', how='inner')
m2 = pd.merge(m1, df3, on='zipcode', how='inner')
df = pd.merge(m2, df2, on='zipcode', how='inner')

df.columns = ['ZIPCODE', 'TOTAL HOUSES', 'PRICE', 'SQRT LIVING', 'PRICE/M2']

c1.header('Average Values')
c1.dataframe(df, height=550)

# Statistic Descriptive
num_attributes = data.select_dtypes( include=['int64', 'float64'])
media = pd.DataFrame(num_attributes.apply(np.mean))
mediana = pd.DataFrame(num_attributes.apply(np.median))
std = pd.DataFrame(num_attributes.apply(np.std))

max_ = pd.DataFrame(num_attributes.apply(np.max))
min_ = pd.DataFrame(num_attributes.apply(np.min))

df1 = pd.concat([max_, min_, media, mediana, std], axis=1).reset_index()
df1.columns = ['attributes', 'max', 'min', 'mean', 'median', 'std']

c2.header('Descriptive Analysis')
c2.dataframe(df1, height=600)

# ================================
# Densidade de Portfólio
# ================================

st.title( 'Region Overview' )

c1, c2 = st.beta_columns((1,1))
c1.header('Portofio Density')

df = data.sample(10)

#Base Map - Folium
density_map = folium.Map(location=[data['lat'].mean(),
                                   data['long'].mean()],
                                   default_zoom_start=15)

with c1:
    folium_static( density_map )