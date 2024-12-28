from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

def flight_analysis_layout():
    # Define flight points (example data)
    flight_data = {
        "latitude": [25.276987, 24.453884],  # Example latitudes (Dubai, Abu Dhabi, Sharjah)
        "longitude": [55.296249, 54.377344],  # Example longitudes
        "labels": ["Dubai", "Abu Dhabi", "Sharjah"]  # Tooltip labels
    }

    # Create the OpenStreetMap figure
    fig = go.Figure(go.Scattermapbox(
        lat=flight_data["latitude"],
        lon=flight_data["longitude"],
        mode='markers',
        marker=dict(
            size=10,
            color='blue',
            symbol='circle',
        ),
        text=flight_data["labels"],  # Add tooltips
        hoverinfo="text"
    ))

    # Update layout for OpenStreetMap
    fig.update_layout(
        mapbox=dict(
            style="open-street-map",  # Use OpenStreetMap
            center=dict(lat=25.276987, lon=55.296249),  # Center map on Dubai
            zoom=7,  # Adjust zoom level
        ),
        margin=dict(l=0, r=0, t=0, b=0)  # Remove margins for a clean look
    )

    tab1_content = html.Div(
            [
                dbc.Alert(
                    [
                        html.I(className="bi bi-exclamation-triangle-fill me-2"),
                        "Interactive OpenStreetMap showing flight data.",
                    ],
                    color="info",
                    className="mb-4",
                ),
            ],
        className="mt-3",
    )

    tab2_content = html.Div(
            [
            dcc.Graph(
                id="flight-map",
                figure=fig,
                style={"height": "80vh"}  # Set height of Graph to 80% of viewport
            ),
            ],
        className="mt-3",
    )


    tabs = dbc.Tabs(
        [
            dbc.Tab(tab1_content, label="Statistics",className="p-4 border"),
            dbc.Tab(tab2_content, label="Flight Map",className="p-4 border"),
        ]
    )


    return html.Div(
        [
            html.H4("Flight Analysis", className="mb-4"),
            html.Hr(),
            tabs,


        ],
        style={
            "height": "90vh",  # Make the Div fill the viewport height
            "display": "flex",
            "flexDirection": "column"  # Ensure content stacks vertically
        }
    )
