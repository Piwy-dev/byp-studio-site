// Change the language of the page by changing the URL
window.onload = function() {
    var languageSwitcher = document.getElementById('languageSwitcher');
    
    languageSwitcher.addEventListener('change', function() {
        var selectedLanguage = languageSwitcher.value;
        var currentUrl = window.location.href;
        var currentLanguage = currentUrl.split('/')[3]; // assuming the language prefix is always the third element of the URL path
        var newUrl = currentUrl.replace(currentLanguage, selectedLanguage);
        window.location.href = newUrl;
    });
};
