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
(%s, %s, %s, %s, %s, %s, %s)