-- Создает таблицу с остатком на конец дня полте закрытия банковского дня
-- Active: 1728491536018@@127.0.0.1@5432@Kompass-db
CREATE TABLE IF NOT EXISTS closing_balance(
    client_id INTEGER REFERENCES users_compass(client_id),
    account_id INTEGER REFERENCES account_kompass(account_id),
    balance_at_day TIMESTAMP NOT NULL,
    closing_balance DECIMAL(10,2) DEFAULT 0)