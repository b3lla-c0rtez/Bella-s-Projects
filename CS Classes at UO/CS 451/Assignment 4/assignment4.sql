SELECT c.fname, c.lname, s.description
FROM customer c
JOIN orders o ON o.customer_num = c.customer_num
JOIN items i ON i.order_num = o.order_num
JOIN stock s ON s.stock_num = i.stock_num
JOIN manufact m ON m.manu_code = s.manu_code
ORDER BY c.fname, c.lname