-- Active: 1728491536018@@127.0.0.1@5432@Kompass-db@public
-- Наполняю таблицу account данными

INSERT IN account_compass (account_compass.client_id,
 account_compass.account_number,
 account_compass.account_currency,
 account_compass.account_balance,
 account_compass.account_type,
 account_compass.account_created_date)
VALUES (%s %s %s %s %s %s)