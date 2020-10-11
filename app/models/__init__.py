from pymysql import MySQLError

from app import db


class Service:
    """Класс для работы с БД"""

    def _get_one(self, sql, parameters=None):
        """Получить один кортеж кортеж данных"""
        cursor = db.get_db().cursor()
        try:
            if parameters is not None:
                cursor.execute(sql, parameters)
                response = cursor.fetchone()
                return {'data': response, 'error': False}
            else:
                cursor.execute(sql)
                response = cursor.fetchone()
                return {'data': response, 'error': False}
        except MySQLError as error:
            print('Error:', error)
            return {'data': {}, 'error': True}

    def _get_many(self, sql, parameters=None):
        """Получить больше одного кортежа данных"""
        cursor = db.get_db().cursor()
        try:
            if parameters is not None:
                cursor.execute(sql, parameters)
                response = cursor.fetchall()
                return {'data': response, 'error': False}
            else:
                cursor.execute(sql)
                response = cursor.fetchall()
                return {'data': response, 'error': False}

        except MySQLError as error:
            print('Error:', error)
            return {'data': [], 'error': True}

    def _add_one(self, sql, parameters):
        """Получить один кортеж кортеж данных"""
        cursor = db.get_db().cursor()
        try:
            cursor.execute(sql, parameters)
            return {'error': False}

        except MySQLError as error:
            print('Error:', error)
            return {'error': True}

    def _add_many(self, sql, parameters):
        """Получить один кортеж кортеж данных"""
        cursor = db.get_db().cursor()
        try:
            cursor.executemany(sql, parameters)
            return {'error': False}

        except MySQLError as error:
            print('Error:', error)
            return {'error': True}

    def _check(self, sql, parameters=None):
        """Получить один кортеж кортеж данных"""
        cursor = db.get_db().cursor()
        try:
            if parameters is not None:
                cursor.execute(sql, parameters)
                response = cursor.fetchone()
                return {'flag': bool(response), 'error': False}
            else:
                cursor.execute(sql)
                response = cursor.fetchone()
                return {'flag': bool(response), 'error': False}

        except MySQLError as error:
            print('Error:', error)
            return {'flag': False, 'error': True}


class User(Service):

    def get_users(self):
        sql = """
        SELECT users.* FROM users
        """
        return self._get_many(sql)


class Article(Service):
    pass


class Comment(Service):
    pass


class Assessment(Service):
    pass


class Category(Service):
    pass


class Report(Service):
    pass
