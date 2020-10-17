from datetime import datetime

from pymysql import MySQLError
from werkzeug.security import generate_password_hash

from app import db


class Service:
    """Класс для работы с БД"""

    def commit(self):

        try:
            db.get_db().commit()
            return {'data': None, 'exception': {'error': False, 'code': '', 'msg': ''}}

        except MySQLError as error:
            error_code, error_msg = error.args
            return {'data': None, 'exception': {'error': True, 'code': error_code, 'msg': error_msg}}

    def _get_one(self, sql, parameters=None):
        """Получить один кортеж данных"""
        cursor = db.get_db().cursor()
        try:
            if parameters is not None:
                cursor.execute(sql, parameters)
                response = cursor.fetchone()
                return {'data': response, 'exception': {'error': False, 'code': '', 'msg': ''}}
            else:
                cursor.execute(sql)
                response = cursor.fetchone()
                return {'data': response, 'exception': {'error': False, 'code': '', 'msg': ''}}
        except MySQLError as error:
            error_code, error_msg = error.args
            return {'data': None, 'exception': {'error': True, 'code': error_code, 'msg': error_msg}}

    def _get_many(self, sql, parameters=None):
        """Получить больше одного кортежа данных"""
        cursor = db.get_db().cursor()
        try:
            if parameters is not None:
                cursor.execute(sql, parameters)
                response = cursor.fetchall()
                return {'data': response, 'exception': {'error': False, 'code': '', 'msg': ''}}
            else:
                cursor.execute(sql)
                response = cursor.fetchall()
                return {'data': response, 'exception': {'error': False, 'code': '', 'msg': ''}}

        except MySQLError as error:
            error_code, error_msg = error.args
            return {'data': None, 'exception': {'error': True, 'code': error_code, 'msg': error_msg}}

    def _add_one(self, sql, parameters):
        """Получить один кортеж кортеж данных"""
        cursor = db.get_db().cursor()
        try:
            cursor.execute(sql, parameters)
            return {'data': None, 'exception': {'error': False, 'code': '', 'msg': ''}}

        except MySQLError as error:
            error_code, error_msg = error.args
            return {'data': None, 'exception': {'error': True, 'code': error_code, 'msg': error_msg}}

    def _add_many(self, sql, parameters):
        """Получить один кортеж кортеж данных"""
        cursor = db.get_db().cursor()
        try:
            cursor.executemany(sql, parameters)
            return {'data': None, 'exception': {'error': False, 'code': '', 'msg': ''}}

        except MySQLError as error:
            error_code, error_msg = error.args
            return {'data': None, 'exception': {'error': True, 'code': error_code, 'msg': error_msg}}

    def _check(self, sql, parameters=None):
        """Получить один кортеж кортеж данных"""
        cursor = db.get_db().cursor()
        try:
            if parameters is not None:
                cursor.execute(sql, parameters)
                response = cursor.fetchone()
                return {'data': bool(response), 'exception': {'error': False, 'code': '', 'msg': ''}}
            else:
                cursor.execute(sql)
                response = cursor.fetchone()
                return {'data': bool(response), 'exception': {'error': False, 'code': '', 'msg': ''}}

        except MySQLError as error:
            error_code, error_msg = error.args
            return {'data': None, 'exception': {'error': True, 'code': error_code, 'msg': error_msg}}


class User(Service):

    # ----- GET -----
    def get_users(self):
        """Получить всех пользователей"""
        sql = """
        SELECT users.* FROM users
        """
        return self._get_many(sql)

    def get_count_users(self):
        sql = """
        SELECT COUNT(users.id) as count_users FROM users
        """
        return self._get_one(sql)

    # ----- ADD -----
    def add_user(self,
                 username: str,
                 email: str,
                 password: str):
        """Добавить пользователя в бд"""

        sql = """INSERT INTO users VALUES(NULL, NULL, %s, %s, %s, NULL, NULL, NULL, NULL, NULL, %s, NULL)"""

        password_hash = generate_password_hash(password)
        create_account = datetime.utcnow()

        parameters = (username, email, password_hash, create_account)

        return self._add_one(sql, parameters)

    def add_users(self, list_users: list):
        """Добавить несколько пользователей в бд"""
        sql = """INSERT INTO users VALUES(NULL, NULL, %s, %s, %s, NULL, NULL, NULL, NULL, NULL, %s, NULL)"""

        return self._add_many(sql, list_users)

    # ----- CHECK -----
    def check_username(self, username):
        sql = """
        SELECT * FROM users WHERE users.username = (%s) LIMIT 1
        """
        parameters = (username,)
        return self._check(sql, parameters)

    def check_email(self, email):
        sql = """
        SELECT * FROM users WHERE users.email = (%s) LIMIT 1
        """
        parameters = (email,)
        return self._check(sql, parameters)


class Article(Service):
    # ----- GET -----

    def get_articles(self):
        sql = """
        SELECT articles.* FROM articles 
        """
        return self._get_many(sql)

    def get_count_articles(self):
        sql = """
        SELECT COUNT(articles.id) as count_articles FROM articles
        """
        return self._get_one(sql)

    # ----- ADD -----
    def add_articles(self, list_users: list):
        """Добавить несколько статей в бд"""
        sql = """
        INSERT INTO articles VALUES(NULL, %s, %s, %s, %s, %s, NULL)
        """

        return self._add_many(sql, list_users)


class Comment(Service):
    # ----- ADD -----
    def add_comments(self, list_users: list):
        """Добавить несколько комментариев в бд"""
        sql = """
        INSERT INTO comments VALUES(NULL, %s, %s, %s, %s, %s, NULL)
        """

        return self._add_many(sql, list_users)


class Assessment(Service):
    pass


class Category(Service):
    pass


class Report(Service):
    pass
