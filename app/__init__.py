from flask import Flask
from flask_cors import CORS


def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    from .app import proxy_bp
    app.register_blueprint(proxy_bp)

    return app
