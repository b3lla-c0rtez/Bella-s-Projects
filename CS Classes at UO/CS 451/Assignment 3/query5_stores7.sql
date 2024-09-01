SELECT order_num, customer_num, ship_weight
FROM orders
WHERE ABS(ship_weight-(SELECT AVG(ship_weight) FROM orders)) <= ALL(SELECT ABS(ship_weight - (SELECT AVG(ship_weight) FROM orders)) FROM orders)
