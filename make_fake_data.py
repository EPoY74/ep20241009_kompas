"""Генерируем фейковые данные для 
БД в тетовом задании
"""

from faker import Faker


def main():
    """
    Основной код программы.
    """
    fake = Faker('ru_Ru')   

    print(fake.name())
    print(fake.ascii_email())
    print(fake.date_between(start_date='-5y'))
    print(fake.phone_number())


if __name__ == "__main__":
    main()
