-- Читает дату создания аккаунта из таблицы users_compass
SELECT users_compass.account_open_day 
FROM users_compass
WHERE client_id = %s