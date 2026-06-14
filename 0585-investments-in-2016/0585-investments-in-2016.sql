WITH policy_stats AS (
    SELECT 
        tiv_2016,
        COUNT(*) OVER (PARTITION BY tiv_2015) AS tiv_2015_count,
        COUNT(*) OVER (PARTITION BY lat, lon) AS location_count
    FROM insurance
)
SELECT 
    CAST(SUM(tiv_2016) AS DECIMAL(18,2)) AS tiv_2016
FROM policy_stats
WHERE tiv_2015_count > 1
  AND location_count = 1;