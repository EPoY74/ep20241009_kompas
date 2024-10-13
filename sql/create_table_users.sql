-- Создает таблицу с пользователями
    CREATE TABLE IF NOT EXISTS users_compass(
    client_id SERIAL PRIMARY KEY,
    first_name VARCHAR NOT NULL,
    second_name VARCHAR,
    surname VARCHAR,
    birthday DATE NOT NULL,
    account_open_day DATE NOT NULL,
    accouns_close_day DATE,
    email VARCHAR,
    phone_number VARCHAR NOT NULL,
    is_blocked boolean NOT NULL DEFAULT FALSE)