from pymysql import MySQLError

from app import db


def red_text(text):
    return f'\033[031m{text}\033[0m'


def green_text(text):
    return f'\033[032m{text}\033[0m'

def purple_text(text):
    return f'\033[035m{text}\033[0m'


def create_tables():
    with open('/home/ineednew/projects/blog/sql_scripts/create_tables.sql', mode='r') as file:
        cursor = db.get_db().cursor()
        sql_scripts = file.read().split('-----')
        print('Создание таблиц...')
        for count, sql_script in enumerate(sql_scripts, start=1):
            try:
                name_table = sql_script.split()[2]
                cursor.execute(sql_script)
                print(f'Таблица {purple_text(name_table)} {green_text(" создана").rjust( 40 - len(name_table),".")}')
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
                name_table = sql_script.split()[4]
                cursor.execute(sql_script)
                print(f'Таблица {purple_text(name_table)} {red_text(" удалена").rjust( 40 - len(name_table),".")}')
            except MySQLError as error:
                print(f'При удалении таблицы №{count} произошла ошибка: {error}')

        print('Удаление завершено.')


def recreate():
    print('Пересозданте базы данных...')
    drop_tables()
    create_tables()
    print('Пересоздание закончено.')
