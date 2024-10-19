--- добавляю отдельно колонку времени авторизации и транзакции
ALTER TABLE operations_compass 
ADD COLUMN (
    authoriz_time TIMESTAMP NOT NULL, 
    trans_time TIMESTAMP
    )