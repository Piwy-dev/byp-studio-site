window.onload = function () {
    const toggleButton = document.getElementById('dark-mode-switcher');
    const body = document.body;
    const bottom = document.querySelector('.bottom');

    toggleButton.addEventListener('change', function () {
        body.classList.toggle('dark');
        bottom.classList.toggle('dark');
        console.log('Dark mode toggled');
    });
}
