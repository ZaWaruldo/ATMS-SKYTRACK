import dash
from dash import html, Input, Output
import dash_bootstrap_components as dbc


# Create the About modal component
def get_about_modal():
    return dbc.Modal(
        [
            dbc.ModalHeader("About"),
            dbc.ModalBody([
                html.Div("This is pre-release PHX flight logs and track Analyser."),
                html.Div("Use the sidebar navigation links to perform pre-processing and analysis on logs.")
            ]),
            dbc.ModalBody([
                html.Div("Feedback and comments:"),
                html.Div("Hamad Alawadhi"),
                html.Div("Tel: +971 55 9738886"),
                html.A("dans442@dans.gov.ae", href="mailto:dans442@dans.gov.ae", style={"text-decoration": "underline", "color": "primary"})
            ]),
            dbc.ModalFooter(
                dbc.Button("Close", id="close", className="ml-auto")
            ),
        ],
        id="about-modal",
        is_open=False,  # Initially closed
    )

# Callback to toggle modal visibility
def setup_about_modal_callback(app):
    @app.callback(
        Output("about-modal", "is_open"),
        [Input("about-navlink", "n_clicks"), Input("close", "n_clicks")],
        [dash.dependencies.State("about-modal", "is_open")],
    )
    def toggle_modal(open_click, close_click, is_open):
        # Check if the "About" NavLink or the "Close" button was clicked
        if open_click or close_click:
            return not is_open
        return is_open
