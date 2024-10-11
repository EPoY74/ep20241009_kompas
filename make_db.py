"""
Создаю таблицы для хранения финансовой информации
Автор: Евгений Петров
Почта: p174@mail.ru
Дата: 09.10.2024
"""
import create_table


def main():
    """Основной код и логика программы.
    """
    # db_conn : connection = work_postgresql.connection()
    
    # Таблица создана
    # create_table.create_table_users()

    create_table.create_table_account_kompass()
    
    
if __name__ == "__main__":
    main()
