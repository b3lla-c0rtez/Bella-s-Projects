SELECT d.dname, dep.dependent_name
FROM dependent dep
JOIN employee e ON e.ssn = dep.essn
RIGHT JOIN department d ON d.dnumber = e.dno
ORDER BY d.dname
