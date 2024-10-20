SELECT 
    cb.client_id,
    cb.account_id,
    cb.closing_balance,
    SUM(oc.amount) AS operations_now
FROM 
    closing_balance AS cb
JOIN 
    operations_compass AS oc ON cb.account_id = oc.account_id 
    
WHERE cb.account_id = 100 
    AND cb.balance_at_day::date = (
        SELECT MAX(balance_at_day::date) 
        FROM closing_balance
        WHERE account_id = 100
    )
 GROUP BY 
    cb.closing_balance,
    cb.client_id,
    cb.account_id;