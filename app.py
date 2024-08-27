import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
st.sidebar.title('India Data Visualization')

df=pd.read_csv('India.csv')
list_of_states=list(df['State'].unique())
list_of_states.insert(0,'India Overall')

selected_state=st.sidebar.selectbox('Select A State',list_of_states)

primary=st.sidebar.selectbox('Select Primary Parameter',sorted(df.columns[5:]))
secondary=st.sidebar.selectbox('Select Secondary Parameter',sorted(df.columns[5:]))

plot=st.sidebar.button('Plot Graph')

if plot:
    if selected_state=='India Overall':
        #Plot for India
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude",size=primary,color=secondary, zoom=3, mapbox_style='carto-positron',size_max=25,color_discrete_map='Inferno')
        st.plotly_chart(fig)

    else:
        state=df[df['State']==selected_state]
        fig = px.scatter_mapbox(state, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=3,
                                mapbox_style='carto-positron', size_max=25,color_discrete_map='Inferno')
        st.plotly_chart(fig)
        # Plot for state
