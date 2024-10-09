"""
Создаю БД и таблицы для хранения финансовой информации
Автор: Евгений Петров
Почта: p174@mail.ru
Дата: 09.10.2024
"""

import psycopg2


import settings
import work_postgresql


def main():
    """Основной код и логика программы.
    """
    DB_NAME : str = settings.KOMPASS_DBNAME
    DB_USER : str = settings.KOMPASS_USER_DB
    DB_PASSWORD : str = settings.KOMPASS_PASSWORD_DB

    db_connect = work_postgresql.connect_to_db(DB_NAME, DB_USER, DB_PASSWORD)

    db_connect.close()


if __name__ == "__main__":
 
    main()

