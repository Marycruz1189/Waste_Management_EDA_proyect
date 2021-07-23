
import streamlit as st
from PIL import Image
import pandas as pd
import os
import sys
dir = os.path.dirname
import requests
src_path = (dir(dir(__file__)))
sys.path.append(src_path)
import utils.dashboard_tb as ft
path = os.path.dirname(__file__)
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import utils.visualization_tb as vis
st.set_option('deprecation.showPyplotGlobalUse', False)

ft.configuracion()

menu = st.sidebar.selectbox('Menu:',
                            options=["No selected", "Welcome", "Data_Clean", "Flask_API" ])

st.title("WASTE MANAGEMENT SPAIN")
img = Image.open( dir(dir(path)) + os.sep + 'resources' + os.sep+ 'waste.jpg')
st.image(img,use_column_width=True)

if menu == 'Welcome':
    ft.menu_home()
        
if menu == 'Data_Clean':
    ft.menu_data()
    
if menu == 'Flask_API':
    ft.menu_api()




    
 




