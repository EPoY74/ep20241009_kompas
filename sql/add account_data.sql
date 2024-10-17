-- Active: 1728491536018@@127.0.0.1@5432@Kompass-db@public
-- Наполняю таблицу account данными

спраINSERT INTO account_compass
(client_id,
 account_number,
 account_currency,
 account_balance,
 account_type,
 account_created_date)
VALUES (%s, %s, %s, %s, %s, %s)