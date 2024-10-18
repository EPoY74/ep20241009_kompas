-- Active: 1728491536018@@127.0.0.1@5432@Kompass-db@public
SELECT 
operations_compass.account_id, 
operations_compass.amount, 
operations_compass.transaction_date, 
operations_compass.operation_description 
FROM operations_compass 
WHERE operations_compass.transaction_date
-- по времени - работает. 
BETWEEN '2020-05-26' AND '2021-06-23 06:05:30'
AND operations_compass.account_id = 90  
ORDER BY operations_compass.transaction_date ASC;
