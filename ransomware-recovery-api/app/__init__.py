from flask import Flask, jsonify
from flask_cors import CORS

def register_error_handlers(app):
    @app.errorhandler(400)
    def bad_request(e):
        return jsonify(error="Bad Request", detail=str(e)), 400

    @app.errorhandler(404)
    def not_found(e):
        return jsonify(error="Not Found", detail=str(e)), 404

    @app.errorhandler(500)
    def server_error(e):
        return jsonify(error="Internal Server Error"), 500

def create_app(config_obj=None):
    app = Flask(__name__)
    CORS(app)

    if config_obj:
        app.config.from_object(config_obj)
    else:
        app.config.from_object("config.DevConfig")

    from .routes.health import bp as health_bp
    from .routes.files import bp as files_bp

    app.register_blueprint(health_bp)
    app.register_blueprint(files_bp, url_prefix="/api/files")

    register_error_handlers(app)
    return app
