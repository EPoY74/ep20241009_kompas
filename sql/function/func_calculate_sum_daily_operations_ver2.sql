INSERT INTO closing_balance(
    client_id,
    account_id,
    balance_at_day,
    closing_balance
)
SELECT bal.inner_client_id, bal.inner_account_id, bal.balance_at_day, 
  sum(total_turnover) over (partition by inner_client_id, inner_account_id order by balance_at_day) as real_closing_balance
FROM
  (SELECT
  ac.client_id AS inner_client_id,
      ac.account_id AS inner_account_id,
      oc.transaction_date::date AS balance_at_day,
      SUM(oc.amount) AS total_turnover
  FROM 
      operations_compass AS oc 
      JOIN account_compass AS ac ON ac.account_id = oc.account_id
      -- JOIN users_compass AS us ON ac.client_id = us.client_id
--   WHERE ac.account_id = 100
  GROUP BY
      ac.client_id,
      ac.account_id,
      oc.transaction_date::date) as bal
