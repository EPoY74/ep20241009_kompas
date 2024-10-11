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


if __name__ == "__main__":
    main()
