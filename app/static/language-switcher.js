// Change the language of the page by changing the URL

var languageSwitcher = document.getElementById('languageSwitcher');

languageSwitcher.addEventListener('change', function() {
    var selectedLanguage = languageSwitcher.value;
    window.location.href = '/' + selectedLanguage + window.location.pathname;
});
