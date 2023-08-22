document.addEventListener("DOMContentLoaded", function() {
    let contentDiv = document.getElementById("game"); // Change this to match your main container's ID
    let themeSelect = document.querySelectorAll("input[type='radio'][name='theme']");

    // Apply the selected theme
    function applyTheme(theme) {
        contentDiv.classList.remove("standard", "elemental", "fantasy");
        contentDiv.classList.add(theme);
    }

    // Listen for changes in radio button selection
    themeSelect.forEach(radio => {
        radio.addEventListener("change", function() {
            if (radio.checked) {
                applyTheme(radio.value);
            }
        });
    });
    let playAgainButton = document.querySelector(".replay");
    playAgainButton.addEventListener("click", function() {
        applyTheme(selectedTheme);
    });
});

