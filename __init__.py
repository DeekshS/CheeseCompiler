from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register the routes after creating the app
    from app.routes import compile, home
    app.register_blueprint(home)
    app.register_blueprint(compile)

    return app
