-- Читаю строки из users_compass
SELECT client_id, first_name 
FROM users_compass 
WHERE users_compass.client_id
BETWEEN
15 AND 25;
