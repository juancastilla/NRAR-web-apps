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
    
    # Set paths to load data
    if platform.system() == 'Darwin':
        casedetails_path = 'data/compliance_dataviz/Case Details.csv'
        enfactionscount_path = 'data/compliance_dataviz/Enforcement actions — count.csv'
        enfactionsdetails_path = 'data/compliance_dataviz/Enforcement actions — description.csv'
    else:
        casedetails_path = os.path.join(stdir,'streamlit/data/compliance_dataviz/Case Details.csv')
        enfactionscount_path = os.path.join(stdir, 'streamlit/data/compliance_dataviz/Enforcement actions — count.csv')
        enfactionsdetails_path = os.path.join(stdir,'streamlit/data/compliance_dataviz/Enforcement actions — description.csv')
    
    # Load the data
    
    @st.cache
    def load_data():
        custom_date_parser = lambda x: datetime.strptime(x, "%b-%y")
        nan_values_list = ["NaN",' ']
        df_casedetails = pd.read_csv(casedetails_path, na_values=nan_values_list, parse_dates=['Received Date','Finalisation Date'], date_parser=custom_date_parser, index_col=0)
        df_enfactions_count = pd.read_csv(enfactionscount_path, na_values=nan_values_list, index_col=0)
        df_enfactions_description = pd.read_csv(enfactionsdetails_path, parse_dates=['Enforcement Action Date'], date_parser=custom_date_parser, na_values=nan_values_list, index_col=0)
        df_casedetails['Received Date'] = df_casedetails['Received Date'].dt.strftime("%b-%y")
        df_casedetails['Finalisation Date'] = df_casedetails['Finalisation Date'].dt.strftime("%b-%y")
        df_enfactions_description['Enforcement Action Date'] = df_enfactions_description['Enforcement Action Date'].dt.strftime("%b-%y")
        return df_casedetails
        
    df_casedetails = load_data()
    
    with st.form(key='Sunburst comparison'):
        st.markdown('### **Select ordering of variables**')
        cols_form = st.beta_columns(5)
        
        l1_L = cols_form[0].selectbox('Level 1 (left)', ['Industry', 'LGA', 'WSP', 'Received Date', 'Finalisation Date', 'Offences','Finalisation Reason', 'none'], key='l1_L', index=5)
        l1_R = cols_form[0].selectbox('Level 1 (right)', ['Industry', 'LGA', 'WSP', 'Received Date', 'Finalisation Date', 'Offences','Finalisation Reason', 'none'], key='l1_R', index=5)

        l2_L = cols_form[1].selectbox('Level 2 (left)', ['Industry', 'LGA', 'WSP', 'Received Date', 'Finalisation Date', 'Offences','Finalisation Reason', 'none'], key='l2_L', index=6)
        l2_R = cols_form[1].selectbox('Level 2 (right)', ['Industry', 'LGA', 'WSP', 'Received Date', 'Finalisation Date', 'Offences','Finalisation Reason', 'none'], key='l2_R', index=6)
        
        l3_L = cols_form[2].selectbox('Level 3 (left)', ['Industry', 'LGA', 'WSP', 'Received Date', 'Finalisation Date', 'Offences','Finalisation Reason', 'none'], key='l3_L', index=1)
        l3_R = cols_form[2].selectbox('Level 3 (right)', ['Industry', 'LGA', 'WSP', 'Received Date', 'Finalisation Date', 'Offences','Finalisation Reason', 'none'], key='l3_R', index=1)
        
        l4_L = cols_form[3].selectbox('Level 4 (left)', ['Industry', 'LGA', 'WSP', 'Received Date', 'Finalisation Date', 'Offences','Finalisation Reason', 'none'], key='l4_L', index=7)
        l4_R = cols_form[3].selectbox('Level 4 (right)', ['Industry', 'LGA', 'WSP', 'Received Date', 'Finalisation Date', 'Offences','Finalisation Reason', 'none'], key='l4_R', index=7)

        l5_L = cols_form[4].selectbox('Level 5 (left)', ['Industry', 'LGA', 'WSP', 'Received Date', 'Finalisation Date', 'Offences','Finalisation Reason', 'none'], key='l5_L', index=7)
        l5_R = cols_form[4].selectbox('Level 5 (right)', ['Industry', 'LGA', 'WSP', 'Received Date', 'Finalisation Date', 'Offences','Finalisation Reason', 'none'], key='l5_R', index=7)
        
        st.write('Press submit to update the plot')
        submitted = st.form_submit_button('Submit')
    
    if submitted:
        
        level_list_L = [l1_L, l2_L, l3_L, l4_L, l5_L]
        level_list_R = [l1_R, l2_R, l3_R, l4_R, l5_R]
        # items to be removed
        unwanted = {'none'}
        level_list_L = [ele for ele in level_list_L if ele not in unwanted]
        level_list_R = [ele for ele in level_list_R if ele not in unwanted]
        
        #level_list
        col1, col2 = st.beta_columns(2)
        
        
        with col1:
            path_title_L = ', '.join(level_list_L)
            df_L = df_casedetails.groupby(level_list_L).count().reset_index()
            df_L['count'] = df_L.iloc[:,-1:]
            fig_L = px.sunburst(df_L, path=level_list_L, values='count', width=900, height=900)
            fig_L.update_layout(title=path_title_L)
            st.plotly_chart(fig_L)
        with col2:
            path_title_R = ', '.join(level_list_R)
            df_R = df_casedetails.groupby(level_list_R).count().reset_index()
            df_R['count'] = df_R.iloc[:,-1:]
            fig_R = px.sunburst(df_R, path=level_list_R, values='count', width=900, height=900)
            fig_R.update_layout(title=path_title_R)
            st.plotly_chart(fig_R)
            

        
