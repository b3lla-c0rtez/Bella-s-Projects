SELECT fname, lname, p.pname
FROM employee 
JOIN works_on w ON employee.ssn = w.essn
JOIN project p ON w.pno = p.pnumber
JOIN (SELECT pno, SUM(hours) AS tothours
FROM works_on
GROUP BY pno
ORDER BY tothours DESC
LIMIT 3) AS top3 ON p.pnumber=top3.pno
ORDER BY lname, p.pname