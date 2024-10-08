"""
Файл настроек для тестового задания Компас
Требуемые переменные среды:
KOMPASS_DBNAME - Наменование БД
KOMPASS_USER_DB - Имя пользователя БД
KOMPASS_PASSWORD_DB - Пароль от БД
KOMPASS_HOST_DB - Имя хоста БД
KOMPASS_PORT_DB - Порт подключения к БД
"""
import os

print(os.environ)


# Считываю параметры подключеия к БД из
#  переменных окружения операционой системы.
# Они расположены вне кода с целью обеспечения безопасности
#  и снижения риска утечки конфиденциальной информации

# Считываю переменную окружения из ОС с
# наименованием БД KOMPASS_DBNAME
if "KOMPASS_DBNAME" not in os.environ:
    raise ValueError(
      """В переменной KOMPASS_DBNAME 
      должно быть назвнаие БД сервиса. Впиши его, пользователь!"""
      )
KOMPASS_DBNAME = os.environ["KOMPASS_DBNAME"]

# Считываю переменную окружения из ОС с
# именем пользователя БД KOMPASS_USER_DB
if "KOMPASS_USER_DB" not in os.environ:
    raise ValueError(
      """В переменной KOMPASS_USER_DB 
      должно быть имя пользователя БД сервиса. Впиши его, пользователь!"""
      )
KOMPASS_USER_DB = os.getenv("KOMPASS_USER_DB")

# Считываю переменную окружения из ОС с
# # перолем от БД  KOMPASS_PASSWORD_DB
if "KOMPASS_PASSWORD_DB" not in os.environ:
    raise ValueError(
      """В переменной KOMPASS_PASSWORD_DB 
      должty быть пароль БД сервиса. Впиши его, пользователь!"""
      )
KOMPASS_PASSWORD_DB = os.getenv("KOMPASS_PASSWORD_DB")

# Считываю переменную окружения из ОС с
# хостом расположеня БД KOMPASS_HOST_DB
if "KOMPASS_HOST_DB" not in os.environ:
    raise ValueError(
      """В переменной KOMPASS_BOT_HOST_DB 
      должно быть место расположенияя (хост)  БД сервиса. Впиши его, пользователь!"""
      )
KOMPASS_HOST_DB = os.getenv("KOMPASS_HOST_DB")

# Считываю переменную окружения из ОС с
# портом подключения к БД KOMPASS_PORT_DB
if "KOMPASS_PORT_DB" not in os.environ:
    raise ValueError(
      """В переменной KOMPASS_PORT_202407_DB 
      должен быть порт подключения к  БД сервиса. Впиши его, пользователь!"""
      )
KOMPASS_PORT_DB= os.getenv("KOMPASS_PORT_DB")
