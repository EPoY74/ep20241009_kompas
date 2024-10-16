"""Генерируем фейковые данные для 
БД в тетовом задании
"""
from datetime import date

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

    sql_query:str = read_file("./sql/read_client_id_from_users.sql")

    sql_responces: tuple = work_postgresql.read_one_db(inner_db_conn, sql_query)

    for sql_resp in sql_responces:
        print(sql_resp)
    print(sql_responces)

    work_postgresql.divide_line()
    sql_query:str = read_file("./sql/read_rows_from_users.sql")

    sql_responces: tuple = work_postgresql.read_all_db(inner_db_conn, sql_query)

    for sql_resp in sql_responces:
        print(sql_resp)
    # print(sql_responces)


def main():
    """
    Основной код программы.
    """
      # Формируем экземпляр класса Faker
    # main_fake = Faker('ru_Ru')
    db_connect: connection = work_postgresql.conn_to_db()

    # Генерируем таблицу users_compass. Сгенерировали.
    # generate_users_table(main_fake)

    generate_account_table(db_connect)
    work_postgresql.close_connect(db_connect)

if __name__ == "__main__":
    main()
