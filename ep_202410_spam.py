"""
Тут я ковыряю всякие там штучки - дрючки не нужные в коде,
но нужные для проекта:)
Автор: Евгений Петров
Почта: p174@mail.ru
Since: 15.10.2024 
"""


def add_char_left(inner_str: str, count_char: int, add_char: chr) -> str:
    """Добавляет слева в строку символ add_char
    в строку inner_str
    заданное количество раз count_char

    Returns:
        str: строка с дополнительными символами
    """
    out_str: str  = inner_str.rjust(count_char, add_char)
    return out_str


if __name__ == "__main__":
    print(add_char_left("Привет", 20, "0"))  
