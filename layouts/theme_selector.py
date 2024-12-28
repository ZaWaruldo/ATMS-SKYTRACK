from dash import dcc, Output, Input, clientside_callback
import os

# List of available themes in `dbc.themes`
themes = [
    "CERULEAN", "COSMO", "CYBORG", "DARKLY", "FLATLY", "JOURNAL",
    "LITERA", "LUMEN", "LUX", "MATERIA", "MINTY", "MORPH", "PULSE",
    "QUARTZ", "SANDSTONE", "SIMPLEX", "SKETCHY", "SLATE", "SOLAR",
    "SPACELAB", "SUPERHERO", "UNITED", "VAPOR", "YETI", "ZEPHYR"
]

# Base path for local themes (e.g., assets/themes)
theme_base_path = "/assets/themes"

# Function to create the theme selector dropdown
def get_theme_selector(default_theme="DARKLY"):
    return dcc.Dropdown(
        id="theme-selector",
        options=[{"label": theme, "value": theme} for theme in themes],
        value=default_theme,  # Default theme
        clearable=False,
        className='dbc text-primary'
    )

# Clientside callback for dynamic theme switching
def setup_clientside_callback():
    clientside_callback(
        """
        (selectedTheme) => {
            const stylesheets = document.querySelectorAll('link[rel="stylesheet"]');
            const themeBasePath = "/assets/themes/";
            const newThemeUrl = `${themeBasePath}${selectedTheme.toLowerCase()}.css`;

            // Update the stylesheet link for the theme
            stylesheets.forEach(link => {
                if (link.href.includes("themes")) {
                    link.href = newThemeUrl;
                }
            });

            return window.dash_clientside.no_update;
        }
        """,
        Output("theme-output", "children"),  # Dummy output
        Input("theme-selector", "value"),
    )

# Helper function to ensure the 'assets/themes' directory exists
def check_theme_directory():
    if not os.path.exists("assets/themes"):
        raise FileNotFoundError("The 'assets/themes' directory does not exist. Please run the script to download the themes.")