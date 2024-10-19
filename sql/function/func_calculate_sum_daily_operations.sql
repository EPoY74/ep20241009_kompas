CREATE OR REPLACE  FUNCTION calculate_sum_daily_operations()
RETURN VOID AS $$
BEGIN
    INSERT INTO closing_balance(
        closing_balance.account_id,
        closing_balance.balance_at_day
    )
END;
$$ LANGUAGE PLPGSQL