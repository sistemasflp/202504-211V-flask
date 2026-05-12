from flask import Flask
from app.routes import base_bp, post_bp, comments_bp, users_bp
from app.utils.db import close_db_connection, get_db_connection
from app.models.user import ensure_user_table

def create_app():
    app = Flask(__name__)

    with app.app_context():
        get_db_connection()
        ensure_user_table()

    app.teardown_appcontext(close_db_connection)

    # Registrar Blueprints
    app.register_blueprint(base_bp)
    app.register_blueprint(post_bp)
    app.register_blueprint(comments_bp)
    app.register_blueprint(users_bp)

    return app
