from flask import Flask
from flask_cors import CORS


def create_app(test_config=None):
    routes = Flask(__name__)
    CORS(routes)
    routes.config['CORS_HEADERS'] = 'Content-Type'

    from .routes import proxy_bp
    routes.register_blueprint(proxy_bp)

    return routes
