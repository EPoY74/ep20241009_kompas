"""
Набор функций для создания таблиц в базе даннных
Автор: ЕВгений Петров
Дата: 10.10.2024
Почта: p174@mail.ru
"""
from psycopg2.extensions import connection
import work_postgresql


def read_file(file_path: str):
    """
    Читает файл с текстом sql запроса 
    по заданному пути file_path
    
    Args:
        file_path: Имя файла, при необходиости
        указать полный путь к файлу
    Return:
        Содержимое файла
    """
    with open(file_path, "r", encoding="utf-8") as file:
        inner_sql_query : str = file.read()
    return inner_sql_query


def create_table(inner_db_connect: connection, inner_sql_query: str):
    """Функция создает таблицe с заданными параметрами
    в заданной БД

    Args:
        inner_db_connect (connection): соединение с БД, в которой создаем таблицу
        inner_sql_query (str): Запрос создания таблицы
    """
    try:
        work_postgresql.write_to_db(inner_db_connect,inner_sql_query)
    except ValueError as err:
        print(f"Ошибка выполнения:  {err}")
    else:
        print("SQL запрос для создания таблицы users выполнен успешно")
    finally:
        print("Завершение работы функции создания таблицы users")


def create_table_users():
    """Создаю таблицу users.
    Передача дополнительных переметров не требуется, так как
    все необходитом подключается в данной функции.
    """
    # Получаю содержимое файла с sql запросом
    sql_query: str = read_file("./sql/create_table_users.sql")

    # Получаю соединения с БД
    db_conn: connection = work_postgresql.conn_to_db()

    # Создаю таблицу в БД users_kompass
    create_table(db_conn,sql_query)


def create_table_account_kompass():
    """Создаем таблицу с  данными по счетам.
    Дополнительные перметр ыне требуются, так как
    все необходимое подключается в функции
    """

    # Получаю содержимое файла с sql запросом
    sql_query: str = read_file("./sql/create_table_account.sql")

    # Получаю соединения с БД
    db_conn: connection = work_postgresql.conn_to_db()

    # Создаю таблицу в БД users_kompass
    create_table(db_conn,sql_query)

def create_table_operations_kompass():
    """Создаем таблицу с операциями.
    Пареметры никакие не принимает, все 
    подключается в функции  
    """

    # Получаю содержимое файла с sql запросом
    sql_query: str = read_file("./sql/create_table_operations.sql")

    # Получаю соединения с БД
    db_conn: connection = work_postgresql.conn_to_db()

    # Создаю таблицу в БД users_kompass
    create_table(db_conn,sql_query)
