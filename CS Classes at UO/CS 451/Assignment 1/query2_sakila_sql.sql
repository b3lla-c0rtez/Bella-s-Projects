SELECT c.first_name, c.last_name, c.email, p.amount
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
JOIN rental r ON p.rental_id = r.rental_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON f.film_id = i.film_id
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category cat ON cat.category_id = fc.category_id
WHERE cat.name = 'Drama' AND p.amount > 6
ORDER BY c.last_name