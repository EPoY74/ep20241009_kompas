"""
Модуль для работы с БД PosgresQl
Автор: Евгений Б. Петров
Почта: epoy74@gmail.com
"""
import time
from typing import List

import psycopg2
import settings


def divide_line(quantity: int = 30):
    """Выыводит в консоль заданное количество дефисов
    для визуально разделения контента 

    Args:
        quantity (int, optional): Требуемое количетво дефисов. Defaults to 30.
    """
    print("-" * quantity)



def getting_time() -> List:
    """
    Возвращает текущее время в неформатированном виде
    :return:
    """
    time_now_get = time.localtime(time.time())
    time_now_out_get: List = [time_now_get.tm_mday,
                              time_now_get.tm_mon,
                              time_now_get.tm_year,
                              time_now_get.tm_hour,
                              time_now_get.tm_min,
                              time_now_get.tm_sec,
                              ]
    return time_now_out_get

def connect_to_db(
        db_name: str,
        db_user: str,
        db_pass: str,
        db_host:str = "localhost",
        db_port: str = "5432"):
    """
    Подключается к базе данных с заданными параметрами.
    Возвращает подключение.
    ВНИМАНИЕ! Библиотека psycopg2 на 19.08.2024 не закрывает
     подключения к БД с контекстным менеджером.
      Обязательно следить за закрытиями соединений

    :param db_name: Имя подключаемой БД
    :param db_user: Имя пользователя БД
    :param db_pass: Пароль пользователя БД
    :param db_host: Хост БД, по умолчанию "localhost"
    :param db_port: Порт подключения, по умолчанию "5432"

    :return: Подключение к БД
    """
    print(f"Подключение к БД {getting_time()}")
    connect = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_pass,
        host=db_host,
        port=db_port,
    )
    if connect:
        print(f"БД подключена {getting_time()}")

    return connect


def write_to_db(db_connect, sql_query_con: str):
    """
    Запись запроса в БД PostgresQL
    sql_con: - запрос в БД
    :return:
    """
    try:
        with db_connect.cursor() as curr:
            curr.execute(sql_query_con)
            db_connect.commit()
            print(f"Запрос {sql_query_con} выполнен в {getting_time()}")
            db_connect.close()
        print(f"Connection is closed {getting_time()}")
        divide_line(50)
    except psycopg2.Error as err:
        print(f"Ошибка: \n:{err}\n{getting_time()}")
        raise err
