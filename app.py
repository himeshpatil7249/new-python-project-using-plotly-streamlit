import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

df = pd.read_csv('india.csv')
s = list(df['State'].unique())
s.insert(0,'Overall India')

st.sidebar.title('India App')
states = st.sidebar.selectbox('Select an Option',s)

primary = st.sidebar.selectbox('Select an Primary Parameter ',sorted(df.columns[4:]))

secondary = st.sidebar.selectbox('Select an Secondary Parameter ',sorted(df.columns[4:]))

btn = st.sidebar.button('Click viz Data')

if btn:

    if states == 'Overall India':
        #plot for india
        #fig = px.scatter_mapbox(df,lat='Latitude',lon='Longitude',zoom=3, size=primary, color=secondary,mapbox_style='carto=positron')
        #st.plotly_chart(fig)

        fig = px.scatter_map(df,lat='Latitude',lon='Longitude',zoom=4 , size = primary, color=secondary,hover_name='District',map_style='open-street-map',color_continuous_scale='YlOrRd' )
        st.plotly_chart(fig)

    else:
        select_state = df[df['State'] == states]

        fig = px.scatter_map(select_state, lat='Latitude', lon='Longitude', zoom=5, size=primary, color=secondary,
                             hover_name='District', map_style='open-street-map', color_continuous_scale='YlOrRd')
        st.plotly_chart(fig)
