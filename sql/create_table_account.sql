-- Создает талицу со счетами клиентов банка
CREATE TABLE IF NOT EXISTS account_сompass(
    account_id SERIAL PRIMARY KEY,
    client_id INTEGER REFERENCES users_compass(client_id),
    --номер счета
    account_number VARCHAR NOT NULL,
    -- валюту счета нажно забирать из другой таблицы
    account_currency VARCHAR NOT NULL,
    -- 10 это общая точность (precision)
    -- 2 это масштаб (scale)
    account_balance DECIMAL(10,2) DEFAULT 0,
    -- Данные account_type  нужно забирать из другой таблицы
    -- что бы нельзя было накосячить и создать счет с непонятным типом
    account_type VARCHAR NOT NULL,
    account_created_date TIMESTAMP NOT NULL,
    account_closed_date TIMESTAMP);