-- Создает талицу со счетами клиентов банка
CREATE TABLE IF NOT EXIST account_kompass(
    account_id SERIAL PRIMARY KEY,
    client_id integer REFERENCES table_users(client_id),
    accoutn_number VARCHAR NOT NULL,
    -- валюту счета нажно забирать из другой таблицы
    account_currency VARCHAR NOT NULL,
    -- 10 это обая точность (presition)
    -- 2 это масштаб (scale)
    account_balance DECIMAL(10:2) DEFAULT 0,
    -- Данные account_type  нужно забирать из другой таблицы
    -- что бы нельзя было накосячить и создать счет с непонятным типом
    account_type VARCHAR NOT NULL,
    account_created_date: TIMESTAMP NOT NULL,
    account_cloused_date: TIMESTAMP);