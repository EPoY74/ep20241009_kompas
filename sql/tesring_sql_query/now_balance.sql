-- Считает баланс на текущий день


SELECT 
    cb.client_id,
    cb.account_id,
    cb.closing_balance,
    SUM(oc.amount) AS operations_now
FROM 
    closing_balance AS cb
JOIN 
    operations_compass AS oc ON cb.account_id = oc.account_id 
    
WHERE cb.account_id = 1
    AND cb.balance_at_day::date = (
        SELECT MAX(balance_at_day::date) 
        FROM closing_balance
        WHERE account_id = 1
    )
 GROUP BY 
    cb.closing_balance,
    cb.client_id,
    cb.account_id
    ;

--- Тестирую и ковыряюсь
SELECT 
    oc.transaction_date,
    cb.client_id,
    cb.account_id,
    oc.amount,
    cb.closing_balance,
    SUM(oc.amount) AS operations_now
FROM 
    closing_balance AS cb
JOIN 
    operations_compass AS oc ON cb.account_id = oc.account_id 
    
WHERE cb.account_id = 1
    -- AND cb.balance_at_day::date = (
    --     SELECT MAX(balance_at_day::date) 
    --     FROM closing_balance
    --     WHERE account_id = 1
    -- )
 GROUP BY 
    oc.transaction_date,
    oc.amount,
    cb.closing_balance,
    cb.client_id,
    cb.account_id
     ORDER BY oc.transaction_date DESC
    ;


-- баланс на другой день

SELECT 
    cb.client_id,
    cb.account_id,
    cb.closing_balance,
    SUM(oc.amount) AS operations_now
FROM 
    closing_balance AS cb
LEFT JOIN 
    operations_compass AS oc 
    ON cb.account_id = oc.account_id 
    
WHERE  cb.account_id = 1 
    AND cb.balance_at_day::date = (
        SELECT balance_at_day::date 
        FROM closing_balance
        WHERE account_id = 1 AND balance_at_day::date < '2023-12-10'
        ORDER BY balance_at_day DESC
        LIMIT 1
        )
    -- AND oc.transaction_date = '2023-12-10' 
 GROUP BY 
    cb.client_id,
    cb.closing_balance,
    cb.account_id
    ;