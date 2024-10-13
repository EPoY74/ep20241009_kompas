"""Генерируем фейковые данные для 
БД в тетовом задании
"""
from datetime import date

from faker import Faker


def main():
    """
    Основной код программы.
    """
    fake = Faker('ru_Ru')

    # По дугому  генератор данный не берет, хотя должен.
    start_date: date = date(1997, 1, 1)
    end_date: date = date(2010, 10, 1)

    sql_name : str  = fake.name()
    sql_email: str = fake.ascii_email()
    sql_account_open_day: str =  fake.date_between(start_date='-5y')
    sql_phone_number: str = fake.phone_number()

    # Когда передаешь строку - не может почему-то распарсить
    # Приходится действовать явно через конструктор date
    # Это ошибка. Надо зафиксить.
    sql_birthday: str = fake.date_between_dates(date_start=start_date, date_end=end_date)

if __name__ == "__main__":
    main()
