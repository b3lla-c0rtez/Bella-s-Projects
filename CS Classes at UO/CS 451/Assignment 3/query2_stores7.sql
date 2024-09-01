SELECT c.customer_num, c.fname, c.lname, c.city, c.state, CONCAT('$', IFNULL(price, 0)) AS totKarsten
FROM customer c
LEFT JOIN 
(SELECT o.customer_num, SUM(i.total_price) AS price
FROM orders o
JOIN items i ON o.order_num = i.order_num
JOIN stock s USING (stock_num, manu_code)
JOIN manufact m ON m.manu_code = s.manu_code 
WHERE m.manu_name = 'Karsten'
GROUP BY o.customer_num
) AS total ON c.customer_num = total.customer_num
GROUP BY c.customer_num, c.fname, c.lname, c.city, c.state
ORDER BY c.lname
