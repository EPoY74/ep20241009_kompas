-- Active: 1728491536018@@127.0.0.1@5432@Kompass-db@public
-- Спамовые вопросы. Не для сохранения

SELECT COUNT(*) from operations_compass


-- Ищу повторяющиеся строки. Таких при текущем сосбоянии БД не оказалось.
SELECT 
operations_compass.account_id, 
operations_compass.amount, 
operations_compass.transaction_date 
FROM operations_compass 
WHERE operations_compass.transaction_date::date = '2021-06-23'
AND operations_compass.account_id = '90'
GROUP BY operations_compass.transaction_date,
operations_compass.account_id, 
operations_compass.amount;

SELECT operations_compass.transaction_date::date, 
operations_compass.account_id, 
COUNT(*)
FROM operations_compass
GROUP BY operations_compass.transaction_date, 
operations_compass.account_id
HAVING COUNT(*) > 1;

SELECT * 
FROM operations_compass 
WHERE operations_compass.account_id = '33935';


-- не корректный запрос - случайное совпадение client_id и
-- account_id, а может и данные от разных пользователей
SELECT 
users_compass.first_name AS my_client,
operations_compass.amount AS amount,
operations_compass.transaction_date AS my_date,
operations_compass.operation_description AS my_description
FROM users_compass
LEFT JOIN operations_compass
ON users_compass.client_id = operations_compass.account_id
WHERE users_compass.client_id = '158';


-- не работает, не дописал
SELECT users_compass.first_name AS client_name, 
SUM(amount)
FROM operations_compass, users_compass
LEFT JOIN operations_compass
ON users_compass.client_id = operations_compass.client_id

 
 SELECT SUM(operations_compass.amount) 
 AS my_sum
 FROM operations_compass
 WHERE operations_compass.account_id = 100;

 SELECT operations_compass.account_id, operations_compass.amount
 FROM operations_compass
 WHERE operations_compass.account_id = 100;


SELECT * 
FROM operations_compass
WHERE operations_compass.account_id = 10
ORDER BY operations_compass.transaction_date ASC




INSERT INTO closing_balance(
        client_id,
        account_id,
        balance_at_day,
        closing_balance
    )
SELECT  bal.inner_client_id, bal.inner_account_id, bal.balance_at_day, 
  sum(total_turnover) over (partition by inner_client_id, inner_account_id order by balance_at_day) as real_closing_balance
FROM
  (SELECT
  ac.client_id AS inner_client_id,
      ac.account_id AS inner_account_id,
      oc.transaction_date::date AS balance_at_day,
      SUM(oc.amount) AS total_turnover
  FROM 
      operations_compass AS oc 
      JOIN account_compass AS ac ON ac.account_id = oc.account_id
      -- JOIN users_compass AS us ON ac.client_id = us.client_id
 -- WHERE ac.account_id = 100
  GROUP BY
      ac.client_id,
      ac.account_id,
      oc.transaction_date::date) as bal
