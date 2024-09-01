SELECT DISTINCT CONCAT(c.fname," " , c.lname) AS customer_name, c.city, c.state, s.description, o.order_date
FROM customer c
JOIN orders o ON c.customer_num = o.customer_num
JOIN items i ON o.order_num = i.order_num
JOIN stock s ON i.stock_num = s.stock_num
JOIN manufact m ON s.manu_code = m.manu_code
JOIN catalog cat ON cat.stock_num = s.stock_num AND cat.manu_code = s.manu_code AND cat.manu_code = i.manu_code AND cat.stock_num = i.stock_num
WHERE o.order_date BETWEEN '1998-05-22' AND '1998-06-25' AND m.manu_name = 'HUSKY' 
ORDER BY customer_name AND o.order_date