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
(1, 100, 'Дебет', '2024-10-21 07:07:09', '2024-10-21 07:07:09', 'Четвертая операция', FALSE)



