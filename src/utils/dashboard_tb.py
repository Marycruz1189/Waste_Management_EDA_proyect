import streamlit as st
from PIL import Image
import pandas as pd
import os 
import requests
path = os.path.dirname(__file__)
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import seaborn as sns
import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import utils.visualization_tb as vis
st.set_option('deprecation.showPyplotGlobalUse', False)

def configuracion():
    st.set_page_config(page_title='Waste Management', page_icon=':electric_plug:', layout="wide")

def menu_home():
    st.title('¡Welcome to the EDA project Waste Management in Spain')
    st.write('WHAT A WASTE: A national review of solid waste management')
   

def menu_data():    
    dir = os.path.dirname
    path = os.path.dirname(__file__)
    csv_path = dir(dir(path)) + os.sep + 'reports' + os.sep+'waste_management_cleaned.csv'
    df = pd.read_csv(csv_path)
    st.dataframe(df)
    st.pyplot(vis.most_generation_graph(df))
    st.pyplot(vis.most_disposal_graph(df))
    st.pyplot(vis.correlation_variables(df))
    st.pyplot(vis.time_collected(df))
    st.pyplot(vis.time_typedisposal(df))
    st.pyplot(vis.correlation_gdp_kg(df))
    st.pyplot(vis.correlation_pop_tn(df))
    st.pyplot(vis.correlation_gdp_kg(df))


def menu_api(): 
    url= "http://localhost:6060/token_id?token_id=Y4290783D"
    json_api = requests.get(url).json()
    st.write(json_api)


   
   






