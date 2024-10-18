"""
Тут я ковыряю всякие там штучки - дрючки не нужные в коде,
но нужные для проекта:)
Автор: Евгений Петров
Почта: p174@mail.ru
Since: 15.10.2024 
"""
import time

from progress.bar import Bar


def add_char_left(inner_str: str, count_char: int, add_char: chr) -> str:
    """Добавляет слева в строку символ add_char
    в строку inner_str
    заданное количество раз count_char

    Returns:
        str: строка с дополнительными символами
    """
    out_str: str  = inner_str.rjust(count_char, add_char)
    return out_str

def try_lib_progress():
    """
    Тестирую библиотеку progress, так как похоже
    рассыпается от вложенного цикла
    """
    progress_bar = Bar('Processing', max=100)
    for i in range(100):
        progress_bar.next()
        time.sleep(0.01)  # Задержка для демонстрации
        for j in range(100):
            time.sleep(0.01)  # Задержка для демонстрации
            # Тут не расспается... Почему у меня сыпется в коде?


if __name__ == "__main__":
    # print(add_char_left("Привет", 20, "0"))
    try_lib_progress()
