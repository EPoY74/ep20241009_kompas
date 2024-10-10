"""
Создаю таблицы для хранения финансовой информации
Автор: Евгений Петров
Почта: p174@mail.ru
Дата: 09.10.2024
"""

# import psycopg2
# from psycopg2.extensions import connection


# import settings
import work_postgresql


def main():
    """Основной код и логика программы.
    """
    db_connect = work_postgresql.conn_to_db()
    
    db_connect.close()


if __name__ == "__main__":
 
    main()

