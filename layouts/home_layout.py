import dash_bootstrap_components as dbc
import os, re
import pandas as pd
from dash import html, dcc

from config import cat062_directory, cat004_directory,cat062_stats_file

def natural_sort_key(s):
    """Extract numeric parts for natural sorting."""
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def home_layout():
    # Get the list of files in each directory
    cat062_files = os.listdir(cat062_directory)
    cat004_files = os.listdir(cat004_directory)
    
    df = pd.read_csv(cat062_stats_file)

    # Join the list of files into a string with newline characters
    cat062_files.sort(key=natural_sort_key)
    cat062_files_str = '\n'.join(cat062_files)
    # cat04_files_str = '\n'.join(cat004_files)

    cat062_card = dbc.Card(
        dbc.CardBody([
                dbc.CardHeader("CAT062 Processed Files", className="card-title"),
                dcc.Textarea(
                    id='cat062-file-list',
                    value=cat062_files_str,
                    className="card-text p-3 bg-light text-dark border overflow-auto",
                    style={'width': '100%', 'height': '300px'},
                    readOnly=True
                ),
                dbc.CardFooter(f"{len(cat062_files)} files found."),
                ]),
            style={"width": "18rem"},
            ),

    row_content_1 = dbc.Stack(
        [
        html.Div(cat062_card),
        html.Div(cat062_card),
        html.Div(cat062_card),
        ],
        direction="horizontal",
        gap=2,
        ),
    
    cat062_stats_table = dbc.Table()

    return html.Div([
        dbc.Row(row_content_1,justify="center"),
        html.Hr(),
        dbc.Row(cat062_stats_table,justify="center"),
        ])