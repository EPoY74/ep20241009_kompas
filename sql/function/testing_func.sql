DROP TABLE closing_balance;

SELECT calculate_sum_forid_daily_operations('100');

SELECT  calculate_sum_daily_operations();

SELECT * FROM operations_compass WHERE operations_compass.account_id = 100;

DROP FUNCTION IF EXISTS calculate_sum_forid_daily_operations(INTEGER);

EXPLAIN INSERT INTO closing_balance(
    client_id,
    account_id,
    balance_at_day,
    closing_balance
)
SELECT 
    us.client_id,
    ac.account_id,
    oc.transaction_date::date AS balance_at_day,
    SUM(oc.amount) AS closing_balance
FROM 
    operations_compass AS oc 
    JOIN account_compass AS ac ON oc.account_id = ac.account_id 
    JOIN users_compass AS us ON us.client_id = ac.client_id 
WHERE
    ac.account_id = 100
GROUP BY
    us.client_id,
    ac.account_id,
    oc.transaction_date::date;
