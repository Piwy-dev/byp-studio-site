window.onload = function() {
    // Dark mode switcher
    const toggleButton = document.getElementById('dark-mode-switcher');
    const body = document.body;
    const bottom = document.querySelector('.bottom');

    toggleButton.addEventListener('change', function() {
        body.classList.toggle('dark');
        bottom.classList.toggle('dark');
    });

    // Language switcher
    const languageSwitcher = document.getElementById('languageSwitcher');

    languageSwitcher.addEventListener('change', function() {
        const newLanguage = this.value;
        const currentPath = window.location.pathname;
        const newPath = currentPath.replace(/^\/[a-z]{2}\//, '/' + newLanguage + '/');
        window.location.href = newPath;
    });
}
