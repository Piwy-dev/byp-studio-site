window.onload = function() {
    /* Dark mode switcher */
    const toggleButton = document.getElementById('dark-mode-switcher');
    const body = document.body;
    const bottom = document.querySelector('.bottom');
    
    // Check if the dark mode is enabled in the localStorage object
    const isDarkModeEnabled = localStorage.getItem('darkModeEnabled') === 'true';

    // Set the initial state of the dark mode
    if (isDarkModeEnabled) {
        body.classList.add('dark');
        bottom.classList.add('dark');
        toggleButton.querySelector('input').checked = true;
    }

    toggleButton.addEventListener('change', function () {
        const isChecked = toggleButton.querySelector('input').checked;
        body.classList.toggle('dark', isChecked);
        bottom.classList.toggle('dark', isChecked);
        
        // Store the state of the dark mode in the localStorage object
        localStorage.setItem('darkModeEnabled', isChecked);
    });

    /* Language switcher */
    const languageSwitcher = document.getElementById('languageSwitcher');

    languageSwitcher.addEventListener('change', function() {
        const newLanguage = this.value;
        const currentPath = window.location.pathname;
        const newPath = currentPath.replace(/^\/[a-z]{2}\//, '/' + newLanguage + '/');
        window.location.href = newPath;
    });
}
