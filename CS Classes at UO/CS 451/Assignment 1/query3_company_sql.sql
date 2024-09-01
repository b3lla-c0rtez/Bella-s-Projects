SELECT CONCAT(e1.fname,' ', e1.lname) AS supervisor, CONCAT(e2.fname,' ', e2.lname) AS spervisee
FROM employee e1
JOIN employee e2 ON e1.ssn = e2.superssn
JOIN department d ON e1.dno = d.dnumber AND e2.dno = d.dnumber
WHERE dname = 'Administration'
ORDER BY e1.fname