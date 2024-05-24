
SELECT customer_id, COUNT(*) AS count_no_trans 
FROM visits 
WHERE visit_id NOT IN (SELECT visit_id from transactions)
GROUP BY customer_id;
