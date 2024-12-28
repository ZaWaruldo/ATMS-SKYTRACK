import os
import sys
import subprocess
import dash
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.graph_objs import Bar
from dash import Dash, dcc, html, Input, Output, State, dash_table
import dash_bootstrap_components as dbc

#import functions
from config import cat004_directory, cat062_directory, cat062_stats_file
from layouts.home_layout import home_layout
from layouts.preprocess_layout import preprocess_layout
from layouts.flight_analysis_layout import flight_analysis_layout
from layouts.theme_selector import get_theme_selector, setup_clientside_callback, check_theme_directory
from layouts.about import get_about_modal, setup_about_modal_callback

#define directories
cat062_dir = cat062_directory
cat004_dir = cat004_directory
#define stats file
cat062_statistics_file=cat062_stats_file

subprocess.run([sys.executable, 'Scripts/init.py'])

# Ensure the 'assets/themes' directory exists
try:
    check_theme_directory()
except FileNotFoundError as e:
    print(e)
    exit(1)

# Default theme
default_theme = "/assets/themes/darkly.css"
# Set up clientside callback
setup_clientside_callback()

# Initialize Dash app
app = Dash(
    __name__,
    external_stylesheets=[default_theme,dbc.icons.BOOTSTRAP],

)

app.title = "ATMS SKYTRACK"
app._favicon="assets/icons/favicon.ico"

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "maxWidth": "60rem",     # Equivalent to 960px if the root font size is 16px
    "width": "100%",
}

card = dbc.Card(
    [
        dbc.CardImg(src="/static/images/favicon-32x32.png", top=True),
        dbc.CardBody(
            [
                html.H4("Card title", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and "
                    "make up the bulk of the card's content.",
                    className="card-text",
                ),
                dbc.Button("Go somewhere", color="primary"),
            ]
        ),
    ],
    style={"width": "18rem"},
)

sidebar = html.Div(
    [
        html.H4("ATMS-SKYTRACK", className="h5", style={"text-align": "center"}),
        html.P("Flight track history viewer made simple", className="card-text", style={"text-align": "center"}),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink([html.I(className="bi bi-house-door me-2"), "Home"], href="/", active="exact"),
                dbc.NavLink([html.I(className="bi bi-gear me-2"), "Pre-process"], href="/pre-process", active="exact"),
                dbc.NavLink([html.I(className="bi bi-airplane-engines me-2"), "Flight Analysis"], href="/flight-analysis", active="exact"),
                dbc.NavLink([html.I(className="bi bi-question-circle me-2"), "About"],href="#",id="about-navlink", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
        html.Hr(),
        html.P("Select Theme", className="lead"),
        get_theme_selector(),
        html.Div(id="theme-output", style={"display": "none"}),
        ],
    style=SIDEBAR_STYLE,
)


app.layout = (
    [
        dcc.Location(id="url", refresh=False),  # Added dcc.Location to track URL
        sidebar,
        get_about_modal(),
        html.Div(id="page-content", style=CONTENT_STYLE,)
    ]
)



@app.callback(Output('page-content','children'),[Input('url','pathname')])
def display_page(pathname):
    if pathname =='/':
        return home_layout()
    elif pathname =='/pre-process':
        return preprocess_layout()
    elif pathname =='/flight-analysis':
        return flight_analysis_layout()
    else:
        return home_layout()

# Callback to open and close the modal
setup_about_modal_callback(app) 

if __name__ == '__main__':
    app.run(debug=True)
