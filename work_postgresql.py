"""
Модуль для работы с БД PosgresQl
Автор: Евгений Б. Петров
Почта: epoy74@gmail.com
"""
import time
from typing import List

import psycopg2
from psycopg2.extensions import connection
from psycopg2.extensions import cursor

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


def conn_to_db():
    """Выполняет подключение к БД,
    Дополнительных переметров передавать не требуется.
    Параметры считываются из переменных окружения операцинной системы.
    Данная функция написана для уменьшения количества кода, 
    так как подключение требуетс очень часто.

    Returns:
        _type_: Подключение к БД postgresql
    """
    DB_NAME_CONSTANT : str = settings.KOMPASS_DBNAME  # pylint: disable=invalid-name
    DB_USER : str = settings.KOMPASS_USER_DB  # pylint: disable=invalid-name
    DB_PASSWORD : str = settings.KOMPASS_PASSWORD_DB  # pylint: disable=invalid-name

    db_connect = connect_to_db(DB_NAME_CONSTANT, DB_USER, DB_PASSWORD)
    return db_connect

def close_connect(inner_db_connect: connection):
    """Закрываю соединение с БД inner_bd_connect.
    Закрытие вынес в отдельную функцию,
    так как нужно иногда обрабатывать много sql запросов,
    а открывать соединение на отдельный запрос - не выгодно

    Args:
        inner_db_connect (connection): Закрываемое соединение
    """

    inner_db_connect.close()
    if inner_db_connect.closed == 1 :
        print(f"Соединение закрыто {getting_time()}")
        divide_line(50)

def connect_to_db(
        db_name: str,
        db_user: str,
        db_pass: str,
        db_host:str = "localhost",
        db_port: str = "5432") -> connection:
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

    :return: класс connection для подключение к БД
    """
    try:
        print(f"Подключение к БД {getting_time()}")
        connect = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_pass,
            host=db_host,
            port=db_port,
        )
        if connect:
            print(f"БД {db_name} подключена {getting_time()}")
        else:
            print(f"БД {db_name} не подключена {getting_time()}")
    except psycopg2.Error as err:
        print(f"Ошибка: \n:{err}\n{getting_time()}")
        raise err

    return connect


def write_to_db(db_connect: connection,
                sql_query_con: str,
                inner_var: tuple = None,
                is_sql_text: bool = False):
    """
    Запись запроса sql_query_con (str)
    с параметрами (при необходимости) inner_var (tuple, optional) 
    в БД PostgresQL по соединению db_connect (connection)
    
    Если установлен  is_sql_text (bool) True то 
    выводим текст sql запроса в консоль , 
    Args:
        db_connect (connection):соединение с БД
        sql_query_con (str): запрос в БД
        is_sql_text (bool): выводить или нет текст sql запроса в консоль
        inner_var (tuple, optional): параметры sql запроса, если есть. Defaults to None.

    Raises:
        err: Если падает -  пробрасываю ошибку дальше для обработки
    """
    try:
        with db_connect.cursor() as curr:
            curr.execute(sql_query_con,
                         inner_var)
            db_connect.commit()
            if is_sql_text:
                print (f"Запрос \n{sql_query_con}\n выполнен в {getting_time()}")
    except psycopg2.Error as err:
        print(f"Ошибка: \n:{err}\n{getting_time()}")
        raise err
    finally:
        db_connect.close()
        if db_connect.closed == 1 :
            print(f"Соединение закрыто {getting_time()}")
            divide_line(50)


def write_to_db_without_closing(db_connect: connection,
                sql_query_con: str,
                inner_var: tuple = None,
                is_sql_text: bool = False):
    """
    Запись запроса в БД PostgresQL.
    СОЕДИНЕНИЕ НЕ ЗАКРЫВАЕТСЯ!!!
    ТРЕБУЕТСЯ ЗАКРЫТЬ СОЕДИНЕНИЕ ОТДЕЛЬНО!!!
    sql_connect -  класс соединение с БД.
    sql_query_con - обрабатываемй sql запрос
    inner_var - переменные, передаваемые в запрос (Defaults to None)
    is_sql_text(bool) - Выводить в консоль(Defaults to False)
    :return:
    """
    try:
        with db_connect.cursor() as curr:
            curr.execute(sql_query_con,
                         inner_var)
            db_connect.commit()
            if is_sql_text:
                print(f"Запрос \n{sql_query_con}\n выполнен в {getting_time()}")
    except psycopg2.Error as err:
        print(f"Ошибка: \n:{err}\n{getting_time()}")
        raise err
def write_to_db_without_close_and_commit(db_connect: connection,
                sql_query_con: str,
                inner_var: tuple = None,
                is_sql_text: bool = False):
    """
    Запись запроса в БД PostgresQL.
    СОЕДИНЕНИЕ НЕ ЗАКРЫВАЕТСЯ!!!
    ТРЕБУЕТСЯ ЗАКРЫТЬ СОЕДИНЕНИЕ ОТДЕЛЬНО!!!
    sql_connect -  класс соединение с БД.
    sql_query_con - обрабатываемй sql запрос
    inner_var - переменные, передаваемые в запрос (Defaults to None)
    is_sql_text(bool) - Выводить в консоль(Defaults to False)
    :return:
    """
    try:
        with db_connect.cursor() as curr:
            curr.execute(sql_query_con,
                         inner_var)
            if is_sql_text:
                print(f"Запрос \n{sql_query_con}\n выполнен в {getting_time()}")
    except psycopg2.Error as err:
        print(f"Ошибка: \n:{err}\n{getting_time()}")
        raise err

def read_one_db(db_connect: connection,
                sql_query: str,
                inner_vars: tuple = None) -> tuple:

    """
    --- НЕ ЗАКРЫВАЕТ СОЕДИНЕНИЕ ---
    Возврящает одну запись.
    Читает запрос sql_query
    с переменными (если нужны) inner_vars
    из БД с соединением db_connect

    Args:
        db_connect (connection): Соединение с БД
        sql_query (str): запрос
        inner_vars (tuple, optional): переменные, передаваемые в запрос.. Defaults to None.

    Raises:
        err: Если падает -  пробрасываю ошибку дальше для обработки

    Returns:
       tuple :  Информация из БД
    """

    curr: cursor

    try:
        with db_connect.cursor() as curr:
            curr.execute(sql_query,inner_vars)
            sql_responce: tuple|None = curr.fetchone()

    except psycopg2.Error as err:
        print(f"Ошибка: \n:{err}\n{getting_time()}")
        raise err

    return sql_responce


def read_all_db(db_connect: connection,
                sql_query: str,
                inner_vars: tuple = None) -> tuple:

    """
    --- НЕ ЗАКРЫВАЕТ СОЕДИНЕНИЕ ---
    Возврящает все записи.
    Читает запрос sql_query
    с переменными (если нужны) inner_vars
    из БД с соединением db_connect

    Args:
        db_connect (connection): Соединение с БД
        sql_query (str): запрос
        inner_vars (tuple, optional): переменные, передаваемые в запрос.. Defaults to None.

    Raises:
        err: Если падает -  пробрасываю ошибку дальше для обработки

    Returns:
       tuple :  Информация из БД
    """

    curr: cursor

    try:
        with db_connect.cursor() as curr:
            curr.execute(sql_query,inner_vars)
            sql_responce: tuple|None = curr.fetchall()

    except psycopg2.Error as err:
        print(f"Ошибка: \n:{err}\n{getting_time()}")
        raise err

    return sql_responce
