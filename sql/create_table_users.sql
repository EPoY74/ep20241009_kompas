-- Создает таблицу с пользователями
    CREATE TABLE IF NOT EXISTS users_compass(
    client_id SERIAL PRIMARY KEY,
    first_name VARCHAR,
    second_name VARCHAR,
    surname VARCHAR,
    account_open_day DATE,
    accouns_close_day DATE,
    email VARCHAR,
    phone_number VARCHAR,
    is_blocked boolean)