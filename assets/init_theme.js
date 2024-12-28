document.addEventListener("DOMContentLoaded", () => {
    const savedTheme = localStorage.getItem("selectedTheme") || "DARKLY"; // Default to DARKLY
    const themeBasePath = "/assets/themes/";
    const newThemeUrl = `${themeBasePath}${savedTheme.toLowerCase()}.css`;

    // Update the theme stylesheet
    const stylesheets = document.querySelectorAll('link[rel="stylesheet"]');
    stylesheets.forEach(link => {
        if (link.href.includes("themes")) {
            link.href = newThemeUrl;
        }
    });

    // Set the dropdown value to the saved theme
    const dropdown = document.querySelector("#theme-selector");
    if (dropdown) {
        dropdown.value = savedTheme;
    }
});
