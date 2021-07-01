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
# import streamlit.components.v1 as components
# from pathlib import Path
# import platform
# import os


#%% App
# Configure app layout and sidebar menu
st.sidebar.title('Navigation')

selection = st.sidebar.radio("Go to",['Home','Compliance Data Viz','Trade-Off Analysis','About'])

st.sidebar.title('About')

st.sidebar.info("This app is maintained by The Regulators")


# if selection == 'Compliance Data Viz':

    # if platform.system() == 'Darwin':
    #     markdown = read_markdown_file('submit_page.md')
    # else:
    #     markdown = read_markdown_file(os.path.join(stdir,'submit_page.md'))

    # st.markdown(markdown, unsafe_allow_html=True)

    #components.iframe("https://docs.google.com/forms/d/e/1FAIpQLSeOgQtYLJALacZQfwF2Nb5RMWOqg_ODVyyEXoStBKHekfg66w/viewform?usp=sf_link", height=1500, scrolling=True)

# if selection == 'Trade-Off Analysis':

    # if platform.system() == 'Darwin':
    #     markdown = read_markdown_file('about_page.md')
    # else:
    #     markdown = read_markdown_file(os.path.join(stdir,'about_page.md'))

    # st.markdown(markdown, unsafe_allow_html=True)

# Main app page — groundwater model display and search map
# NOTE: this could be refactored into a separate .py script and import on app start

# if selection == 'Find Models':

    # st.title('GroMoPo — Groundwater Model Portal')

    # st.write("Sharing groundwater model data, knowledge and insights more easily through a portal of regional and global numerical groundwater models. The first priority is archiving existing models, but the repository could eventually archive model input and scripts for translating commonly used geospatial datasets into model inputs.")

    # map = folium.Map(zoom_start=3, crs='EPSG{}'.format(epsg),min_zoom=3,max_bounds=True)
    # folium.TileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', attr='x',name='OpenTopoMap').add_to(map)
    # folium.TileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',name='ArcWorldImagery', attr='x').add_to(map)


    # rgroup, marker_cluster, mlayer = plot_map(all_gdf,img,popup=popup)

    # rgroup.add_to(map)
    # marker_cluster.add_to(map)
    # mlayer.add_to(map)

    # map.add_child(folium.LayerControl())

    # Fullscreen().add_to(map)

    # folium_static(map, height=700, width=1400)
