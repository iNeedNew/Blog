from pymysql import MySQLError

from app import db


def create_tables():
    with open('/home/ineednew/projects/blog/sql_scripts/create_tables.sql', mode='r') as file:
        cursor = db.get_db().cursor()
        sql_scripts = file.read().split('-----')
        print('Создание таблиц...')
        for count, sql_script in enumerate(sql_scripts, start=1):
            try:
                cursor.execute(sql_script)
                print(f'Таблица №{count} создана')
            except MySQLError as error:
                print(f'При создании таблицы №{count} произошла ошибка: {error}')

        print('Создание завершено.')


def drop_tables():
    with open('/home/ineednew/projects/blog/sql_scripts/drop_tables.sql', mode='r') as file:
        cursor = db.get_db().cursor()
        sql_scripts = file.read().split('-----')
        print('Удаление таблиц...')
        for count, sql_script in enumerate(sql_scripts, start=1):
            try:
                cursor.execute(sql_script)
                print(f'Таблица №{count} удалена')
            except MySQLError as error:
                print(f'При удалении таблицы №{count} произошла ошибка: {error}')

        print('Удаление завершено.')


def recreate():
    print('Пересозданте базы данных...')
    drop_tables()
    create_tables()
    print('Пересоздание закончено.')
