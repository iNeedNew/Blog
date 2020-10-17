from secure_config import SecureConfiguration as sc

class Configuration:
    """Общий конфиг"""

    SECRET_KEY = 'key'


class Development(Configuration):
    """Конфиг для разработки"""
    DEBUG = True

    MYSQL_DATABASE_HOST = sc.MYSQL_DATABASE_HOST
    MYSQL_DATABASE_PORT = sc.MYSQL_DATABASE_PORT
    MYSQL_DATABASE_USER = sc.MYSQL_DATABASE_USER
    MYSQL_DATABASE_PASSWORD = sc.MYSQL_DATABASE_PASSWORD
    MYSQL_DATABASE_DB = sc.MYSQL_DATABASE_DB


configs = {
    'development':Development,
}
