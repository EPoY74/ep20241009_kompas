-- добавляет моковые данные в таблицу operations_comapss

INSERT INTO operations_compass
 (
    account_id,
    amount,
    operation_type,
    authorization_day,
    transaction_date,
    operation_description,
    is_frozen
)
VALUES
(90, 200, 'Дебет', "2021-06-23 06:06:09", "2021-06-23 06:06:09", "Вторая операция", FALSE)