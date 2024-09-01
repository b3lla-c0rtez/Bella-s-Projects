SELECT title, CONCAT('$',SUM(amount)) AS amtspent
FROM film f
LEFT JOIN inventory i ON f.film_id = i.film_id
LEFT JOIN rental r ON i.inventory_id = r.inventory_id
LEFT JOIN payment p ON r.rental_id = p.rental_id
WHERE f.title LIKE 'I%'
GROUP BY f.title
