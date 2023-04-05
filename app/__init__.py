import os
from flask import Flask, render_template, g, current_app

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

    # create the pages
    @app.route("/")
    def main():
        return render_template('main.html')
    
    @app.route("/en/home")
    def home_en():
        return render_template('en/home.html')
    
    @app.route("/fr/home")
    def home_fr():
        return render_template('fr/home.html')
    
    @app.route("/nl/home")
    def home_nl():
        return render_template('nl/home.html')
    
    @app.route("/en/gkb")
    def gkb_en():
        return render_template('en/gkb.html')
    
    @app.route("/fr/gkb")
    def gkb_fr():
        return render_template('fr/gkb.html')
    
    @app.route("/nl/gkb")
    def gkb_nl():
        return render_template('nl/gkb.html')
    
    @app.route("/en/gkb/privacy-policy")
    def privacy_gkb_en():
        return render_template('en/gkb/privacy-policy.html')
    
    @app.route("/fr/gkb/privacy-policy")
    def privacy_gkb_fr():
        return render_template('fr/gkb/privacy-policy.html')
    
    @app.route("/nl/gkb/privacy-policy")
    def privacy_gkb_nl():
        return render_template('nl/gkb/privacy-policy.html')
    
    @app.route("/en/gkb/terms-of-service")
    def terms_gkb_en():
        return render_template('en/gkb/terms-of-service.html')
    
    @app.route("/fr/gkb/terms-of-service")
    def terms_gkb_fr():
        return render_template('fr/gkb/terms-of-service.html')
    
    @app.route("/nl/gkb/terms-of-service")
    def terms_gkb_nl():
        return render_template('nl/gkb/terms-of-service.html')
    
    return app
