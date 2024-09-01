SELECT s.sname, c.fname, c.lname
FROM state s
LEFT JOIN customer c ON s.code = c.state
ORDER BY s.sname, c.lname
