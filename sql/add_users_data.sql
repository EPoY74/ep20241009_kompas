--Добавляет NOT NULL данные в таблицу users_kompass

INSERT INTO users_compass (first_name, birthday, account_open_day, email, phone_number, is_blocked)  VALUES (%s, %s, %s, %s, %s, %s)