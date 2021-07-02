# IMPORTS
import streamlit as st
# import geopandas as gpd
# import matplotlib.cm as cm
# from matplotlib.pyplot import imread
# # import numpy as np
# import folium
# from folium.features import GeoJsonPopup, GeoJsonTooltip
# from folium import plugins
# from folium.plugins import Fullscreen
# from streamlit_folium import folium_static
import streamlit.components.v1 as components
# from pathlib import Path
import platform
import os

import pandas as pd

# from pivottablejs import pivot_ui
# import plotly
import plotly.express as px
# import missingno as msno
from datetime import datetime

stdir = os.getcwd() # streamlit app dir

# Configure for wide layout
st.set_page_config(layout="wide")

#%% App
# Configure app layout and sidebar menu
st.sidebar.title('NRAR Web Apps')

selection = st.sidebar.radio("Go to",['Home','Compliance Data Viz','Trade-Off Analysis','About'])

st.sidebar.title('About')

st.sidebar.info("NRAR's interdisciplinary behavioural and cost optimisation model: A collection of Streamlit web apps for data analysis, data visualisation and exploratory modelling")

## HELPER FUNCTIONS ##


if selection == 'Compliance Data Viz':
    
    st.markdown('# Compliance Data — Sunburst Plot ')
    
    if platform.system() == 'Darwin':
        casedetails_path = 'data/compliance_dataviz/Case Details.csv'
        enfactionscount_path = 'data/compliance_dataviz/Enforcement actions — count.csv'
        enfactionsdetails_path = 'data/compliance_dataviz/Enforcement actions — description.csv'
    else:
        casedetails_path = os.path.join(stdir,'streamlit/data/compliance_dataviz/Case Details.csv')
        enfactionscount_path = os.path.join(stdir, 'streamlit/data/compliance_dataviz/Enforcement actions — count.csv')
        enfactionsdetails_path = os.path.join(stdir,'streamlit/data/compliance_dataviz/Enforcement actions — description.csv')
    
    custom_date_parser = lambda x: datetime.strptime(x, "%b-%y")
    nan_values_list = ["NaN",' ']
    df_casedetails=pd.read_csv(casedetails_path, na_values=nan_values_list, parse_dates=['Received Date','Finalisation Date'], date_parser=custom_date_parser, index_col=0)
    df_enfactions_count=pd.read_csv(enfactionscount_path, na_values=nan_values_list, index_col=0)
    df_enfactions_description=pd.read_csv(enfactionsdetails_path, parse_dates=['Enforcement Action Date'], date_parser=custom_date_parser, na_values=nan_values_list, index_col=0)
    df_casedetails['Received Date'] = df_casedetails['Received Date'].dt.strftime("%b-%y")
    df_casedetails['Finalisation Date'] = df_casedetails['Finalisation Date'].dt.strftime("%b-%y")
    df_enfactions_description['Enforcement Action Date'] = df_enfactions_description['Enforcement Action Date'].dt.strftime("%b-%y")
    df_casedetails.sort_values('Received Date', inplace=True)
        
    
    def plot_sunburst():
        path_title = ', '.join(level_list)
        df = df_casedetails.groupby(level_list).count().reset_index()
        df['count'] = df.iloc[:,-1:]
        fig = px.sunburst(df, path=level_list, values='count', width=900, height=900)
        fig.update_layout(title=path_title)
        st.plotly_chart(fig)
    
    with st.form(key='columns_in_form'):
        st.markdown('### **Select ordering of variables**')
        cols = st.beta_columns(5)
        level_1 = cols[0].selectbox('Level 1', ['Industry', 'LGA', 'WSP', 'Received Date', 'Finalisation Date', 'Offences','Finalisation Reason', 'none'], key='a', index=5)
        level_2 = cols[1].selectbox('Level 2', ['Industry', 'LGA', 'WSP', 'Received Date', 'Finalisation Date', 'Offences','Finalisation Reason', 'none'], key='b', index=6)
        level_3 = cols[2].selectbox('Level 3', ['Industry', 'LGA', 'WSP', 'Received Date', 'Finalisation Date', 'Offences','Finalisation Reason', 'none'], key='c', index=1)
        level_4 = cols[3].selectbox('Level 4', ['Industry', 'LGA', 'WSP', 'Received Date', 'Finalisation Date', 'Offences','Finalisation Reason', 'none'], key='d', index=7)
        level_5 = cols[4].selectbox('Level 5', ['Industry', 'LGA', 'WSP', 'Received Date', 'Finalisation Date', 'Offences','Finalisation Reason', 'none'], key='e', index=7)
        st.write('Press submit to update the plot')
        submitted = st.form_submit_button('Submit')
        
    if submitted:
        level_list = [level_1, level_2, level_3, level_4, level_5]
        # items to be removed
        unwanted = {'none'}
        level_list = [ele for ele in level_list if ele not in unwanted]
        #level_list
        plot_sunburst()
            

        
