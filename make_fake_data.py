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

    start_date = date(1997, 1, 1)
    end_date = date(2010, 10, 1)



    print(fake.name())
    print(fake.ascii_email())
    print(fake.date_between(start_date='-5y'))
    print(fake.phone_number())
    
    # Когда передаешь строку - не может почему-то распарсить
    # Приходится действовать явно через конструктор date
    # Это ошибка. Надо зафиксить.
    print(fake.date_between_dates(date_start=start_date, date_end=end_date))
    
if __name__ == "__main__":
    main()
