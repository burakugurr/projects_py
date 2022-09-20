# Importing necessary modules
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from dash import dcc, html
import plotly_express as px
from flask import Flask
import pandas as pd
import dash


# Server
server = Flask(__name__)
app = dash.Dash(__name__, server = server, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Read the data from PSQL w/ psycopg2
df = pd.read_csv('london-clean.csv')


# Visual Components

# Comp-A

countfig = go.FigureWidget()
#  id,downo,daytype,SubSystem,StartStn, JourneyTime,Gender,Product line
#  EndStn,EntTime,ExTime,Zones,JourneyType, Unit price,Quantity,Rating
#  DailyCapping,FullFare,DiscountFare,FinalProduct, 
countfig.add_scatter(name = )




# Design & Layout
app.layout = html.Div()


# Run the app
app.run_server(debug= True)
