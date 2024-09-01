SELECT DISTINCT stores7.customer.customer_num,fname,lname,city,state,
IF(SUM(total_price) IS NOT NULL,CONCAT('$',SUM(total_price)),"$0") AS totKarsten FROM stores7.customer
LEFT JOIN stores7.orders on stores7.customer.customer_num = stores7.orders.customer_num
LEFT JOIN stores7.items on stores7.orders.order_num = stores7.items.order_num AND items.manu_code="KAR"
GROUP BY stores7.customer.customer_num,stores7.orders.order_num
ORDER BY lname,fname;
