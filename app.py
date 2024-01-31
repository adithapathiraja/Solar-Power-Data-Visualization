import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from datetime import datetime

!git clone https://github.com/adithapathiraja/Solar-Power-Data-Visualization.git
%cd /content/Solar-Power-Data-Visualization

excel_file_path = '/content/Solar-Power-Data-Visualization/Dataset - Nov 01 - Dec 01 2023.xlsx'  # Replace with the path to your Excel file
df = pd.read_excel(excel_file_path)
st.write(df)
