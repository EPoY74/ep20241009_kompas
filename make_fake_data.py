"""Генерируем фейковые данные для 
БД в тетовом задании
"""
from datetime import date, datetime
import random
from typing import List

from faker import Faker
import tqdm

from psycopg2.extensions import connection

from create_table import read_file
import work_postgresql


def generate_users_table(inner_db_conn: connection, fake: Faker):

    """Генерирует таблицу users_compass
    с моковыми данными
    """
    # По другому  генератор даты данные не берет, хотя должен.
    start_date: date = date(1997, 1, 1)
    end_date: date = date(2010, 10, 1)

    # db_connect: connection = work_postgresql.conn_to_db()

    for i in tqdm.tqdm(range(10000)):
        sql_name : str  = fake.name()
        sql_email: str = str(i) + fake.ascii_email()
        sql_account_open_day: str =  fake.date_between(start_date='-5y')
        sql_phone_number: str = fake.phone_number()

        # Когда передаешь строку - не может почему-то распарсить
        # Приходится действовать явно через конструктор date
        # Это ошибка. Надо зафиксить.
        sql_birthday: str = fake.date_between_dates(date_start=start_date, date_end=end_date)
        # print(f"{i}. {sql_name}")

        # формирую sql запрос
        sql_query: str = read_file(("./sql/add_users_data.sql"))

        # формирую данные, передаваемые в sql запрос
        sql_datas = (sql_name,
                    sql_birthday,
                    sql_account_open_day,
                    sql_email,
                    sql_phone_number,
                    'False')

        # Пишем запрос в БД
        work_postgresql.write_to_db_without_closing(inner_db_conn, sql_query, tuple(sql_datas))

    # Закрыываю соединение с БД после его использования.
    work_postgresql.close_connect(inner_db_conn)



def generate_account_table(inner_db_conn: connection):
    """Генерирует таблицу account_table 

    Args:
        inner (connection): Соединение с БД
    """


    # Заполняем таблицу
    # запрос на получение даты заключения договора
    sql_query:str = read_file("./sql/read_account_open_date.sql")

    # Запрос на добавление данных в таблицу
    sql_query_add: str = read_file("./sql/add account_data.sql")

    i: int = 1
    for i in tqdm.tqdm(range(5, 100000)):
        client_id  = i
        account_number = str(("408 07 810 0 "
                          + str(random.randint(1,9999)).rjust(4,'0')
                          + " 0 "
                          + str(i).rjust(7,'0')))
        currency = '810'
        balance = 0
        account_type = "Текущий"

        #Получаю дату заключение договора клииента
        sql_data_i:tuple = (i,)
        sql_responces = work_postgresql.read_one_db(inner_db_conn, sql_query, sql_data_i)
        for row in sql_responces:
            created_date = str(row)

        # Формирую массив для наполение таблицы данными
        sql_data = (client_id, 
                           account_number,
                           currency,
                           balance,
                           account_type,
                           created_date)
        work_postgresql.write_to_db_without_closing(inner_db_conn, sql_query_add, sql_data)



def generate_operations_table(inner_db_conn: connection, fake: Faker, max_clients:int):
    """
    Генерирует таблицу operations_compass
    с моковыми данными

    Args:
        inner_db_conn (connection): Соединение с БД
        fake (Faker): Экземпляр класса Faaker
        max_clients (int): Число клиентов, для скольких генерирум описание
    """


    are_data: List[tuple] = []
    i: int = 1
    # max_clients = 100

    for i in tqdm.tqdm(range(1, max_clients)):
        sql_account_id : str  = str(i)

        #Получаю дату заключение договора клииента
            # Заполняем таблицу
        # запрос на получение даты заключения договора
        sql_query:str = read_file("./sql/read_account_open_date.sql")
        sql_data_i:tuple = (i,)
        sql_responces = work_postgresql.read_one_db(inner_db_conn, sql_query, sql_data_i)

        for row in sql_responces:
            created_date = str(row)

            # По другому  генератор даты данные не берет, хотя должен.
        # print(created_date.split('-')) Изза этой какашки расссыпается прогресс бар?

        # Распаковываю кортеж
        year, month, day = map(int, created_date.split('-'))
        start_date: date = datetime(year, month, day)
        end_date: date = datetime(2024, 10, 1)


        # Генерирую произвольное количество операций
        iter_amount: int = 0
        for iter_amount in range(random.randint(10, 50)):
            sql_amount: int = random.randint(-50000,50000)
            # Убираю ноль, что бы не плодить сущности
            if sql_amount == 0:
                sql_amount  = iter_amount

            if sql_amount < 0 :
                sql_operation_type = "Кредит"
                operation_description = f"Оплата покупки {iter_amount}"
            elif sql_amount > 0:
                sql_operation_type = "Дебет"
                operation_description = f"Получение дохода {iter_amount}"
            else:
                sql_operation_type = f"Ошибка {iter_amount}"
                operation_description = f"Ошибка {iter_amount}"

            sql_authorization_day: str = (
                fake.date_time_between(start_date=start_date, end_date=end_date)
                )
            sql_transaction_date = sql_authorization_day

            # формирую sql запрос
            sql_query: str = read_file(("./sql/add_operations_data.sql"))

            # формирую данные, передаваемые в sql запрос
            sql_datas = (sql_account_id,
                        sql_amount,
                        sql_operation_type,
                        sql_authorization_day,
                        sql_transaction_date,
                        operation_description,
                        'False',)
            # print(sql_authorization_day)
            # print(sql_datas)

            # Пишем запрос в БД
            work_postgresql.write_to_db_without_close_and_commit(
                inner_db_conn, sql_query, tuple(sql_datas)
                )
        inner_db_conn.commit()
            # are_data.append(sql_datas)

    # Закрыываю соединение с БД после его использования.
    work_postgresql.close_connect(inner_db_conn)
    return are_data


def main():
    """
    Основной код программы.
    """
      # Формируем экземпляр класса Faker
    main_fake = Faker('ru_Ru')
    db_connect: connection = work_postgresql.conn_to_db()

    # Генерируем таблицу users_compass. Сгенерировали.
    # generate_users_table(main_fake)

    # generate_account_table(db_connect)
    generate_operations_table(db_connect, main_fake, 110000)
    work_postgresql.close_connect(db_connect)


if __name__ == "__main__":
    # Тут запускаю код, если мы его используем не как библиотеку
    
    main()
