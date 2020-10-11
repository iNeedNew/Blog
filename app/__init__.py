from flask import Flask
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

from config import configs

db = MySQL(cursorclass=DictCursor)

def create_app(config_name: str):
    """Фабричный шаблон создания приложения"""

    app = Flask(__name__)
    app.config.from_object(configs[config_name])

    db.init_app(app)

    # Регистрация отдельных приложений
    from app.admin import admin
    app.register_blueprint(admin)

    from app.auth import auth
    app.register_blueprint(auth)

    from app.error import error
    app.register_blueprint(error)

    from app.main import main
    app.register_blueprint(main)

    from app.user import user
    app.register_blueprint(user)

    return app
