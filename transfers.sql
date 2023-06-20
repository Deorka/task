SELECT acc, dt_from, dt_to, balance
    FROM (
    SELECT acc, balance, date_trunc('month', date) AS dt_from,
        date_trunc('month', date + interval '1 month') - interval '1 day' AS dt_to,
        SUM(balance) OVER (PARTITION BY account, date_trunc('month', date)) AS balance_sum,
        AVG(balance) OVER (PARTITION BY account, date_trunc('month', date)) AS balance_avg
        FROM transfers
        ) subquery
        WHERE balance_avg >= balance_sum * 0.95;
        ORDER BY account, dt_from
