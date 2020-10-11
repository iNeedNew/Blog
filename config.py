class Configuration:
    """Общий конфиг"""

    SECRET_KEY = 'key'


class Development(Configuration):
    """Конфиг для разработки"""
    DEBUG = True




configs = {
    'development':Development,
}
