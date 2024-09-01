SELECT d.dname, p.pname, p.plocation
FROM project p
JOIN department d ON p.dnum = d.dnumber
LEFT JOIN dept_locations dl ON p.plocation = dl.dlocation AND p.dnum = dl.dnumber
WHERE dl.dnumber IS NULL
