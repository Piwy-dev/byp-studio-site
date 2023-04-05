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
    
    @app.route("/en/privacy-policy")
    def privacy_en():
        return render_template('en/privacy-policy.html')
    
    @app.route("/fr/privacy-policy")
    def privacy_fr():
        return render_template('fr/privacy-policy.html')
    
    @app.route("/nl/privacy-policy")
    def privacy_nl():
        return render_template('nl/privacy-policy.html')
    
    @app.route("/en/terms-of-service")
    def terms_en():
        return render_template('en/terms-of-service.html')
    
    @app.route("/fr/terms-of-service")
    def terms_fr():
        return render_template('fr/terms-of-service.html')
    
    @app.route("/nl/terms-of-service")
    def terms_nl():
        return render_template('nl/terms-of-service.html')
    
    return app
