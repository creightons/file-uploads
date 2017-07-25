from flask import render_template

def apply_routes(app):

    @app.route('/')
    def index():
        return render_template('index.html')
