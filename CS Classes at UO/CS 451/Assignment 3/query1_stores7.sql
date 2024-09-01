SELECT c.fname, c.lname, c.city, s.sname, MD5(c.phone)
FROM customer c
JOIN state s ON s.code = c.state
WHERE s.sname LIKE 'Florida' OR s.sname LIKE 'Oklahoma' OR s.sname LIKE 'ARIZONA'
ORDER BY s.sname LIKE 'OKLAHOMA', s.sname LIKE 'ARIZONA', s.sname LIKE 'FLORIDA'
