SELECT stock_num, manu_code, description, unit_price, unit, unit_descr
FROM stock
WHERE (stock_num, manu_code) NOT IN (SELECT stock_num, manu_code FROM items)