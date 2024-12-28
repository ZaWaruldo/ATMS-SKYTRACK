import os
import requests

# Base URL for Bootswatch themes
bootswatch_url = "https://cdn.jsdelivr.net/npm/bootswatch@5.3.2/dist"

# List of themes to download
themes = [
    "cerulean", "cosmo", "cyborg", "darkly", "flatly", "journal", "litera", "lumen",
    "lux", "materia", "minty", "morph", "pulse", "quartz", "sandstone", "simplex",
    "sketchy", "slate", "solar", "spacelab", "superhero", "united", "vapor", "yeti", "zephyr"
]

# Directory to store the themes
theme_dir = os.path.join("assets", "themes")

# Create the directory if it doesn't exist
os.makedirs(theme_dir, exist_ok=True)

# Download and save each theme
for theme in themes:
    theme_url = f"{bootswatch_url}/{theme}/bootstrap.min.css"
    local_path = os.path.join(theme_dir, f"{theme}.css")
    try:
        print(f"Downloading {theme} theme...")
        response = requests.get(theme_url)
        response.raise_for_status()
        with open(local_path, "wb") as f:
            f.write(response.content)
        print(f"Saved {theme} theme to {local_path}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {theme}: {e}")
