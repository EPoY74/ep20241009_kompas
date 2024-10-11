-- Active: 1728491536018@@127.0.0.1@5432@Kompass-db
-- создает таблицу операции
CREATE TABLE IF NOT EXISTS operations_kompass(
    transaction_ID SERIAL PRIMARY KEY,
    account_id INTEGER REFERENCES account_kompass(account_id),
    --сумма операции
    amount DECIMAL (10,2) NOT NULL DEFAULT 0,
    --тип операции (депозит, снятие и тд)б из отдельной таблицы
    operation_type varchar NOT NULL,
    -- дата время авторизации
    authorization_day TIMESTAMP NOT NULL
    --дата время транзакции
    transaction_date TIMESTAMP,
    --описание операции
    operation_description VARCHAR NOT NULL,
    -- в заморозке ли операция для расследования
    is_frozen BOOLEAN NOT NULL DEFAULT FALSE)