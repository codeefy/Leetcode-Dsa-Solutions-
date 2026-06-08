# Write your MySQL query statement below
WITH sales AS (
    SELECT
        p.product_id,
        p.price,
        u.units
    FROM Prices p
    LEFT JOIN UnitsSold u
        ON p.product_id = u.product_id
       AND u.purchase_date BETWEEN p.start_date AND p.end_date
)
SELECT
    product_id,
    ROUND(
        IFNULL(SUM(price * units) / NULLIF(SUM(units), 0), 0),
        2
    ) AS average_price
FROM sales
GROUP BY product_id;