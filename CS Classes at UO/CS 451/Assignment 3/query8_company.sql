SELECT p.pname, SUM(w.hours) AS totHours
FROM project p 
JOIN works_on w ON p.pnumber = w.pno
GROUP BY p.pname
HAVING SUM(w.hours) = (SELECT MAX(hours)
FROM (SELECT pno, SUM(hours) AS hours
FROM works_on
GROUP BY pno) AS max_hours)