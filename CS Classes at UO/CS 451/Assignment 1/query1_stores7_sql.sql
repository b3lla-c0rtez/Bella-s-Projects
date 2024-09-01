SELECT fname, lname, company
FROM customer
WHERE company LIKE '% sports%' AND company NOT LIKE '%sports %'