from random import randint

from faker import Faker

from app.models import User, Article, Comment


def red_text(item):
    return f'\033[031m{str(item)}\033[0m'


def green_text(item):
    return f'\033[032m{str(item)}\033[0m'


def purple_text(item):
    return f'\033[035m{str(item)}\033[0m'


class GenerateData:
    def __init__(self):
        self.fake_data = Faker()

    def __generate(self, object_info: dict, count: int = 0):
        """Метод генерации данных"""
        print(f'Генерация {object_info["whom"]} в количестве: {count}')
        data = []
        number_of_errors_during_generation = 0
        for i in range(count):

            one_data = []
            for index, data_generation_method in enumerate(object_info['data_generation_methods']):

                # Если текщий индекс есть в индексах методов, которые принимают аргументы
                if index in object_info['indexes_of_methods_that_have_attributes']:
                    generated_data_particle = data_generation_method(*object_info['method_arguments'][index])
                    one_data.append(generated_data_particle)
                    continue

                # Если текщий индекс метода есть в индексе методов на проверку
                if index in object_info['method_indexes_that_require_validation']:
                    validation_method = object_info['validation_methods'][index]
                    generated_data_particle = data_generation_method()

                    response = validation_method(generated_data_particle)

                    if response['exception']['error']:
                        print('Error:', response['exception']['msg'], response['exception']['code'])
                        break

                    if response['data']:
                        print('Already in the data base')
                        break

                    one_data.append(generated_data_particle)
                    continue

                one_data.append(data_generation_method())

            if one_data:
                print(green_text(f'Данные №{i} сгенерированы.'))
                data.append(tuple(one_data))
            else:
                print(red_text(f'Ошибка в генерации данных №{i}.'))
                number_of_errors_during_generation += 1

        print(
            f'Соотношение генерации данных: {green_text(len(data) - number_of_errors_during_generation)}/{red_text(number_of_errors_during_generation)}')
        successful_addition = 0
        error_while_adding = 0

        # Комитить данные по частям
        for i in range(((len(data)) // 100) + 1):
            method_sending_to_db = object_info['method_of_sending_data_to_database']
            response = method_sending_to_db(data[i * 500:(i + 1) * 500])

            if response['exception']['error']:
                print(red_text('Ошибка при добавлении части данных'))
                print(response['exception']['msg'])
                print(response['exception']['code'])
                error_while_adding += 1

            response_commit = object_info['service'].commit()
            if response_commit['exception']['error']:
                print(red_text('Ошибка при комите части данных'))
                print(response['exception']['msg'])
                print(response['exception']['code'])
                error_while_adding += 1

            else:
                print(green_text('Часть данных закомичено.'))
                successful_addition += 1

        print(f'Данные добавлены: {green_text(successful_addition)}/{red_text(error_while_adding)}')


    """
    object_info = {
    'whom':
    'service': Объект класса-сервиса 
    'data_generation_methods': объекты функций/методов, которые будут генерировать данные
    'method_indexes_that_require_validation': индексы методов для проверки
    'validation_methods': методы для проверки данных
    'method_of_sending_data_to_database': метод загрузки данных в опер. пам.
    'method_arguments': аргументы метода
    'indexes_of_methods_that_have_attributes': индексы методов, у которых есть аргументы 
    }
    
    """


    def generate_users(self, count: int = 0):
        object_info = {
            'whom': 'пользователей',
            'service': User(),
            'data_generation_methods': [self.fake_data.first_name, self.fake_data.email,
                                        self.fake_data.password, self.fake_data.future_datetime],
            'method_indexes_that_require_validation': [0, 1],
            'validation_methods': [User().check_username, User().check_email],
            'method_of_sending_data_to_database': User().add_users,

            'method_arguments': [],
            'indexes_of_methods_that_have_attributes': []
        }

        self.__generate(object_info=object_info, count=count)

    def generate_articles(self, count: int = 0):
        count_users = User().get_count_users()['data']['count_users']
        object_info = {
            'whom': 'пользователей',
            'service': Article(),
            'data_generation_methods': [randint, randint, self.fake_data.text, self.fake_data.text,
                                        self.fake_data.future_datetime],
            'method_indexes_that_require_validation': [],
            'validation_methods': [],
            'method_of_sending_data_to_database': Article().add_articles,
            'method_arguments': [(1, count_users), (1, 5), (50,), (250,)],
            'indexes_of_methods_that_have_attributes': [0, 1, 2, 3]
        }

        self.__generate(object_info=object_info, count=count)

    def generate_comments(self, count: int = 0):
        count_users = User().get_count_users()['data']['count_users']
        count_articles = Article().get_count_articles()['data']['count_articles']
        object_info = {
            'whom': 'комментариев',
            'service': Comment(),
            'data_generation_methods': [randint, randint, randint, self.fake_data.text,
                                        self.fake_data.future_datetime],
            'method_indexes_that_require_validation': [],
            'validation_methods': [],
            'method_of_sending_data_to_database': Comment().add_comments,
            'method_arguments': [(1, count_users), (1, count_users), (1, count_articles), (420,)],
            'indexes_of_methods_that_have_attributes': [0, 1, 2, 3]
        }
        self.__generate(object_info=object_info, count=count)

