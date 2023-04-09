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
        
    @app.route("/<language>/games")
    def games(language):
        if language == 'fr':
            return render_template('fr/games.html')
        elif language == 'nl':
            return render_template('nl/games.html')
        else:
            return render_template('en/games.html')
        
    @app.route("/<language>/games/byp-quiz")
    def byp_quiz(language):
        if language == 'fr':
            return render_template('fr/games/byp-quiz.html')
        elif language == 'nl':
            return render_template('nl/games/byp-quiz.html')
        else:
            return render_template('en/games/byp-quiz.html')
        
    @app.route("/<language>/bots")
    def bots(language):
        if language == 'fr':
            return render_template('fr/bots.html')
        elif language == 'nl':
            return render_template('nl/bots.html')
        else:
            return render_template('en/bots.html')
        
    @app.route("/<language>/bots/gkb")
    def gkb(language):
        if language == 'fr':
            return render_template('fr/bots/gkb.html')
        elif language == 'nl':
            return render_template('nl/bots/gkb.html')
        else:
            return render_template('en/bots/gkb.html')
        
    @app.route("/<language>/bots/gkb/privacy-policy")
    def privacy_gkb(language):
        if language == 'fr':
            return render_template('fr/bots/gkb/privacy-policy.html')
        elif language == 'nl':
            return render_template('nl/bots/gkb/privacy-policy.html')
        else:
            return render_template('en/bots/gkb/privacy-policy.html')
        
    @app.route("/<language>/bots/gkb/terms-of-services")
    def terms_gkb(language):
        if language == 'fr':
            return render_template('fr/bots/gkb/terms-of-services.html')
        elif language == 'nl':
            return render_template('nl/bots/gkb/terms-of-services.html')
        else:
            return render_template('en/bots/gkb/terms-of-services.html')
        
    return app
