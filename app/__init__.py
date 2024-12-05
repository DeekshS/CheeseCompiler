from flask import Flask
from app.routes import home, compile  # Import blueprints

def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(home, url_prefix='/')  # Home blueprint at the root '/'
    app.register_blueprint(compile, url_prefix='/compile')  # Compile blueprint at '/compile'

    return app
