from dash import Dash, html, dcc, Input, Output, State 
import dash_bootstrap_components as dbc 
import subprocess 
import sys

dropdown = dbc.DropdownMenu(
    [
        dbc.DropdownMenuItem("1. RDR data extraction", header=True),
        dbc.DropdownMenuItem("Extract CAT004", disabled=True),
        dbc.DropdownMenuItem("Extract CAT011", disabled=True),
        dbc.DropdownMenuItem("Extract CAT034/48", disabled=True),
        dbc.DropdownMenuItem("Extract CAT021", disabled=True),
        dbc.DropdownMenuItem("Extract CAT062"),
        dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem("2. Processing", header=True),
        # dbc.DropdownMenuItem("Active item", active=True),
        dbc.DropdownMenuItem("Process CAT062 Data", id="cat062-button-p"),
        dbc.DropdownMenuItem("Generate CAT062 Stats", id="cat062-button-s"),
        dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem("3. Log Parsing", header=True),
        dbc.DropdownMenuItem("CDS1/CDS2", disabled=True),
        html.P(
            '''Search and collect logs based on flight data. Dataset includes
            TRK, MSG, FTMPLA, AFTN, SYSIA, FDB.''',
            className="text-muted px-4",
        ),
        dbc.DropdownMenuItem("Clients", disabled=True),
        html.P(
            '''Search and collect logs from selected clients pbased on flight data. Dataset includes
            CWP, MON, FDB, AFTN, FSP.''',
            className="text-muted px-4",
        ),
        dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem("Clear Cache", disabled=True),
        html.P(
            "Remove filtered logs but preserve CAT062 processing",
            className="text-muted px-4",
        ),
    ],
    label="Main Menu",
)


def preprocess_layout():
    return html.Div(
        [
        dbc.Row([dbc.Col(dropdown,md=4),]),
        html.Hr(),
        html.Div(id='log-console',
                children='...',
                className="min-vh-70 p-2 bg-light text-dark border rounded-3 overflow-auto",
                style={'height': '300px', 'overflowY': 'scroll'})
        ],
        )

