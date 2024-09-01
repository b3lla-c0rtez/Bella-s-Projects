SELECT CONCAT(c.first_name,' ' , c.last_name) AS customer_name, f.title, r.rental_date
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON f.film_id = i.film_id
WHERE MONTH(r.rental_date) = 7 AND YEAR(r.rental_date) = 2005
ORDER BY f.title, c.last_name, r.rental_date
