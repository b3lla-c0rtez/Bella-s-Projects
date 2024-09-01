SELECT c.fname, c.lname, SUM(i.cost + o.ship_charge) AS totalSpent
FROM orders o
JOIN (
SELECT SUM(total_price) as cost, order_num
FROM items
GROUP BY order_num
) i ON o.order_num = i.order_num
JOIN customer c ON o.customer_num = c.customer_num
GROUP BY c.fname, c.lname
ORDER BY c.lname