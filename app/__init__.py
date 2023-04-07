import os
from flask import Flask, render_template, g, current_app, redirect, request

def create_app(test_config=None):
    """
    Create and configure the app.
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    lang = 'en'

   # create the pages
    @app.route("/")
    def index():
        print(request.accept_languages)
        return redirect('/{}/home'.format(lang))

    @app.route("/<language>/home")
    def home(language):
        global lang
        if language == 'fr':
            lang = 'fr'
            return render_template('fr/home.html')
        elif language == 'nl':
            lang = 'nl'
            return render_template('nl/home.html')
        else:
            lang = 'en'
            return render_template('en/home.html')

    @app.route("/<language>/gkb")
    def gkb(language):
        if language == 'fr':
            return render_template('fr/gkb.html')
        elif language == 'nl':
            return render_template('nl/gkb.html')
        else:
            return render_template('en/gkb.html')
        
    @app.route("/<language>/gkb/privacy-policy")
    def privacy_gkb(language):
        if language == 'fr':
            return render_template('fr/gkb/privacy-policy.html')
        elif language == 'nl':
            return render_template('nl/gkb/privacy-policy.html')
        else:
            return render_template('en/gkb/privacy-policy.html')
        
    @app.route("/<language>/gkb/terms-of-services")
    def terms_gkb(language):
        if language == 'fr':
            return render_template('fr/gkb/terms-of-services.html')
        elif language == 'nl':
            return render_template('nl/gkb/terms-of-services.html')
        else:
            return render_template('en/gkb/terms-of-services.html')
        
    @app.route("/<language>/games")
    def games(language):
        if language == 'fr':
            return render_template('fr/games.html', active='games')
        elif language == 'nl':
            return render_template('nl/games.html', active='games')
        else:
            return render_template('en/games.html', active='games')
        
    @app.route("/<language>/bots")
    def bots(language):
        if language == 'fr':
            return render_template('fr/bots.html', active='bots')
        elif language == 'nl':
            return render_template('nl/bots.html', active='bots')
        else:
            return render_template('en/bots.html', active='bots')
        
    return app
