SELECT seller_id as id, name, COUNT(id) AS sales_c,
   (SELECT
    SUM(price) AS sales_s,
    DENSE_RANK() OVER (ORDER BY COUNT(id) DESC) AS sales_rank_c
    FROM sales
    GROUP BY employee_id)
FROM employee
GROUP BY id
