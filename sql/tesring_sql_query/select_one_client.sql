SELECT 
operations_compass.account_id, 
operations_compass.amount, 
operations_compass.transaction_date, 
operations_compass.operation_description 
FROM operations_compass 
WHERE operations_compass.account_id = 90  
ORDER BY operations_compass.transaction_date ASC;
