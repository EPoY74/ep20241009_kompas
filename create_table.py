"""
Набор функций для создания таблиц в базе даннных
Автор: ЕВгений Петров
Дата: 10.10.2024
Почта: p174@mail.ru
"""
from psycopg2.extensions import connection
import work_postgresql


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
    все неодходитом подключается в данной функции.
    """
    with open("./sql/create_table_users.sql", "r", encoding="utf-8") as file:
        sql_query : str = file.read()
    
    db_conn: connection = work_postgresql.conn_to_db()
    create_table(db_conn,sql_query)