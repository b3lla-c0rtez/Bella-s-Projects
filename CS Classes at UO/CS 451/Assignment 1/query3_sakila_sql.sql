SELECT COUNT(p.rental_id) 
FROM payment p
JOIN rental r ON p.rental_id = r.rental_id 
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON f.film_id = i.film_id
WHERE f.title LIKE '%MOTHER%'