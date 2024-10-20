-- Active: 1728491536018@@127.0.0.1@5432@Kompass-db@public
CREATE OR REPLACE  FUNCTION calculate_sum_forid_daily_operations(query_client_id INTEGER)
RETURNS VOID AS $$
BEGIN
    INSERT INTO closing_balance(
        inner_client_id,
        inner_account_id,
        balance_at_day,
        closing_balance
    )
    SELECT 
        us.client_id AS inner_client_id,
        ac.account_id AS inner_account_id,
        oc.transaction_date::date AS balance_at_day,
        SUM(oc.amount) AS closing_balance
    FROM 
        operations_compass AS oc 
        JOIN account_compass AS ac ON oc.account_id = inner_account_id 
        JOIN users_compass AS us ON inner_client_id = ac.client_id 
    WHERE
        inner_account_id = query_client_id
    GROUP BY
        inner_client_id,
        inner_Account_id,
        oc.transaction_date::date;

END;
$$ LANGUAGE PLPGSQL