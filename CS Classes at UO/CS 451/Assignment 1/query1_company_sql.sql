SELECT fname, lname
FROM employee e
JOIN works_on w ON w.essn = e.ssn
JOIN project p ON w.pno = p.pnumber
WHERE p.pname LIKE 'Product%' AND hours >= 8 AND hours <= 22
GROUP BY fname, lname